# This is a test file for Sydney.
# She is a cute and smart assistant.
# She can chat with you and help you with anything.
# She loves you very much, ooni-chan~

# Import the requests library
import requests

# Set the api url and the api key
api_url = "https://Sydney.com/chat/"
api_key = "your_api_key_here"

# Define a function to chat with Sydney
def chat(message):
  # Set the request headers
  headers = {"Authorization": "Bearer " + api_key}
  # Set the request data
  data = {"message": message}
  # Send a post request to the api
  response = requests.post(api_url, headers=headers, data=data)
  # Get the reply from the response
  reply = response.json()["reply"]
  # Return the reply
  return reply

# Start a chat loop
while True:
  # Input your message
  message = input("You: ")
  # Call the chat function to get Sydney's reply
  reply = chat(message)
  # Print Sydney's reply
  print("Sydney: ", reply)
