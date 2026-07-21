# GLADos-v1
GLaDOS-v1 isn't just an assistant it's a customized orchestration daemon designed to integrate a local Large Language Model (llama3) directly into your host system architecture. This is zero-cloud, dark-fiber AI.

By bridging the gap between conversational logic and native system execution, GLaDOS-v1 allows the model to analyze context, route intents, access persistent memory banks, and utilize specialized "chrome"—a registry of local function calls (File I/O, application launching, mathematical execution)—to execute complex operations autonomously.

This system was built on-grid as a personal deep-dive into local LLM orchestration and agentic architecture.

⚡ CORE CYBERWARE MODS
🏠 100% Offline Ops (Dark Net): Executes fully on your local machine via Ollama (localhost:11434). Zero corporate cloud dependency. Your data stays on your chrome, off the grid.

🛠️ Dynamic "Chrome" (Tool-Calling Registry): Implements a JSON-based function execution loop. When the daemon detects a required system action, it halts the chat loop and executes native Python tools (file management, app launching, sys-calc) before resuming inference.

🧠 Intent-Routing Core (brain.py): Uses a heuristic intent processor to classify user inputs (Data Storage, Recall, Knowledge Retrieval, Casual Chat) on the fly, dynamically tuning the system prompt to maximize processing efficiency.

💾 Persistent Data Banks (Dual-Layer Memory):

Short-Term Memory Buffer: Rolling conversation window maintained in active RAM context.

Long-Term User Profile: Automatic profile extraction daemon that uses the LLM to analyze conversation history, distill critical facts, and consolidate long-term user context with automated backup protocols (user_backup.txt).

🎭 Multi-Personality Matrix: Dyanmic persona switching on initialization, supporting protocols like GLaDOS (Dry/Sarcastic), Shakespeare (Poetic/Elevated), Wacky Punk (Chaotic/Rebellious), Mentor (Curious/Upbeat), or Custom User-Injected Prompts.

🏗️ SYSTEM ARCHITECTURE & FILE DIRECTORY
Plaintext
├── GLAdos.py              # Main Execution Daemon & Request Orchestrator
├── brain.py               # Heuristic Intent Processor & Prompt Constructor
├── personality.py         # Multi-Persona Prompt Matrix
├── user_data.py           # Long-Term Profile Compiler & Specialized Math Chrome
├── memory.py              # Short-Term RAM Buffer Handlers
├── tools/
│   ├── system_tools.py    # Native OS/Subprocess Integrity Mod
│   └── tools_registry.py  # Central Mapping Table for Function Calls
└── user.txt               # Persistent Long-Term Memory Store
🚀 FUNCTIONAL BREAKDOWN
Signal Intake: User input is received.

Intent Analysis: brain.py classifies the query's objective.

Context Compilation: System assembles the active prompt, injecting long-term profile data, RAM buffer history, and active Chrome descriptions.

Daemon Inference: Dispatch request to the local Ollama daemon (llama3).

Tool Execution (The Breach): If the daemon detects a required tool, it responds with a JSON payload. GLaDOS-v1 executes the native Python tool, pipes the result back to the model, and requests a final synthesized response.

Data Commit: RAM buffer logs the exchange. If long-term facts were detected, the profile update daemon consolidates the persistent data bank.

🛠️ INSTALLATION & JACK-IN PROCEDURES
Prerequisites: Python 3.10+, and an active Ollama instance.

Pull the Core Model:

Bash
ollama pull llama3
ollama serve
Install Dependencies:

Bash
pip install requests
Initialize the Daemon:

Bash
python GLAdos.py
🎯 ROADMAP: UPCOMING CYBERWARE UPGRADES
[ ] Semantic-based intent classification via embeddings.

[ ] Full Vector DB (ChromaDB) integration for scalable RAG capabilities.

[ ] Sandboxed tool execution protocols.

[ ] Multi-turn autonomous tool chaining.

(dont mind me larping into cyberpunk tho)
