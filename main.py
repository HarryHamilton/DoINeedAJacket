import requests
from statistics import mean
""" Somes end points for future reference
print(data["timeseries"][0])  # This accesses the timeseries part of the json
print(data["timeseries"][0]["latest"])  # accesses "latest" part of json
"""

endpoint = ["https://api.usb.urbanobservatory.ac.uk/api/v2/sensors/feed/room-3-018-zone-1/room-temperature",
            "https://api.usb.urbanobservatory.ac.uk/api/v2/sensors/feed/room-3-018-zone-2/room-temperature",
            "https://api.usb.urbanobservatory.ac.uk/api/v2/sensors/feed/room-3-018-zone-3/room-temperature",
            "https://api.usb.urbanobservatory.ac.uk/api/v2/sensors/feed/room-3-018-zone-4/room-temperature", ]

temps = []
for i in range(len(endpoint)):
    response = requests.get(endpoint[i])
    data = response.json()
    temps.append(data["timeseries"][0]["latest"]["value"])  # accesses the value :)

if (mean(temps) < 18.0):
    print("The temperature is", mean(temps), "c you need a jacket")
else:
    print("The temperature is", mean(temps), "c you don't a jacket")






