#!/data/data/com.termux/files/usr/bin/bash

TS=$(date -Is)

# Network status + latency
PING_OUT=$(ping -c 1 -W 1 8.8.8.8 2>/dev/null)

if echo "$PING_OUT" | grep -q "time="; then
  STATUS="UP"
  LATENCY=$(echo "$PING_OUT" | sed -n 's/.*time=\([0-9.]*\).*/\1/p')
else
  STATUS="DOWN"
  LATENCY="NA"
fi

echo "TIME=$TS"
echo "STATUS=$STATUS"
echo "LATENCY_MS=$LATENCY"
echo "===="
