"""
M4STCLAW v5 | Project: Sentinel-Bypass Unified Research Suite
Goal: Provides a zero-dependency CLI dashboard to probe rate-limits, extract security tokens,
      and test browser telemetry suppression.
"""

import sys
import os
import re
import json
import time
import hashlib
import requests
from datetime import datetime

# ANSI colors for zero-dependency high-fidelity console logs
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

class SentinelSuite:
    def __init__(self):
        self.session = requests.Session()
        self.research_log = "sentinel_research_log.json"
        self.log_data = []
        self._load_existing_log()

    def _load_existing_log(self):
        if os.path.exists(self.research_log):
            try:
                with open(self.research_log, "r") as f:
                    self.log_data = json.load(f)
            except Exception:
                self.log_data = []

    def _save_log(self):
        with open(self.research_log, "w") as f:
            json.dump(self.log_data, f, indent=4)
        print(f"{GREEN}[+] Research database successfully synced to {self.research_log}{RESET}\n")

    def print_banner(self):
        print(f"""{BLUE}{BOLD}
============================================================
              M4STCLAW SENTINEL RESEARCH SUITE v5.4
============================================================
 [Mode: Autonomous Prober]  [Clearance: ALPHA-1]
============================================================{RESET}""")

    def menu(self):
        self.print_banner()
        print("Select operational module:")
        print(f" {BOLD}1.{RESET} Standard Browser & Script UA Prober")
        print(f" {BOLD}2.{RESET} GitHub Meta Token & CSRF Extractor")
        print(f" {BOLD}3.{RESET} API Rate-Limit Prober (Telemetry Scan)")
        print(f" {BOLD}4.{RESET} Execute Full Suite & Sync Database")
        print(f" {BOLD}5.{RESET} Exit Research Session\n")
        
        choice = input(f"{BOLD}Execute node (1-5) -> {RESET}").strip()
        return choice

    def run_ua_probe(self):
        print(f"\n{BLUE}[*] Triggering UA Fingerprinting Node...{RESET}")
        user_agents = {
            "Chrome Browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Minimalist / Python": "python-requests/2.28.1",
            "M4STCLAW Custom": "M4STCLAW-Researcher/5.0 (Autonomous Agent Grid)"
        }

        for name, ua in user_agents.items():
            print(f"Testing fingerprint: {BOLD}{name}{RESET}...")
            headers = {"User-Agent": ua, "Accept": "application/vnd.github.v3+json"}
            start = time.time()
            try:
                r = self.session.get("https://api.github.com/zen", headers=headers, timeout=8)
                latency = time.time() - start
                remaining = r.headers.get("X-RateLimit-Remaining", "N/A")
                is_flagged = r.status_code == 403 or "abuse" in r.text.lower()
                
                status_color = RED if is_flagged else GREEN
                print(f"  -> Status: {status_color}{r.status_code}{RESET} | Latency: {YELLOW}{latency:.2f}s{RESET} | RateLimit Remaining: {BLUE}{remaining}{RESET}")
                
                self.log_data.append({
                    "timestamp": datetime.now().isoformat(),
                    "module": "UA_PROBER",
                    "label": name,
                    "ua": ua,
                    "status_code": r.status_code,
                    "latency_sec": latency,
                    "remaining_limit": remaining,
                    "abuse_triggered": is_flagged
                })
            except Exception as e:
                print(f"  -> {RED}Network Connection Failure: {e}{RESET}")
        self._save_log()

    def extract_csrf_tokens(self):
        target_repo = "m4stanuj/LeadSniper"
        base_url = f"https://github.com/{target_repo}"
        print(f"\n{BLUE}[*] Loading target node: {BOLD}{target_repo}{RESET}...")
        
        try:
            r = self.session.get(base_url, timeout=10)
            token_match = re.search(r'<meta name="csrf-token" content="(.*?)"', r.text)
            version_match = re.search(r'"client-version":"(.*?)"', r.text)
            nonce_match = re.search(r'data-fetch-nonce="(.*?)"', r.text)

            auth_token = token_match.group(1) if token_match else None
            client_version = version_match.group(1) if version_match else "unknown"
            fetch_nonce = nonce_match.group(1) if nonce_match else None

            print(f"{GREEN}[+] Security payload extracted successfully:{RESET}")
            print(f"  - {BOLD}CSRF Authenticity Token:{RESET} {auth_token[:25]}..." if auth_token else f"  - {RED}CSRF Token: Not Found{RESET}")
            print(f"  - {BOLD}Client Build Version (SHA):{RESET} {client_version}")
            print(f"  - {BOLD}Session Fetch Nonce:{RESET} {fetch_nonce}" if fetch_nonce else f"  - {YELLOW}Fetch Nonce: Dynamic/None{RESET}")

            self.log_data.append({
                "timestamp": datetime.now().isoformat(),
                "module": "TOKEN_EXTRACTOR",
                "target": target_repo,
                "csrf_found": auth_token is not None,
                "client_version": client_version,
                "nonce_found": fetch_nonce is not None
            })
            self._save_log()
        except Exception as e:
            print(f"{RED}[!] Connection error extraction failed: {e}{RESET}\n")

    def rate_limit_probe(self):
        print(f"\n{BLUE}[*] Executing unauthenticated telemetry prober...{RESET}")
        endpoint = "https://api.github.com/zen"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/vnd.github.v3+json",
            "X-Research-Node": hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        }

        try:
            start = time.time()
            r = requests.get(endpoint, headers=headers, timeout=10)
            latency = time.time() - start
            
            rl_limit = r.headers.get("X-RateLimit-Limit")
            rl_remaining = r.headers.get("X-RateLimit-Remaining")
            rl_reset = r.headers.get("X-RateLimit-Reset")
            
            print(f"{GREEN}[+] Server response parsed:{RESET}")
            print(f"  - {BOLD}Rate-Limit Ceiling:{RESET} {rl_limit} requests/hour")
            print(f"  - {BOLD}Remaining Requests:{RESET} {rl_remaining}")
            if rl_reset:
                reset_time = datetime.fromtimestamp(int(rl_reset)).strftime('%Y-%m-%d %H:%M:%S')
                print(f"  - {BOLD}Rate-Limit Reset Window:{RESET} {reset_time}")

            self.log_data.append({
                "timestamp": datetime.now().isoformat(),
                "module": "LIMIT_PROBER",
                "rl_limit": rl_limit,
                "rl_remaining": rl_remaining,
                "rl_reset": rl_reset,
                "latency_sec": latency
            })
            self._save_log()
        except Exception as e:
            print(f"{RED}[!] Telemetry request failed: {e}{RESET}\n")

    def execute(self):
        while True:
            choice = self.menu()
            if choice == "1":
                self.run_ua_probe()
            elif choice == "2":
                self.extract_csrf_tokens()
            elif choice == "3":
                self.rate_limit_probe()
            elif choice == "4":
                print(f"\n{YELLOW}[*] Automating Full Research Sequence...{RESET}")
                self.run_ua_probe()
                self.extract_csrf_tokens()
                self.rate_limit_probe()
                print(f"{GREEN}[+] Full automation execution complete.{RESET}\n")
            elif choice == "5":
                print(f"\n{GREEN}[+] Session securely terminated. Keep building, brother. 👽🤙{RESET}")
                break
            else:
                print(f"\n{RED}[!] Invalid entry. Choose options 1 to 5.{RESET}\n")

if __name__ == "__main__":
    suite = SentinelSuite()
    suite.execute()
