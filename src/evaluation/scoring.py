import random

def score_response(response, prompt_version):
    # For demo: assign a random score (replace with real eval if needed)
    if response and isinstance(response, str) and response.strip():
        return random.randint(3, 5)
    return 1
