from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# NASA EONET API URL
EONET_API_URL = 'https://eonet.gsfc.nasa.gov/api/v2.1/events'

@app.route('/')
def home():
    return "Welcome to the Disaster Data API! Please go to /disasters to see the events."

@app.route('/disasters', methods=['GET'])
def get_disasters():
    try:
        # Get query parameters for filtering
        limit = request.args.get('limit', 10)  # Default to 5 events
        status = request.args.get('status', 'open')  # Default to open events
        days = request.args.get('days', 20)  # Default to past 7 days
        
        # Construct API request URL
        params = {
            'limit': limit,
            'status': status,
            'days': days
        }

        # Make a GET request to EONET API
        response = requests.get(EONET_API_URL, params=params)

        if response.status_code == 200:
            events = response.json()

            # Function to handle missing date and content
            def parse_event(event):
                # Handle missing date from geometry or properties
                date = None
                if event.get('geometry') and isinstance(event['geometry'], list) and len(event['geometry']) > 0:
                    date = event['geometry'][0].get('date')
                
                if not date and event.get('properties'):
                    date = event['properties'].get('date')
                
                if not date:
                    date = 'No date available'

                # Handle missing content (description)
                content = event.get('description', 'No description available')

                return {
                    "title": event.get("title", "No title available"),
                    "date": date,
                    "content": content
                }

            # Process the events and ensure all fields are populated
            simplified_events = [parse_event(event) for event in events.get("events", [])]

            return jsonify(simplified_events), 200
        else:
            return jsonify({'error': 'Failed to fetch events from EONET API'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
