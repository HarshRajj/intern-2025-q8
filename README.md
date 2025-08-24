# Offline LLM Prompt Evaluation

This project performs an offline evaluation of two different system prompts (A vs B) using a set of 20 diverse user queries and a freely-available LLM (e.g., Google Gemini, OpenAI, Claude, etc.).

## Features
- **Batch evaluation:** Runs all queries through both prompt versions.
- **Metrics:** Records query, prompt_version, score (1-5), and latency (ms) for each run.
- **Modular code:** All logic is in `src/evaluation/` for clarity and reuse.
- **Visualization:** Includes a notebook to plot mean score and latency for each prompt version.
- **.env support:** API keys are loaded from a `.env` file (never committed).

## Folder Structure
```
.
├── data/
│   ├── queries.csv         # 20 diverse user queries
│   └── results.csv         # Evaluation results (auto-generated)
├── notebooks/
│   └── plot_eval.ipynb     # Notebook for plotting results
├── src/
│   └── evaluation/
│       ├── prompts.py      # Prompt templates A & B
│       ├── runner.py       # LLM call and latency logic
│       └── scoring.py      # Scoring logic
├── main.py                 # Entry point: runs the evaluation
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup
1. **Clone the repo:**
   ```bash
   git clone <your-repo-url>
   cd intern-2025-q8
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your API key:**
   - Create a `.env` file in the root directory:
     ```
     GOOGLE_API_KEY=your_actual_gemini_api_key_here
     ```

## Usage
1. **Prepare queries:**
   - Edit `data/queries.csv` if you want to use your own queries.
2. **Run the evaluation:**
   ```bash
   python main.py
   ```
   - This will generate `data/results.csv` with all results.
3. **Visualize results:**
   - Open `notebooks/plot_eval.ipynb` in Jupyter or Colab to plot mean score and latency.

## Output Example
```
query,prompt_version,score,latency_ms
What is the capital of France?,A,5,1234.5
What is the capital of France?,B,4,1102.3
...
```

## Prompt Templates
- **Prompt A:** Helpful, clear assistant
- **Prompt B:** Witty, humorous but informative assistant

## Demo 
[Run on Google Colab](https://colab.research.google.com/drive/1u_xwRZ5v1f0pnlVcMp08RhIUwmGuB9mi?usp=sharing)

## Notes
- You can use any LangChain-compatible LLM (Gemini, OpenAI, Claude, etc.)
- No API keys or credentials are ever committed (see `.gitignore`)
- The code is modular and easy to extend for more prompts or metrics

## License
MIT
