# Stock Data Flask Application

This project is a Flask application for retrieving historical stock prices from Yahoo Finance and saving them to CSV files.

## Getting Started

- Clone this repository to your local machine.
- Install the required dependencies using `pip install -r requirements.txt`.
- Run the Flask application by executing the `main.py` file.

## Usage

To retrieve historical prices for a specific stock, use the endpoint `/get_historical_prices`.

Example: `http://localhost:5000/get_historical_prices?symbol=AAPL&period=1mo`

To save historical prices for a specific stock to a CSV file, use the endpoint `/save_to_csv`.

Example: `http://localhost:5000/save_to_csv?symbol=AAPL&period=1mo`

## Parameters

- `symbol`: The stock symbol (e.g., AAPL for Apple Inc.).
- `period`: The time period for historical prices (e.g., 1d, 1mo, 1y, max). Default is 1 month (1mo).

## Response

- The `/get_historical_prices` endpoint returns a JSON object containing historical price data.
- The `/save_to_csv` endpoint returns a JSON object with a message confirming that the data has been saved to a CSV file.

## Example

1. Retrieve historical prices for Apple Inc. for the last month:
   - Endpoint: `http://localhost:5000/get_historical_prices?symbol=AAPL&period=1mo`
   - Response: JSON object containing historical price data.

2. Save historical prices for Apple Inc. for the last month to a CSV file:
   - Endpoint: `http://localhost:5000/save_to_csv?symbol=AAPL&period=1mo`
   - Response: JSON object with a message confirming that the data has been saved to a CSV file.

## Notes

- Ensure that the stock symbol is valid and exists on Yahoo Finance.
- Period options include `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `ytd`, and `max`.
- CSV files are saved with the following format: `<symbol>_<period>_<current_date>.csv`.
- Timestamps in the CSV files are formatted as `YYYY-MM-DD`.
- Feel free to explore and customize the application as needed!
