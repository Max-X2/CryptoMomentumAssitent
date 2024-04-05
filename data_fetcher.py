import pandas as pd
import requests
from config import API_KEY, BASE_URL, timeframes_config

def fetch_crypto_data(crypto, timeframe, limit):
    # Extract endpoint and aggregate information from the consolidated configuration using the timeframe parameter
    endpoint, aggregate = timeframes_config[timeframe]['endpoint']
    
    # Construct the API URL with the specified parameters
    url = f"{BASE_URL}{endpoint}?fsym={crypto}&tsym=USD&limit={limit}&aggregate={aggregate}&api_key={API_KEY}"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the response is successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response and convert it to a Pandas DataFrame
        data = response.json()['Data']['Data']
        df = pd.DataFrame(data)
        # Convert the 'time' column to a datetime format for easier manipulation
        df['time'] = pd.to_datetime(df['time'], unit='s')
        return df
    else:
        # If the response is not successful, raise an error with the HTTP status code
        response.raise_for_status()
