import requests
url = "https://api.openai.com/v1/chat/completions"
api_key = input("Please enter your API Key: ")

headers = {
    "Authorization": "Bearer {api_key}",
    "Content-Type": "application/json"
}

print("--- Welcome to My AI Assistant ---")
print("Type 'help' for info or 'exit' to leave.")


while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    if user_input.lower() == "help":
        print("Manual:")
        print("- Just type your question and press Enter.")
        print("- Type 'exit' to close the program.")
        continue

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            ai_answer = result["choices"][0]["message"]["content"]
            print(f"AI: {ai_answer}")
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
            
    except Exception as e:
        print(f"Connection Error: {e}")
