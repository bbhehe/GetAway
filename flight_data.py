import requests

def get_flight_data():
    # Make a request to the Google Flights API
    response = requests.get('https://serpapi.com/search.html?engine=google_flights&departure_id=BUD&arrival_id=VIE&gl=us&hl=en&currency=USD&outbound_date=2024-05-08&return_date=2024-05-14&api_key=f993cfbb3db7547d47cfae99621152f1288a15b909a385b7e515ae6e3758ac8f')

    # Process the response data
    if response.status_code == 200:
        flight_data = response.json()
        # Process flight data as needed
        print(flight_data)
    else:
        print('Error:', response.status_code)

if __name__ == "__main__":
    get_flight_data()
