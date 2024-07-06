import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=J40JYFDGGPQBLB3W'
r = requests.get(url)
data = r.json()

print(data['Meta Data'])
print("=========================================================================================================================")
key_date = None
for index, date in enumerate(data['Time Series (Daily)'].keys(), start=1):
    print(f"{index} : {date}")
    if index == 1:
        key_date = date
print("==========================================================================================================================")
print("Type of data from daily dictionary: ")
print(f"Date : {key_date}")
print(data['Time Series (Daily)'][key_date])
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Learning git")