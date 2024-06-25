import requests
import json

API_Key = ""
prompts = '''These are my previous questions, for which you have already given answers.'''
stmt = "This is the question that you will answer now: "
print("Press ctrl x to exit")



while True:
  if(prompt=="\exit"):
      break
  prompt = input("Enter your prompt:  ")
  prompt2 = prompts + stmt + prompt
  prompts += prompt
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer {API_Key}",
      "X-Title": "Simple cli chatbot", # Optional. Shows in rankings on openrouter.ai.
    },
    data=json.dumps({
      "model": "mistralai/mistral-7b-instruct", # Optional
      "messages": [
        { "role": "user", "content": f"{prompt2}" }
      ]
    })
  )
  if response.status_code == 200:
        response_data = response.json()
        # Assuming the response structure mentioned in your message
        try:
            message_content = response_data['choices'][0]['message']['content']
            print(f"Response: {message_content}")
        except (KeyError, IndexError):
            print("Unexpected response format:", response_data)
  else:
    print("Failed to retrieve data:", response.status_code)
  
