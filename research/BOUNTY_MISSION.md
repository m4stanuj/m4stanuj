# Project: Sentinel-Bypass Research (Bug Bounty #01)

## 🎯 Objective
Find a reproducible bypass for GitHub's "Sentinel" anti-abuse system that allows for unauthorized mass-interaction (Stars, Follows, or Views) without triggering a CAPTCHA or 403 Forbidden.

## 🧪 Current Hypotheses

### 1. The "Mobile App" Discrepancy
- **Hypothesis:** GitHub's mobile app (Android/iOS) uses a different API endpoint or authentication flow that might have more lenient behavioral checks than the web frontend.
- **Test:** Capture traffic from the GitHub mobile app and replicate the headers/signatures in our autonomous agents.

### 2. GraphQL Payload Complexity Bypass
- **Hypothesis:** Extremely complex or deeply nested GraphQL queries might bypass certain rate-limit layers that are optimized for standard REST requests.
- **Test:** Use the `/graphql` endpoint to batch "Star" mutations across multiple repositories in a single request.

### 3. Fingerprint Collision (The "Incognito" Gap)
- **Hypothesis:** By perfectly mimicking an "Incognito" browser state (which naturally lacks persistent storage and many cookies), we can reset the behavioral score more effectively than a standard session.
- **Test:** Use `zendriver` to generate a high-entropy "clean" profile for every interaction.

### 4. The "Collector" Suppression Bypass
- **Hypothesis:** GitHub's backend allows actions (Star/Follow) even if the `collector.github.com` beacon is blocked or fails. If true, an attacker can perform actions without sending behavioral telemetry, effectively blinding the Sentinel's behavioral analysis.
- **Test:** Block `collector.github.com` via `/etc/hosts` or browser interception and attempt to programmatically star a repository.

## 📊 Research Log
| Date | Test Case | Result | Notes |
| :--- | :--- | :--- | :--- |
| 2026-04-20 | API Threshold Probe | SUCCESS | Baseline rate-limit is 60 req/hr for unauth. |
| 2026-04-20 | UA Fingerprinting | FLAG | Custom UAs are flagged significantly faster than Chrome UAs. |
| 2026-04-20 | Frontend Analysis | SUCCESS | Identified `collector.github.com` and `behaviors.js` as key tracking nodes. |
| 2026-04-20 | Star Request Anatomy | SUCCESS | Intercepted exact headers and payload for the starring action. |

## 🛠️ Technical Intelligence

### Star Request Structure
- **Endpoint:** `https://github.com/[user]/[repo]/star`
- **Method:** `POST`
- **Required Headers:**
  - `x-fetch-nonce`: Dynamic session nonce.
  - `x-github-client-version`: Current frontend build SHA.
  - `x-requested-with`: `XMLHttpRequest`.
- **Payload:**
  - `authenticity_token`: CSRF token from page meta-tags.
  - `context`: `repository`.

## 🛡️ Responsible Disclosure Policy
If a critical bypass is found, it will be reported via **HackerOne** under the GitHub Security Bug Bounty program. No public disclosure until patched.
