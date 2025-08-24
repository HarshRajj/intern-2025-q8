from langchain.prompts import PromptTemplate

PROMPT_A = PromptTemplate(
    input_variables=["input"],
    template="You are a helpful assistant. Answer the following question as clearly as possible.\nQuestion: {input}\nAnswer:"
)

PROMPT_B = PromptTemplate(
    input_variables=["input"],
    template="You are a witty assistant. Respond to the user's question with a touch of humor, but keep it informative.\nUser: {input}\nResponse:"
)
