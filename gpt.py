import http.client
import json
import config

conn = http.client.HTTPSConnection(config.http_connection)

# query is what is google?
payload = "{\r\n    \"query\": \"What is google?\"\r\n}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': config.api_key,
    'X-RapidAPI-Host': config.host
    }

conn.request("POST", "/ask", payload, headers)

res = conn.getresponse()
# data serves as a json object in this case
data = res.read().decode("utf-8")
json_data = json.loads(data)

print("Returned Message: \n")
print(json_data["response"] + " -- This is the chatgpt response!\n")
print(json_data["conversationId"] + " -- This is the conversation id!\n")

print("Hi Avery! Did this work?")

# {
#   "conversationId": "819e6c3e-e7cb-466c-83af-b0d137b93528",
#   "response": "Google is a multinational technology company specializing in Internet-related services and products, including online advertising technologies, search engine, cloud computing, software, and hardware."
# }