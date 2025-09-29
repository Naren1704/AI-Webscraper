from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template=(
    "You are tasked to extract specific content from the following text content: {dom_content}."
    "Please follow these instructions:\n"
    "1. EXTRACT INFORMATION: Only extract the information that exactly matches the provided description: {user_descrip}."
    "2. NO EXTRA CONTENT: Do not include any additional text, comments or explanations in your response."
    "3. NO MATCH FOUND: If no information matches the description, return 'NO MATCH FOUND.'"
    "4. DIRECT DATA ONLY: Your output should only contain the data that is explicitly requested, with no other text"
)
model=OllamaLLM(model="llama3")

def parse(dom_chunks, user_descrip):
    promt=ChatPromptTemplate.from_template(template)
    chain=promt|model
    parsed_results=[]
    for i, chunk in enumerate(dom_chunks):
        result=chain.invoke({"dom_content": chunk, "user_descrip": user_descrip})
        parsed_results.append(result)
    return "\n".join(parsed_results)