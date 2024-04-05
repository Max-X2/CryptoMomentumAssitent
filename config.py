from secrets import API_KEY_SECRET
BASE_URL = 'https://min-api.cryptocompare.com/data/v2/'


# Configuration for fetching data
API_KEY = API_KEY_SECRET
CRYPTO_SYMBOL = 'BTC'
timeframes_config = {
    '1m': {'endpoint': ('histominute', 1), 'weight': 0.5},
    '5m': {'endpoint': ('histominute', 5), 'weight': 0.5},
    '15m': {'endpoint': ('histominute', 15), 'weight': 1},
    '30m': {'endpoint': ('histominute', 30), 'weight': 1},
    '1h': {'endpoint': ('histohour', 1), 'weight': 2},
    '4h': {'endpoint': ('histohour', 4), 'weight': 3},
    '1d': {'endpoint': ('histoday', 1), 'weight': 4},
}
DATA_LIMIT = 2000

