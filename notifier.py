import urllib.parse
import urllib.request
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("logString")
args = parser.parse_args()

# paste your bot token and telegram user id here 
token=""
chatid=""

url=f"https://api.telegram.org/bot{token}/sendMessage"
message= urllib.parse.urlencode({
  "chat_id": chatid,
  "text": args.logString
}).encode("utf-8")

request = urllib.request.Request(url, data=message)

with urllib.request.urlopen(request) as responce:
  result = responce.read()
  print(json.loads(result))
