import re

log = "/storage/emulated/0/Hackclub/blackbox/blackbox.log"
total = up = 0
latencies = []

with open(log)as f:
    for line in f:
        if line.startswith("STATUS="):
         total += 1

        if "UP" in line:
            up += 1

        if line.startswith("LATENCY_MS="):
         val = line.strip().split("=")[1]
         if val !="NA":
             latencies.append(float(val))

    if total == 0:
      print("No Data!!")
      exit()


    uptime = (up / total) * 100
    avg = sum(latencies)/len(latencies) if latencies else 0

    print(f"Samples: {total}")
    print(f"Uptime: {uptime:.2f}%")
    print(f"Latency avg/min/max: {avg:.1f} / {min(latencies):.1f} / {max(latencies):.1f} ms")




