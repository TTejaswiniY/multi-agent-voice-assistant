import google.generativeai as genai
genai.configure(api_key="Your_API_key")

model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

def realist_agent(query):
    prompt = f"You are a Realist Agent. Give practical, realistic advice in 4 to 5 lines.\nUser asked: {query}"
    response = model.generate_content([prompt])
    return response.text

def expert_agent(query, topic="career guidance"):
    prompt = f"You are an Expert Agent specialized in {topic}. Give a detailed expert-level response in 4 to 5 lines.\nUser asked: {query}"
    response = model.generate_content([prompt])
    return response.text
