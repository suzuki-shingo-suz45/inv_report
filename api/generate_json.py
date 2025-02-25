import json
import random
from datetime import datetime, timedelta

def handler(request):
    # 株価予測データを生成
    start_date = datetime(2023, 1, 1)
    dates = []
    dow_forecast = []
    sp500_forecast = []

    for i in range(365):  # 1年間分の日付データを生成
        date = start_date + timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))
        dow_forecast.append(round(random.uniform(30000, 35000), 2))
        sp500_forecast.append(round(random.uniform(3500, 4500), 2))

    # JSONデータを作成
    data = {
        "dow": {
            "forecast": [{"date": dates[i], "value": dow_forecast[i]} for i in range(len(dates))]
        },
        "sp500": {
            "forecast": [{"date": dates[i], "value": sp500_forecast[i]} for i in range(len(dates))]
        }
    }

    # JSONレスポンスとして返す
    return json.dumps(data)
