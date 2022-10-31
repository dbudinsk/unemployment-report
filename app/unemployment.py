# this is the "app/unemployment_report.py" file...

import os
import json
from pprint import pprint

import requests

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)



# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date? 
# Display the unemployment rate using a percent sign.

breakpoint()

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
#print(data[0])
print(f"{data[0]['value']}%", "as of", data[0]["date"])





