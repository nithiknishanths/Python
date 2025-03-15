from ollama import chat
from ollama import ChatResponse


userinput = input("Please type in your request to llama3.1 model here : ")

response: ChatResponse = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': 'Hi ! Be breif and let me know about the below , Also dont need to say keeping thinsg breif' + userinput,
  },
])

#print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)