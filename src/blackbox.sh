#!/data/data/com.termux/files/usr/bin/bash

LOG="/storage/emulated/0/Hackclub/blackbox/blackbox.log"
INTERVAL=60

mkdir -p /storage/emulated/0/Hackclub/blackbox

last_hash() {
  if [ ! -f "$LOG" ]; then
    echo "0000000000000000000000000000000000000000000000000000000000000000"
    return
  fi
  grep '^HASH=' "$LOG" | tail -n 1 | cut -d= -f2
}

while true; do
  TS=$(date -Is)

  PING=$(ping -c 1 -W 1 8.8.8.8 2>/dev/null)
  if echo "$PING" | grep -q "time="; then
    STATUS="UP"
    LAT=$(echo "$PING" | sed -n 's/.*time=\([0-9.]*\).*/\1/p')
  else
    STATUS="DOWN"
    LAT="NA"
  fi

  PREV=$(last_hash)

  PAYLOAD=$(cat <<EOF
TIME=$TS
STATUS=$STATUS
LATENCY_MS=$LAT
PREV=$PREV
EOF
)

  CURR=$(echo "$PAYLOAD" | sha256sum | cut -d' ' -f1)

  {
    echo "$PAYLOAD"
    echo "HASH=$CURR"
    echo "---"
  } >> "$LOG"

  sleep "$INTERVAL"
done
