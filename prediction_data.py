import yfinance as yf
from prophet import Prophet
import pandas as pd
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
    
    # 予測結果保存（実データ+予測データ）
    forecast_data[name] = forecast[['ds', 'yhat']]
    forecast.to_csv(f'{name}_forecast.csv', index=False)

print("データ取得と予測が完了しました。")
