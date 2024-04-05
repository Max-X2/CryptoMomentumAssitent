import pandas as pd
import numpy as np
import ta

def calculate_squeeze_momentum(df, length=20, mult=2.0, lengthKC=20, multKC=1.5):
    """
    Calculate Squeeze Momentum Indicator components including Bollinger Bands and Keltner Channels.
    """
    # Bollinger Bands
    basis = df['close'].rolling(window=length).mean()
    dev = mult * df['close'].rolling(window=length).std()
    df['upperBB'] = basis + dev
    df['lowerBB'] = basis - dev

    # Keltner Channel
    ma = df['close'].rolling(window=lengthKC).mean()
    range_ma = (df['high'] - df['low']).rolling(window=lengthKC).mean()
    df['upperKC'] = ma + range_ma * multKC
    df['lowerKC'] = ma - range_ma * multKC

    # Squeeze Indicator
    df['sqzOn'] = (df['lowerBB'] > df['lowerKC']) & (df['upperBB'] < df['upperKC'])
    df['sqzOff'] = (df['lowerBB'] < df['lowerKC']) & (df['upperBB'] > df['upperKC'])

    # Momentum Calculation
    m1 = df['high'].rolling(window=lengthKC).max()
    m2 = df['low'].rolling(window=lengthKC).min()
    df['val'] = (df['close'] - ((m1 + m2) / 2 + ma) / 2).rolling(window=lengthKC).apply(lambda x: np.polyfit(np.arange(lengthKC), x, 1)[0], raw=True)

    return df

def calculate_smi(df):
    """
    Calculate Squeeze Momentum Indicator (SMI) and its normalization.
    """
    # Bollinger Bands
    indicator_bb = ta.volatility.BollingerBands(close=df["close"])
    df['bollinger_width'] = indicator_bb.bollinger_hband() - indicator_bb.bollinger_lband()

    # Keltner Channel
    indicator_kc = ta.volatility.KeltnerChannel(high=df["high"], low=df["low"], close=df["close"])
    df['keltner_width'] = indicator_kc.keltner_channel_hband() - indicator_kc.keltner_channel_lband()

    # Squeeze Indicator (Boolean)
    df['squeeze_on'] = df['bollinger_width'] < df['keltner_width']

    # Calculate SMI as the difference in widths (simplified)
    df['SMI'] = df['bollinger_width'] - df['keltner_width']

    return df

def normalize_smi(df):
    """
    Normalize Squeeze Momentum Indicator (SMI) to the range of -1 to +1.
    """
    smi_max, smi_min = df['SMI'].max(), df['SMI'].min()

    df['normalized_SMI'] = df['SMI'].apply(lambda x: 2 * (x - smi_min) / (smi_max - smi_min) - 1 if (smi_max - smi_min) != 0 else 0)

    return df
