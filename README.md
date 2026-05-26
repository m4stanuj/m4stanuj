# m4stanuj

<p align="center"><a href="https://github.com/m4stanuj"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00FF9D,100:3B82F6&height=230&section=header&text=M4ST&fontSize=90&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=Solo%20AI%20Systems%20Architect%20%7C%20Building%20the%20MAST%20Ecosystem&descAlignY=55&descSize=16&descColor=8B9BB4" alt="M4ST Header" /></a></p>

<p align="center"><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=00FF9D&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=120&lines=%24+whoami;Solo+AI+Systems+Architect+%7C+Bareilly%2C+India;%24+cat+mission.txt;Zero-cost+autonomous+agent+infrastructure+on+consumer+hardware;%24+uptime;21+MCP+servers+online+%7C+11+LLM+providers+active+%7C+%E2%82%B90%2Fmonth" alt="Typing SVG" /></a></p>

```
[ SYSTEM ONLINE ] -> MAST v1.0 Active.
"I build the infrastructure that makes AI tools actually work — agents, memory, routing, automation."
Hardware: RTX 2060 Super (8GB VRAM) · Operational Cost: ₹0/month
```

<p align="center"><a href="https://linkedin.com/in/m4stanuj"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a> <a href="https://m4stanuj.github.io"><img src="https://img.shields.io/badge/LIVE_PORTFOLIO-58A6FF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live Portfolio" /></a> <a href="mailto:m4stanuj@gmail.com"><img src="https://img.shields.io/badge/Encrypted_Comms-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a> <a href="https://fiverr.com/m4stanuj"><img src="https://img.shields.io/badge/Hire_on_Fiverr-1DBF73?style=for-the-badge&logo=fiverr&logoColor=white" alt="Fiverr" /></a> <a href="https://github.com/m4stanuj"><img src="https://komarev.com/ghpvc/?username=m4stanuj&style=for-the-badge&color=0D1117&label=PROFILE+VIEWS" alt="Profile Views" /></a></p>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## 🧠 `> cat /config/architect_profile.json`

```json
{
  "identity": {
    "alias": "M4ST",
    "class": "Solo AI Systems Architect",
    "location": "Bareilly, Uttar Pradesh, India",
    "hardware_specs": {
      "gpu": "NVIDIA GeForce RTX 2060 Super (8GB GDDR6 VRAM)",
      "cpu": "Intel Core i7-10700K (8C/16T @ 5.1GHz)",
      "ram": "32GB DDR4 Dual-Channel @ 3200MHz",
      "storage": "1TB NVMe PCIe Gen3 SSD (R: 3500MB/s)"
    },
    "status": "Building MAST — a self-hosted autonomous agent stack at ₹0/month."
  },
  "system_constraints": {
    "vram_allocation": "6.8GB hard limit (reserved for local Ollama, Whisper & Kokoro)",
    "concurrency_limit": 6,
    "sqlite_path": "var/lib/mast/history.db",
    "vector_store": "ChromaDB (Local persistent client)"
  },
  "mcp_gateways": {
    "active_servers": 21,
    "registered_tools": 91,
    "core_definitions": [
      "leadsniper_scraper",
      "shodan_osint",
      "nmap_portscan",
      "chroma_memory_rag",
      "sqlite_task_ledger",
      "kokoro_tts_daemon",
      "browser_playwright_operator",
      "groq_balancer"
    ]
  },
  "llm_balancing_mesh": {
    "provider_rotation_pool": 56,
    "fallback_chain": [
      "groq:llama-3.1-70b-versatile",
      "cerebras:llama-3.1-70b",
      "together:qwen-coder-32b",
      "openrouter:mistral-large",
      "ollama:deepseek-coder-6.7b-instruct (local)"
    ],
    "dynamic_routing_rules": {
      "latency_cap_ms": 600,
      "retry_with_exponential_backoff": true,
      "max_retries": 3,
      "rate_limit_auto_rotate": true
    }
  },
  "semantic_cache_parameters": {
    "backend": "chromadb",
    "distance_metric": "cosine",
    "similarity_threshold": 0.98,
    "indexing_dimensions": 384,
    "cached_latency_ms": 12
  },
  "leadsniper_icp_rules": {
    "target_roles": ["founder", "solo_operator", "tech_lead", "architect"],
    "scrapers_active": ["github_events", "linkedin_directories", "apollo_public"],
    "filter_out_low_intent": true,
    "draft_generation_constraints": {
      "max_length_words": 150,
      "tone": "direct_tech_oriented",
      "personalized_hook": "repo_activity_analysis"
    }
  },
  "secops_parameters": {
    "authorized_targets_only": true,
    "safety_filter_file": "config/authorized_targets.txt",
    "scanner_mesh": ["shodan", "nmap", "nuclei"],
    "fuzzing_rate_limit_req_sec": 5
  }
}
```

---

## 📡 `> tail -f /var/log/mast/system.log`

```log
[2026-05-26 08:14:02.109] [SYSTEM]  Initializing MAST v1.0 core stack on GPU 0 (NVIDIA RTX 2060 Super)...
[2026-05-26 08:14:02.390] [SYSTEM]  Loading 21 MCP server schemas from config/mcp_gateways/...
[2026-05-26 08:14:03.112] [SYSTEM]  91 tools successfully registered into agent namespace.               [ONLINE]
[2026-05-26 08:14:05.419] [ROUTER]  New execution request queued: "audit repository & extract config schemas"
[2026-05-26 08:14:05.422] [ROUTER]  Routing task → Developer Specialist Node (Chain 3: code_analysis)
[2026-05-26 08:14:05.811] [LLM-BAL] Requesting Groq [llama-3.1-70b-versatile]...
[2026-05-26 08:14:06.104] [LLM-BAL] API Error: 429 Too Many Requests (Rate limit reached)
[2026-05-26 08:14:06.106] [LLM-BAL] Rotating API Key pool → Index 14 → Switching provider to Cerebras...
[2026-05-26 08:14:06.321] [LLM-BAL] Cerebras response received in 215ms (112 tokens/sec)                 [SUCCESS]
[2026-05-26 08:22:19.004] [MEMORY]  Executing vector query on ChromaDB persistent client...
[2026-05-26 08:22:19.018] [MEMORY]  ChromaDB: Retrieved 3 context vectors matching indices [0x8f1e, 0x90ac, 0x90f2]
[2026-05-26 08:22:19.040] [MEMORY]  SQLite: Task log successfully committed to SQLite ledger at Index 1104
[2026-05-26 08:22:21.710] [PENTEST] Initiating security recon flow on scope...
[2026-05-26 08:22:21.712] [PENTEST] Checking domain against safety rules in config/authorized_targets.txt...
[2026-05-26 08:22:21.804] [PENTEST] Domain matched authorized list. Spawning Nmap (Flags: -sV -T4 -F)...   [VERIFIED]
[2026-05-26 08:22:25.409] [PENTEST] Port scanner output parsed: 2 open ports, service versions verified.
[2026-05-26 09:27:11.120] [CACHE]   Intercepting prompt request at RAG Gateway...
[2026-05-26 09:27:11.132] [CACHE]   Cosine similarity query hit: 0.985 confidence score.
[2026-05-26 09:27:11.144] [CACHE]   Retrieved prompt response from semantic cache index in 12ms.          [SAVED_TOKENS]
[2026-05-26 09:45:33.090] [SNIPER]  LeadSniper: Initiating Apollo directory scraping thread...
[2026-05-26 09:45:37.411] [SNIPER]  LeadSniper: 47 target profiles collected. Scoring against ICP schema...
[2026-05-26 09:45:38.220] [SNIPER]  LeadSniper: 12 candidates scored > 0.85 limit. Personalized email drafts queued.
[2026-05-26 10:02:17.810] [VOICE]   Synthesizing daily audio briefing...
[2026-05-26 10:02:18.020] [VOICE]   Kokoro-82M: Generated 180 speech tokens in 210ms (Real-Time Factor: 0.85 RTF) [SUCCESS]
```

---

## 📊 `> ./system_diagnostics.sh`

<p align="center"><img src="https://github-readme-stats.vercel.app/api?username=m4stanuj&show_icons=true&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=00FF9D&icon_color=3B82F6&text_color=8B9BB4&ring_color=00FF9D" height="180" alt="GitHub Stats"/> <img src="https://github-readme-streak-stats.herokuapp.com/?user=m4stanuj&theme=github-dark-blue&hide_border=true&background=0D1117&stroke=1F293D&ring=00FF9D&fire=00FF9D&currStreakLabel=00FF9D&sideLabels=8B9BB4&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=3B82F6" height="180" alt="Streak Stats"/></p>

<p align="center"><img src="https://github-readme-stats.vercel.app/api/top-langs/?username=m4stanuj&layout=compact&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=00FF9D&text_color=8B9BB4&langs_count=8" height="160" alt="Top Languages"/></p>

---

## ⚡ `> ls -la /deployed_projects/`

| Project | Description |
| :--- | :--- |
| **🏗️ MAST v1.0 — Unified AI Operator** | M4STCLAW + OpenWork + EIGENT merged into one autonomous stack. 21 MCP servers, 11 LLM providers, 11 task chains, 3-tier ChromaDB memory engine. Runs entirely on a single RTX 2060 Super at **₹0/month**.<br><br>`LangGraph` `ChromaDB` `Ollama` `MCP` `Local LLM` |
| **🛡️ cai-osint — OSINT + Pentest Framework** | AI-orchestrated autonomous recon framework integrating Shodan, Nmap, and Nuclei. CEH-aligned methodology with hardcoded authorized-target verification before any scan.<br><br>`OSINT` `Nmap` `Shodan` `Nuclei` `Security` |
| **🔌 OpenWork — Universal MCP Workspace** | 16 MCP servers that plug into any AI coding assistant — Cursor, VSCode, Windsurf, OpenCode. One JSON config powers every IDE. Universal workspace, zero lock-in.<br><br>`MCP Server` `IDE Integration` `JSON Config` |
| **⚡ Semantic Cache Engine** | ChromaDB vector similarity caching layer. Maps prompts to embeddings, retrieves cached responses at 0.98 similarity in under 12ms. Reduces redundant LLM API calls by **40-60%**.<br><br>`Semantic Cache` `Embeddings` `SQLite` `ChromaDB` |
| **🎯 LeadSniper — AI Outreach Engine** | Autonomous lead generation pipeline. Scrapes targets from open directories, scores based on custom ICP (Ideal Customer Profiles), and drafts hyper-personalized cold outreach — all on consumer hardware.<br><br>`Web Scraping` `LLM Routing` `Outreach` `Python` |
| **🚀 Antigravity Migration Pack** | Full IDE migration config: 21-provider LLM routing chain, 5 MCP servers, 91 tools. One-command setup to replicate the entire MAST development environment on any machine.<br><br>`Migration` `Config Export` `DevOps` `Toolchain` |

---

## 🛠️ `> ./inspect_tech_stack.sh`

### Core Languages & Frameworks
[![Languages](https://skillicons.dev/icons?i=py,ts,js,bash,linux,docker&perline=6)](https://skillicons.dev)

### AI / ML / Orchestration
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-2D2D2D?style=flat-square&logo=python&logoColor=00FF9D) ![CrewAI](https://img.shields.io/badge/CrewAI-FF6B6B?style=flat-square&logo=robot&logoColor=white) ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=llama&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FFD700?style=flat-square&logo=database&logoColor=black) ![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white) ![MCP Protocol](https://img.shields.io/badge/MCP_Protocol-00FF9D?style=flat-square&logo=protocol&logoColor=black) ![Whisper STT](https://img.shields.io/badge/Whisper_STT-74AA9C?style=flat-square&logo=openai&logoColor=white)

### Infrastructure & Tools
[![Infrastructure](https://skillicons.dev/icons?i=mongodb,postgres,redis,sqlite,nginx,vscode,git,github&perline=8)](https://skillicons.dev)

### Security & OSINT
![Nmap](https://img.shields.io/badge/Nmap-4682B4?style=flat-square&logo=nmap&logoColor=white) ![Shodan](https://img.shields.io/badge/Shodan-CC0000?style=flat-square&logo=shodan&logoColor=white) ![Nuclei](https://img.shields.io/badge/Nuclei-6C3483?style=flat-square&logo=security&logoColor=white) ![Playwright](https://img.shields.io/badge/Playwright-45BA4B?style=flat-square&logo=playwright&logoColor=white) ![CEH](https://img.shields.io/badge/CEH_Methodology-000000?style=flat-square&logo=hackthebox&logoColor=9FEF00)

---

## 🐍 `> render contribution_snake.svg`

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/m4stanuj/m4stanuj/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/m4stanuj/m4stanuj/output/github-contribution-grid-snake.svg" />
    <img alt="contribution snake animation" src="https://raw.githubusercontent.com/m4stanuj/m4stanuj/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

---

## 🏆 `> cat /build/highlights.txt`

<p align="center"><a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=m4stanuj&theme=algolia&column=6&no-frame=true&margin-w=15" alt="Trophies" /></a></p>

> **[ 🏗️ MAST ECOSYSTEM ARCHITECT ]**
> Built a unified autonomous agent system merging 3 major frameworks (M4STCLAW, OpenWork, EIGENT) into one installable stack. 21 MCP servers, 11 LLM providers, consumer hardware only.

> **[ 🛡️ OSINT & PENTEST AUTOMATION ]**
> Engineered an AI-orchestrated recon framework integrating Shodan, Nmap, and Nuclei. CEH-aligned workflow with hardcoded authorized-target verification before any scan.

> **[ ⚡ ZERO-COST INFRASTRUCTURE ]**
> Designed a free-tier LLM routing system across 11 providers with automatic fallback, semantic response caching (40-60% API cost reduction), and local model fallback — operational cost: ₹0/month.

> **[ 🎯 SOLO OPERATOR SCALE ]**
> Built LeadSniper to handle full B2B outreach autonomously — scraping, ICP scoring, and personalized drafting — all running locally on an RTX 2060 Super without any cloud dependency.



## 🛰️ `> execute contact_protocol.sh`

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   OPEN TO: Freelance AI Automation · AI Engineering Roles   │
│            Open Source Collaborations · MCP Contracts        │
│                                                             │
│   RESPONSE TIME: < 12 hours                                 │
│   PREFERRED: Direct message or email                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

<p align="center"><a href="https://m4stanuj.github.io"><img src="https://img.shields.io/badge/LIVE_PORTFOLIO-58A6FF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live Portfolio" /></a> <a href="mailto:m4stanuj@gmail.com"><img src="https://img.shields.io/badge/INITIATE_COMMS-00FF9D?style=for-the-badge&logo=minutemailer&logoColor=black" alt="Initiate Comms" /></a> <a href="https://linkedin.com/in/m4stanuj"><img src="https://img.shields.io/badge/CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Connect" /></a></p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00FF9D,100:3B82F6&height=100&section=footer" width="100%">
