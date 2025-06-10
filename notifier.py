import sys
import re
import urllib.parse
import urllib.request
import json

pattern = re.compile("authpriv\.info|authpriv\.notice|daemon\.err uhttpd") # it will grep only ssh session start and close, ssh login with publickey and luci successful logins
def notifier(messageToSend):
  # enter your bot token and telegram account (or group) id
  token=""
  chatid=""

  url=f"https://api.telegram.org/bot{token}/sendMessage"
  message=urllib.parse.urlencode({
    "chat_id": chatid,
    "text": messageToSend
  }).encode("utf-8")

  request = urllib.request.Request(url, data=message)

  try:
    with urllib.request.urlopen(request) as responce:
      result=responce.read()
      print(json.loads(result))
  except Exception as e:
    print("something went wrong") # this log is useless because you can't really read it. Replace it with subprocess and loger (openwrt) call if you need

def main():
  for log_line in sys.stdin():
    if pattern.search(log_line):
      notifier(messageToSend=log_line)
  
if __name__ == "__main__":
  main()
