import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  # Ensure pandas is imported if you need to manipulate or inspect dataframe within the plotting functions
import math
from config import timeframes_config


def plot_squeeze_momentum(timeframe_data, subplot_mode=False, num_periods=50):
    """
    Plot the Squeeze Momentum Indicator for specified timeframes.
    Can plot each timeframe individually or all in subplots based on the subplot_mode flag.
    Assumes timeframe_data is either a single DataFrame (when subplot_mode=False) 
    and tf is specified, or a dictionary with timeframes as keys and DataFrames as values 
    (when subplot_mode=True).
    
    Parameters:
    - timeframe_data: DataFrame or dict of DataFrames
    - subplot_mode: bool, default False. If True, plots all timeframes in a subplot grid.
    - num_periods: int, default 50. Number of periods to display from the end of the DataFrame.
    """
    if subplot_mode:
        num_timeframes = len(timeframe_data)
        grid_size = math.ceil(np.sqrt(num_timeframes))
        fig, axs = plt.subplots(grid_size, grid_size, figsize=(15, 10))
        fig.suptitle('Squeeze Momentum Indicator Across Timeframes')
        
        axs = axs.flatten()
        for i, (tf, df) in enumerate(timeframe_data.items()):
            if 'val' in df.columns:
                df_last_N = df.tail(num_periods)
                colors = df_last_N['val'].apply(lambda x: 'green' if x > 0 else 'red')
                axs[i].bar(df_last_N.index, df_last_N['val'], color=colors)
                axs[i].set_title(f'{tf} timeframe')
            else:
                print(f"No 'val' column found in dataframe for {tf} timeframe.")
                axs[i].set_visible(False)
        
        # Hide unused subplots
        for j in range(i + 1, len(axs)):
            axs[j].set_visible(False)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show(block=False)
    else:
        for tf, df in timeframe_data.items():
            plt.figure(figsize=(10, 6))
            if 'val' in df.columns:
                df_last_N = df.tail(num_periods)
                colors = df_last_N['val'].apply(lambda x: 'green' if x > 0 else 'red')
                plt.bar(df_last_N.index, df_last_N['val'], color=colors)
                plt.title(f'Squeeze Momentum Indicator for {tf} timeframe')
            else:
                print(f"No 'val' column found in dataframe for {tf} timeframe.")
            plt.show(block=False)




def plot_momentum_with_direction_changes(timeframe_data):
    """
    Plot momentum with directional changes for each timeframe.
    Assumes timeframe_data is a dictionary with timeframes as keys and dataframes as values.
    """
    plt.figure(figsize=(14, 8))
    markers = {'up': '^', 'down': 'v'}
    
    for tf, df in timeframe_data.items():
        if not df.empty and 'val' in df.columns:
            current_momentum = df['val'].iloc[-1]
            previous_momentum = df['val'].iloc[-2] if len(df) > 1 else 0
            
            # Determine marker type based on momentum change
            marker = markers['up'] if current_momentum > previous_momentum else markers['down']
            color = 'green' if current_momentum > 0 else 'red'
            
            plt.plot(df.index[-2:], df['val'].iloc[-2:], marker=marker, color=color, label=f"{tf} momentum change")

    plt.legend()
    plt.show()

def plot_strategy_scores(strategy_scores):
    """
    Plot strategy evaluation scores across different timeframes.
    Assumes strategy_scores is a dictionary with timeframes as keys and scores as values.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    timeframes = list(strategy_scores.keys())
    scores = list(strategy_scores.values())
    
    colors = ['red' if score < 0 else 'green' for score in scores]
    ax.bar(timeframes, scores, color=colors)
    ax.axhline(0, color='grey', linestyle='--')
    ax.set_ylabel('Strategy Score (-100 to +100)')
    ax.set_title('Strategy Evaluation Scores Across Timeframes')
    plt.show()

def plot_intuitive_momentum_changes(timeframe_data):
    """
    Plot intuitive momentum changes across different timeframes.
    Assumes timeframe_data is a dictionary with timeframes as keys and dataframes as values.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    timeframes = list(timeframes_config.keys())


    current_momentum = [df['val'].iloc[-1] if 'val' in df.columns else 0 for df in timeframe_data.values()]
    ypos = np.arange(len(timeframes))
    
    colors = ['green' if val > 0 else 'red' for val in current_momentum]
    ax.barh(ypos, current_momentum, color=colors, tick_label=timeframes)
    
    ax.axvline(0, color='grey', linestyle='--')
    ax.set_xlabel('Momentum Value')
    ax.set_title('Momentum and Direction Change Across Timeframes')
    
    plt.tight_layout()
    plt.show()
