"""
M4STCLAW v5: GitHub Bot Detection & Rate-Limit Researcher
Purpose: Systematic analysis of GitHub's behavioral fingerprinting for security reporting.
"""

import requests
import time
import json
import random
from typing import Dict, List

class GitHubBotResearcher:
    def __init__(self, target_url: str = "https://api.github.com"):
        self.target_url = target_url
        self.session = requests.Session()
        
    def test_fingerprint(self, user_agent: str, custom_headers: Dict = None) -> Dict:
        """Tests how GitHub responds to specific UA/Header combinations."""
        headers = {
            "User-Agent": user_agent,
            "Accept": "application/vnd.github.v3+json"
        }
        if custom_headers:
            headers.update(custom_headers)
            
        start_time = time.time()
        try:
            response = self.session.get(f"{self.target_url}/zen", headers=headers)
            latency = time.time() - start_time
            
            return {
                "ua": user_agent,
                "status": response.status_code,
                "latency": f"{latency:.2f}s",
                "rate_limit_remaining": response.headers.get("X-RateLimit-Remaining"),
                "is_flagged": response.status_code == 403 or "captcha" in response.text.lower()
            }
        except Exception as e:
            return {"error": str(e)}

    def run_stress_test(self, requests_per_second: float = 1.0, duration_sec: int = 10):
        """Measures the threshold for automated interaction triggers."""
        results = []
        start_test = time.time()
        
        while time.time() - start_test < duration_sec:
            res = self.test_fingerprint(
                user_agent=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110, 120)}.0.0.0 Safari/537.36"
            )
            results.append(res)
            time.sleep(1.0 / requests_per_second)
            
        return results

if __name__ == "__main__":
    researcher = GitHubBotResearcher()
    print("[*] Initiating Behavioral Fingerprinting Test...")
    
    # Test 1: Standard Browser UA
    print(f"Standard UA Test: {researcher.test_fingerprint('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')}")
    
    # Test 2: Scripting UA (Commonly flagged)
    print(f"Script UA Test: {researcher.test_fingerprint('python-requests/2.28.1')}")
    
    print("[!] Research data ready for Bug Bounty documentation.")
