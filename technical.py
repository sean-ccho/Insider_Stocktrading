import requests
import json
from datetime import datetime
import time

today = datetime.today()
dateToday = today.strftime("%Y-%m-%d")

url = 'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=daily&time_period=10&series_type=open&apikey=5BXBGO0O397FNY19'
r = requests.get(url)
data = r.json()

sma_value = data["Technical Analysis: SMA"][dateToday]["SMA"]
# print(type(sma_value))
print(sma_value)

# print(data)