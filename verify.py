import hashlib

log = "/storage/emulated/0/Hackclub/blackbox/blackbox.log"
prev = "0"*64
ok = True

with open(log) as f:
    block = []
    for line in f:
        line=line.strip()
        if line == "---":
            payload = "\n".join(block[:-1])
            hash_line = block[-1].split("=")[1]
            h = hashlib.sha256(payload.encode()).hexdigest()
            if h != hash_line or prev not in payload:
                ok = False
                break
            prev = hash_line
            block=[]
        else:
            block.append(line)

print("OK" if ok else "TAMPERED")
