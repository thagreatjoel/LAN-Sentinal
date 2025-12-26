import sys, hashlib, os, time

LOG = "/storage/emulated/0/Hackclub/blackbox/blackbox.log"

def last_hash():
    if not os.path.exists(LOG):
        return "0"*64
    with open(LOG, "rb") as f:
        lines = f.read().split(b"\n")
        for l in reversed(lines):
            if l.startswith(b"HASH="):
                return l.decode().split("=")[1]
    return "0"*64

data = sys.stdin.read().strip()
if not data:
    sys.exit(0)

prev = last_hash()
payload = f"{int(time.time())}\n{data}\nPREV={prev}"
curr = hashlib.sha256(payload.encode()).hexdigest()

with open(LOG, "a") as f:
    f.write(payload + f"\nHASH={curr}\n---\n")
