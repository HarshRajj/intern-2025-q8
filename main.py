
import os
import csv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.evaluation.prompts import PROMPT_A, PROMPT_B
from src.evaluation.runner import run_query
from src.evaluation.scoring import score_response

def load_queries(path="data/queries.csv"):
	with open(path, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		return [row['query'] for row in reader]

def save_results(results, path="data/results.csv"):
	import os
	os.makedirs(os.path.dirname(path), exist_ok=True)
	print(f"[INFO] Saving results to {path} ...")
	with open(path, "w", newline='', encoding='utf-8') as f:
		writer = csv.DictWriter(f, fieldnames=["query", "prompt_version", "score", "latency_ms"])
		writer.writeheader()
		writer.writerows(results)
	print(f"[INFO] Results saved to {path}.")

def main():
	load_dotenv()
	API_KEY = os.getenv("GOOGLE_API_KEY")
	if not API_KEY:
		raise RuntimeError("GOOGLE_API_KEY not found in .env file.")

	llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)
	queries = load_queries()
	results = []

	for prompt_version, prompt in [("A", PROMPT_A), ("B", PROMPT_B)]:
		for query in queries:
			response, latency_ms = run_query(llm, prompt, query)
			score = score_response(response, prompt_version)
			results.append({
				"query": query,
				"prompt_version": prompt_version,
				"score": score,
				"latency_ms": latency_ms
			})

	save_results(results)
	print("Evaluation complete. Results saved to data/results.csv.")

if __name__ == "__main__":
	main()
