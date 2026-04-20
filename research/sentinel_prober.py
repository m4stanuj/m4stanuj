"""
M4STCLAW v5 | Project: Sentinel-Bypass Research
Module: API Threshold Prober
Goal: Mapping unauthenticated rate-limit windows and detection triggers.
"""

import requests
import json
import time
import hashlib
from datetime import datetime

class SentinelAPIProber:
    def __init__(self):
        self.endpoint = "https://api.github.com/zen"
        self.log_file = "sentinel_research_log.json"
        self.research_data = []

    def probe_with_fingerprint(self, user_agent: str, proxy: str = None) -> dict:
        headers = {
            "User-Agent": user_agent,
            "Accept": "application/vnd.github.v3+json",
            "X-Research-Node": hashlib.md5(user_agent.encode()).hexdigest()[:8]
        }
        
        proxies = {"http": proxy, "https": proxy} if proxy else None
        
        try:
            start_time = time.time()
            response = requests.get(self.endpoint, headers=headers, proxies=proxies, timeout=10)
            latency = time.time() - start_time
            
            result = {
                "timestamp": datetime.now().isoformat(),
                "ua_fingerprint": user_agent,
                "status": response.status_code,
                "latency": latency,
                "rl_limit": response.headers.get("X-RateLimit-Limit"),
                "rl_remaining": response.headers.get("X-RateLimit-Remaining"),
                "rl_reset": response.headers.get("X-RateLimit-Reset"),
                "server": response.headers.get("Server"),
                "detection_flag": "403" in str(response.status_code) or "abuse" in response.text.lower()
            }
            
            self.research_data.append(result)
            return result
        except Exception as e:
            return {"error": str(e)}

    def save_log(self):
        with open(self.log_file, "w") as f:
            json.dump(self.research_data, f, indent=4)

if __name__ == "__main__":
    prober = SentinelAPIProber()
    print("[*] Sentinel Probing Initiated...")
    
    # Sequence 1: Standard Chrome Fingerprint
    print(f"[*] Probe 1 (Chrome): {prober.probe_with_fingerprint('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')}")
    
    # Sequence 2: Minimalist UA (High Detection Risk)
    print(f"[*] Probe 2 (Minimal): {prober.probe_with_fingerprint('M4STCLAW-Researcher/5.0')}")
    
    prober.save_log()
    print("[+] Research log saved to sentinel_research_log.json")
