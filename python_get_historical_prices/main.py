from flask import Flask, request, jsonify
from stock_data import StockData

app = Flask(__name__)
stock_data = StockData()

## /get_historical_prices?symbol=AAPL&period=max
@app.route('/get_historical_prices', methods=['GET'])
def get_historical_prices():
    symbol = request.args.get('symbol')
    period = request.args.get('period', '1mo')
    historical_prices = stock_data.get_historical_prices(symbol, period)
    return jsonify(historical_prices.to_dict())

## /save_to_csv?symbol=AAPL&period=1max
@app.route('/save_to_csv', methods=['GET'])
def save_to_csv():
    symbol = request.args.get('symbol')
    period = request.args.get('period', '1mo')
    stock_data.save_to_csv(symbol, period)
    return jsonify({'message': 'Data saved to CSV'})

if __name__ == '__main__':
    app.run(debug=True)
