import yfinance as yf
from prophet import Prophet
import pandas as pd
import json
from datetime import datetime, timedelta

# 現在の日付を取得
today = datetime.today()
start_date = (today - timedelta(days=180)).strftime('%Y-%m-%d')  # 過去6ヶ月
end_date = today.strftime('%Y-%m-%d')  # 現在

# 対象とする指数のティッカーシンボル
tickers = {
    'Dow Jones': '^DJI',
    'S&P 500': '^GSPC',
    'NASDAQ': '^IXIC',
    'Nikkei 225': '^N225'
}

# データ取得と予測
forecast_data = {}

for name, ticker in tickers.items():
    # データ取得
    df = yf.download(ticker, start=start_date, end=end_date)
    df.reset_index(inplace=True)
    df = df[['Date', 'Close']]
    df.columns = ['ds', 'y']
    
    # モデル構築
    model = Prophet()
    model.fit(df)
    
    # 予測期間設定（30日先まで）
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    # 予測結果を辞書形式で保存
    forecast_data[name] = forecast[['ds', 'yhat']].to_dict(orient='records')  # 予測結果を辞書形式で格納

# forecast_dataをJSON形式で保存
with open('https://inv.suz45.net/program/inv_report/forecast_data.json', 'w') as f:
    json.dump(forecast_data, f, indent=4)

print("データ取得と予測が完了し、forecast_data.jsonに保存しました。")
