#!/bin/ash

TOKEN=""
CHAT_ID=""

PATTERN="authpriv\.info|authpriv\.notice|daemon\.err uhttpd"

send_to_telegram() {
  MESSAGE=$1
  URL="https://api.telegram.org/bot${TOKEN}/sendMessage?chat_id=${CHAT_ID}&text=$(echo "$MESSAGE" | sed 's/ /%20/g')"
  wget -qO- "$URL" > /dev/null
}

while IFS= read -r line; do
  if echo "$line" | grep -qE "$PATTERN"; then
    send_to_telegram "$line"
  fi
done
