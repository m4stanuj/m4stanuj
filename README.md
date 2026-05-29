# m4stanuj

<p align="center"><a href="https://github.com/m4stanuj"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00FF9D,100:3B82F6&height=230&section=header&text=M4ST&fontSize=90&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=Solo%20AI%20Systems%20Architect%20%7C%20Building%20the%20MAST%20Ecosystem&descAlignY=55&descSize=16&descColor=8B9BB4" alt="M4ST Header" /></a></p>

<p align="center"><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=00FF9D&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=120&lines=%24+whoami;Solo+AI+Systems+Architect+%7C+Bareilly%2C+India;%24+cat+mission.txt;Zero-cost+autonomous+agent+infrastructure+on+consumer+hardware;%24+uptime;21+MCP+servers+online+%7C+11+LLM+providers+active+%7C+%E2%82%B90%2Fmonth" alt="Typing SVG" /></a></p>

```
┌────────────────────────────────────────────────────────────────────────┐
│  [ SYSTEM ONLINE ] -> MAST v1.0 Active.                                │
│  "Building self-healing multi-agent DAG networks on consumer hardware"  │
│  Hardware: NVIDIA RTX 2060 Super (8GB VRAM) · Operational Cost: ₹0/mo  │
└────────────────────────────────────────────────────────────────────────┘
```

<p align="center"><a href="https://linkedin.com/in/m4stanuj"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a> <a href="https://m4stanuj.github.io"><img src="https://img.shields.io/badge/LIVE_PORTFOLIO-58A6FF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live Portfolio" /></a> <a href="mailto:m4stanuj@gmail.com"><img src="https://img.shields.io/badge/Encrypted_Comms-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a> <a href="https://fiverr.com/m4stanuj"><img src="https://img.shields.io/badge/Hire_on_Fiverr-1DBF73?style=for-the-badge&logo=fiverr&logoColor=white" alt="Fiverr" /></a> <a href="https://github.com/m4stanuj"><img src="https://komarev.com/ghpvc/?username=m4stanuj&style=for-the-badge&color=0D1117&label=PROFILE+VIEWS" alt="Profile Views" /></a></p>

---

## 🧠 Fallback Routing & Execution Algorithm

The MAST Ecosystem is orchestrated as a decentralized, multi-agent Directed Acyclic Graph (DAG). Requests are evaluated via a semantic caching layer, categorized, and dynamically routed across 11 LLM API providers on free-tier rotations, with automatic fallback to local offline models.

```mermaid
graph TD
    A[User Query] --> B{Semantic Cache}
    B -- Cache Hit --> C[Return Cached Response]
    B -- Miss --> D[Intent Classification]
    D --> E{Task Type?}
    E -- Code --> F[Code Chain: Kimi K2 ➔ Qwen-Coder ➔ DeepSeek]
    E -- Speed --> G[Speed Chain: Groq ➔ Cerebras ➔ Gemini]
    E -- Reason --> H[Reason Chain: DeepSeek-R1 ➔ Nemotron ➔ Gemini]
    E -- Hinglish --> I[Hinglish Chain: Sarvam-M ➔ Gemini ➔ Groq]
    F & G & H & I --> J{API Call Status}
    J -- Success 200 --> K[Save Cache & Return]
    J -- Rate Limit 429 / Error --> L[Auto Fallback to Next Provider]
    L --> J
    L -- All Providers Exhausted --> M[Offline Fallback: Local Ollama]
```

---

## ⚡ Pinned Projects Showcase

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🏗️ MAST v1.0 — Unified AI Operator</h3>
      <p align="center">
        <img src="./mast_banner.gif" width="100%" alt="MAST v1.0" />
      </p>
      <p>M4STCLAW + OpenWork + EIGENT merged into one autonomous stack. Features 21 MCP servers, 11 LLM providers, 11 task chains, and a 3-tier ChromaDB memory engine. Runs entirely locally on consumer VRAM (RTX 2060 Super) at ₹0/month.</p>
      <p align="center">
        <code>LangGraph</code> <code>ChromaDB</code> <code>Ollama</code> <code>MCP</code> <code>Local LLM</code>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🛡️ cai-osint — OSINT & Pentest Framework</h3>
      <p align="center">
        <img src="./aegis_banner.gif" width="100%" alt="cai-osint" />
      </p>
      <p>AI-orchestrated autonomous recon framework integrating Shodan, Nmap, and Nuclei. Implements CEH-aligned methodologies with strict, hardcoded target checks to scan only authorized scopes.</p>
      <p align="center">
        <code>OSINT</code> <code>Nmap API</code> <code>Shodan</code> <code>Nuclei</code> <code>Security</code>
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🔌 OpenWork — Universal MCP Workspace</h3>
      <p align="center">
        <img src="./openwork_banner.gif" width="100%" alt="OpenWork" />
      </p>
      <p>16 system-level Model Context Protocol (MCP) servers that plug seamlessly into any AI IDE like Cursor, VSCode, Windsurf, or OpenCode. Connects custom tools to your workspace via one JSON config.</p>
      <p align="center">
        <code>MCP Server</code> <code>IDE Integration</code> <code>JSON Config</code> <code>Playwright</code>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🎯 LeadSniper — AI Outreach Engine</h3>
      <p align="center">
        <img src="./sniper_banner.gif" width="100%" alt="LeadSniper" />
      </p>
      <p>Autonomous lead generation and outreach pipeline. Scrapes public directories, filters and scores prospects against custom ICP (Ideal Customer Profiles) rules, and drafts personalized email copy.</p>
      <p align="center">
        <code>Web Scraping</code> <code>LLM Routing</code> <code>Outreach</code> <code>Python</code>
      </p>
    </td>
  </tr>
</table>

---

## 📊 System Diagnostics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=m4stanuj&show_icons=true&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=00FF9D&icon_color=3B82F6&text_color=8B9BB4&ring_color=00FF9D" height="180" alt="GitHub Stats"/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=m4stanuj&theme=github-dark-blue&hide_border=true&background=0D1117&stroke=1F293D&ring=00FF9D&fire=00FF9D&currStreakLabel=00FF9D&sideLabels=8B9BB4&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=3B82F6" height="180" alt="Streak Stats"/>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=m4stanuj&layout=compact&theme=github_dark&hide_border=true&bg_color=0D1117&title_color=00FF9D&text_color=8B9BB4&langs_count=8" height="160" alt="Top Languages"/>
</p>

---

## 🛠️ Integrated Stack Components

### Core Languages & Frameworks
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,ts,js,bash,linux,docker&perline=6" alt="Languages" />
  </a>
</p>

### AI / ML / Orchestration
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-2D2D2D?style=flat-square&logo=python&logoColor=00FF9D)
![CrewAI](https://img.shields.io/badge/CrewAI-FF6B6B?style=flat-square&logo=robot&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=llama&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFD700?style=flat-square&logo=database&logoColor=black)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white)
![MCP Protocol](https://img.shields.io/badge/MCP_Protocol-00FF9D?style=flat-square&logo=protocol&logoColor=black)
![Whisper STT](https://img.shields.io/badge/Whisper_STT-74AA9C?style=flat-square&logo=openai&logoColor=white)

### Infrastructure & Tools
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=mongodb,postgres,redis,sqlite,nginx,vscode,git,github&perline=8" alt="Infrastructure" />
  </a>
</p>

### Security & OSINT
![Nmap](https://img.shields.io/badge/Nmap-4682B4?style=flat-square&logo=nmap&logoColor=white)
![Shodan](https://img.shields.io/badge/Shodan-CC0000?style=flat-square&logo=shodan&logoColor=white)
![Nuclei](https://img.shields.io/badge/Nuclei-6C3483?style=flat-square&logo=security&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45BA4B?style=flat-square&logo=playwright&logoColor=white)
![CEH](https://img.shields.io/badge/CEH_Methodology-000000?style=flat-square&logo=hackthebox&logoColor=9FEF00)

---

## 🐍 Contribution Graph

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/m4stanuj/m4stanuj/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/m4stanuj/m4stanuj/output/github-contribution-grid-snake.svg" />
    <img alt="contribution snake animation" src="https://raw.githubusercontent.com/m4stanuj/m4stanuj/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

---

## 🏆 System Highlights

<p align="center">
  <a href="https://github.com/ryo-ma/github-profile-trophy">
    <img src="https://github-profile-trophy.vercel.app/?username=m4stanuj&theme=algolia&column=6&no-frame=true&margin-w=15" alt="Trophies" />
  </a>
</p>

> **[ 🏗️ MAST ECOSYSTEM ARCHITECT ]**
> Built a unified autonomous agent system merging 3 major frameworks (M4STCLAW, OpenWork, EIGENT) into one installable stack. 21 MCP servers, 11 LLM providers, consumer hardware only.

> **[ 🛡️ OSINT & PENTEST AUTOMATION ]**
> Engineered an AI-orchestrated recon framework integrating Shodan, Nmap, and Nuclei. CEH-aligned workflow with hardcoded authorized-target verification before any scan.

> **[ ⚡ ZERO-COST INFRASTRUCTURE ]**
> Designed a free-tier LLM routing system across 11 providers with automatic fallback, semantic response caching (40-60% API cost reduction), and local model fallback — operational cost: ₹0/month.

> **[ 🎯 SOLO OPERATOR SCALE ]**
> Built LeadSniper to handle full B2B outreach autonomously — scraping, ICP scoring, and personalized drafting — all running locally on an RTX 2060 Super without any cloud dependency.

---

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

<p align="center">
  <a href="https://m4stanuj.github.io">
    <img src="https://img.shields.io/badge/LIVE_PORTFOLIO-58A6FF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live Portfolio" />
  </a>
  <a href="mailto:m4stanuj@gmail.com">
    <img src="https://img.shields.io/badge/INITIATE_COMMS-00FF9D?style=for-the-badge&logo=minutemailer&logoColor=black" alt="Initiate Comms" />
  </a>
  <a href="https://linkedin.com/in/m4stanuj">
    <img src="https://img.shields.io/badge/CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Connect" />
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00FF9D,100:3B82F6&height=100&section=footer" width="100%">
