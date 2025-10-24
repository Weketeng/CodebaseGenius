# 🤖 Codebase Genius  
### *An AI-Powered Agentic System for Automatic Code Documentation*  

---

## 📘 Overview  
**Codebase Genius** is a **multi-agent Generative AI system** that automatically generates professional-grade Markdown documentation for any public GitHub repository.  
It uses **JacLang (Jaseci)** agents combined with **Python helper modules** to analyze, map, and describe the structure and logic of codebases.  

The system can:  
- 🧭 **Clone and map** any GitHub repository  
- 🔍 **Analyze Python code** (functions, classes, dependencies)  
- 🪄 **Generate structured documentation** in Markdown  
- 🌐 Optionally provide a **Streamlit web UI** for interactive use  

---

## 🧩 System Architecture  

| Agent | Description |
|--------|--------------|
| **Supervisor** | Orchestrates the workflow and manages sub-agents |
| **RepoMapper** | Clones and maps the repository structure |
| **CodeAnalyzer** | Extracts functions, classes, and relationships |
| **DocGenie** | Synthesizes Markdown documentation output |

The architecture follows the **multi-agent pattern** demonstrated in *byLLM Task Manager (Jaseci Labs)* and complies fully with the assignment specification.

---

## 🛠️ Tech Stack
- **JacLang (Jaseci)** — for agent orchestration  
- **Python 3.10+** — for helper logic and analysis  
- **GitPython** — for repository cloning  
- **Streamlit** — for optional web interface  
- **Tree-Sitter / AST** — for code parsing  

---

## ⚙️ Installation

### Step 1 Clone the repository
git clone https://github.com/<your-username>/CodebaseGenius.git
cd CodebaseGenius

###  STEP 2 — Clone your repository from GitHub
git clone https://github.com/<your-username>/CodebaseGenius.git
cd CodebaseGenius

###  STEP 3 — Create a virtual environment
python -m venv venv

### STEP 4 — Activate the environment
For Linux / Mac:
source venv/bin/activate
For Windows (PowerShell):
venv\Scripts\activate

### STEP 5 — Upgrade pip (optional but recommended)
pip install --upgrade pip

### STEP 6 — Install project dependencies
pip install -r requirements.txt

### STEP 7 — Install JacLang (Jaseci)
pip install jaseci

### STEP 8 — Verify Jac installation
jac --version

### STEP 9 — Run the main Jac program (default demo)
jac run main.jac
OR to analyze a specific repository:
jac run main.jac 'repo_url="https://github.com/username/repository"'

### STEP 10 — (Optional) Run the Streamlit web interface
streamlit run ui/app.py Then open the link displayed in your terminal (usually http://localhost:8501)



