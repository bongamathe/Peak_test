import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=J40JYFDGGPQBLB3W'
r = requests.get(url)
data = r.json()

print(data['Meta Data'])
print("=========================================================================================================================")
print(data['Time Series (5min)'])
print("=========================================================================================================================")
print(data)