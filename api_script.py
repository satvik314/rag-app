import requests
import json

# Make a GET request to the FastAPI documentation endpoint to retrieve the OpenAPI schema
response = requests.get("https://rag-app.fly.dev/openapi.json")
openapi_schema = response.json()


## Add a source document

# Define the JSON payload to send to the API, replace 'source' with your actual data
payload = json.dumps({
    "source": "https://www.theverge.com/2024/1/10/24026571/slack-catch-up-mobile-messaging-app"
})

# Define the headers for your request, including the Content-Type for JSON
headers = {
    'Content-Type': 'application/json'
}

# Make a POST request to the '/add' endpoint with your payload and headers
response = requests.post("https://rag-app.fly.dev/add", headers=headers, data=payload)

# Print the status code and response data for debugging
print(response.json())


## Query the document

payload = json.dumps({
   "question" : "What is the document about?"
})

# Make a POST request to the '/query' endpoint
response = requests.post("https://rag-app.fly.dev/query", headers=headers, data=payload)

print(response.json())
