from matplotlib import pyplot as plt
from data_fetcher import fetch_crypto_data
from analysis import calculate_squeeze_momentum, calculate_smi, normalize_smi
import strategy
import config
from visualization import plot_squeeze_momentum

def main():
    # Initialize a dictionary to hold the SMI data for each timeframe
    timeframe_data = {}
    
    # Iterate over each timeframe defined in the consolidated configuration
    for tf in config.timeframes_config.keys():
        print(f"Fetching data for {tf} timeframe...")
        # Fetch cryptocurrency data for the current timeframe
        df = fetch_crypto_data(config.CRYPTO_SYMBOL, tf, config.DATA_LIMIT)
        
        print(f"Calculating Squeeze Momentum for {tf} timeframe...")
        # Calculate the Squeeze Momentum Indicator for the fetched data
        smi_df = calculate_squeeze_momentum(df)
        # Calculate the Simple Moving Average (SMI) on the SMI data
        df = calculate_smi(smi_df)
        # Normalize the SMI data for comparison across timeframes
        smi_df = normalize_smi(df)
        
        # Store the processed data for the current timeframe
        timeframe_data[tf] = smi_df

    # Decide whether to display all plots in a single subplot window or individually
    subplot_mode = True  # Change to False to plot each timeframe individually
    # Display the Squeeze Momentum Indicator plots
    plot_squeeze_momentum(timeframe_data, subplot_mode=subplot_mode)
    
    # Evaluate the trading strategy based on the SMI data and calculate scores for each timeframe
    strategy_scores = strategy.evaluate_optimized_strategy(timeframe_data)
    # Plot the combined strategy visualization including strategy scores and intuitive momentum changes
    strategy.plot_combined_strategy_visualization(strategy_scores, timeframe_data)
    # Calculate the weighted average score of the strategy across all timeframes
    weighted_average_score = strategy.calculate_weighted_average_score(strategy_scores, config.timeframes_config)
    # Generate and print a summary of the strategy evaluation
    strategy.generate_strategy_summary(strategy_scores, weighted_average_score, config.timeframes_config)

if __name__ == "__main__":
    main()
    plt.show()

