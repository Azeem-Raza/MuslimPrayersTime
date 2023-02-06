import requests
import json
#You can enter your city through link
url = "https://dailyprayer.abdulrcs.repl.co/api/vaasa"
response = requests.get(url)
data = response.json()
print(data['city'])
print(data['date'])
for prayer in data["today"]:
  print(prayer + ": " + data["today"][prayer])
print("Prayer Times for next day: ")
# If you want to request for tomorrow prayer's time:
for prayer in data["tomorrow"]:
    print(prayer + ": " + data["tomorrow"][prayer])