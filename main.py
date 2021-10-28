import requests
import json

response = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/feed/816ce6c0-ac7b-4525-90d1-1055f6b83bc0")
print(response.json())
