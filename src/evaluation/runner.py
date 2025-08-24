import time

def run_query(llm, prompt, query):
    formatted_prompt = prompt.format(input=query)
    start = time.perf_counter()
    try:
        response = llm.invoke(formatted_prompt)
        latency_ms = (time.perf_counter() - start) * 1000
        # Try to extract text from response
        if isinstance(response, str):
            response_text = response
        elif hasattr(response, 'content'):
            response_text = response.content
        elif hasattr(response, 'text'):
            response_text = response.text
        else:
            response_text = str(response)
    except Exception as e:
        response_text = str(e)
        latency_ms = -1
    return response_text, round(latency_ms, 1)
