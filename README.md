# CryptoMomentumAssistant

## Project Overview

CryptoMomentumAssistant is a Python-based toolkit designed for cryptocurrency traders and market analysts. This project focuses on analyzing the Squeeze Momentum Indicator (SMI) across several timeframes to identify potential reversals in market momentum. It provides an early look at how data-driven insights can inform trading strategies, leveraging statistical analysis to pinpoint critical market movements.

## Features

- **Timeframe Analysis:** Examine cryptocurrency momentum across a range of timeframes to capture a comprehensive market view.
- **Momentum Reversal Detection:** Identify potential reversals in momentum, offering insights into possible entry and exit points.
- **Configurable:** Flexible configuration options allow users to tailor the analysis to their specific trading strategies and preferences.

## Getting Started

To get started with CryptoMomentumAssistant, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alireza787b/CryptoMomentumAssistant.git
   ```

2. **Set up your environment:**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure your API key:**
## Configure your API Key

To access cryptocurrency data, CryptoMomentumAssistant requires an API key from CryptoCompare. If you don't already have one, you can obtain a free API key by signing up at [CryptoCompare](https://min-api.cryptocompare.com/).

After obtaining your API key, set up your configuration file as follows:

**Create a `secrets.py` file** in the project's root directory.

**Open `secrets.py`** in your text editor and add the following line:

    ```python
    API_KEY_SECRET = "YOUR_SECRET_API_FROM_CRYPTOCOMPARE"
    ```

Replace `YOUR_SECRET_API_FROM_CRYPTOCOMPARE` with the actual API key you obtained from CryptoCompare.




4. **Run the analysis:**
   - Execute the main script to begin the analysis:
     ```bash
     python main.py
     ```

## Future Directions

The current implementation serves as a foundation for a more sophisticated analysis framework. The next phase of this project will involve incorporating machine learning algorithms to enhance the prediction of market movements, automating the detection of trading opportunities based on historical data trends and patterns.

## Contributing

Contributions to CryptoMomentumAssistant are welcome! Whether it's feature requests, bug reports, or code contributions, please feel free to reach out or submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).