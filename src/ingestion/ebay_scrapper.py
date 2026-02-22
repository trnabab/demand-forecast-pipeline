import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")

url = "https://svcs.ebay.com/services/search/FindingService/v1"

params = {
    "OPERATION-NAME": "findCompletedItems",
    "SECURITY-APPNAME": os.getenv("EBAY_APP_ID"),
    "RESPONSE-DATA-FORMAT": "JSON",
    "keywords": "dumbbells",
    "GLOBAL-ID": "EBAY-AU",
}

response = requests.get(url, params=params)

print(response.json())
