knowledge_base = {
    "hello": "Hello! I am your Mini ChatGPT.",
    "who are you": "I am a browser + backend AI assistant.",
    "what is ai": "AI stands for Artificial Intelligence."
}

def ask_llm(question):
    question = question.lower()
    for key in knowledge_base:
        if key in question:
            return knowledge_base[key]
    return "Sorry, I don't know the answer yet."
