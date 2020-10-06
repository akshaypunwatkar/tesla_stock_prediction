import http.client
import json

conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "5d79aadd91msh6e2014127ab2d99p15695djsn9d67a28ba3ed"
    }

conn.request("GET", "/stock/v3/get-historical-data?region=US&symbol=TSLA", headers=headers)

res = conn.getresponse()
data = res.read()

with open('data/tesla_stock_historical.json', 'w') as out:
    out.write(data.decode("utf-8")+'\n')

print("\nStreaming completed\n")

# print(data.decode("utf-8"))