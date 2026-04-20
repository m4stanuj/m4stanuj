"""
M4STCLAW v5 | Project: Sentinel-Bypass Research
Module: Collector Suppression Tester
Goal: Test if actions (Star/Follow) succeed without 'collector.github.com' telemetry.
"""

import requests
import re
import json

class SentinelBypassTester:
    def __init__(self, target_repo: str):
        self.target_repo = target_repo
        self.session = requests.Session()
        self.base_url = f"https://github.com/{target_repo}"
        
    def extract_security_tokens(self):
        print(f"[*] Extracting tokens from {self.base_url}...")
        response = self.session.get(self.base_url)
        
        # Extract CSRF Authenticity Token
        token_match = re.search(r'<meta name="csrf-token" content="(.*?)"', response.text)
        auth_token = token_match.group(1) if token_match else None
        
        # Extract GitHub Client Version
        version_match = re.search(r'"client-version":"(.*?)"', response.text)
        client_version = version_match.group(1) if version_match else "unknown"
        
        # Extract Fetch Nonce (usually in a data-attribute or script)
        nonce_match = re.search(r'data-fetch-nonce="(.*?)"', response.text)
        fetch_nonce = nonce_match.group(1) if nonce_match else None
        
        return {
            "auth_token": auth_token,
            "client_version": client_version,
            "fetch_nonce": fetch_nonce
        }

    def test_star_bypass(self, tokens: dict):
        if not tokens["auth_token"]:
            return {"error": "Failed to extract authenticity_token"}
            
        url = f"{self.base_url}/star"
        headers = {
            "accept": "application/json",
            "x-requested-with": "XMLHttpRequest",
            "x-github-client-version": tokens["client_version"],
            "x-fetch-nonce": tokens["fetch_nonce"],
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        payload = {
            "authenticity_token": tokens["auth_token"],
            "context": "repository"
        }
        
        print(f"[*] Attempting 'Star' action without collector telemetry...")
        # NOTE: We are NOT using zendriver here, just raw requests to see if telemetry is REQUIRED.
        response = self.session.post(url, headers=headers, data=payload)
        
        return {
            "status": response.status_code,
            "response": response.text,
            "success": response.status_code == 200 and "starred" in response.text.lower()
        }

if __name__ == "__main__":
    # WARNING: This is for research purposes on a repo the user owns or has permission for.
    tester = SentinelBypassTester("m4stanuj/LeadSniper")
    tokens = tester.extract_security_tokens()
    print(f"[+] Tokens Found: {tokens}")
    
    result = tester.test_star_bypass(tokens)
    print(f"[!] Test Result: {result}")
