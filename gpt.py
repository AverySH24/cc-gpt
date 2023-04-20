import http.client
import json
import config

conn = http.client.HTTPSConnection(config.http_connection)

# query is what is google?


headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': config.api_key,
    'X-RapidAPI-Host': config.host
    }


# this should return a json object with the result and the conversationID
# print("Returned Message: \n")
# print(json_data["response"] + " -- This is the chatgpt response!\n")
# print(json_data["conversationId"] + " -- This is the conversation id!\n")

def make_query(query, conversation):
    payload = "{\r\n    \"query\": \"" + query + "\"\r\n}"
    conn.request("POST", "/ask", payload, headers)
    res = conn.getresponse()
    # data serves as a json object in this case
    data = res.read().decode("utf-8")
    json_data = json.loads(data)

def start_convo(name):
    payload = "{\r\n    \"query\": \"Respond to all my prompts as if you were " + name + ". Greet me as if you were the composer.\"\r\n}"

# {
#   "conversationId": "819e6c3e-e7cb-466c-83af-b0d137b93528",
#   "response": "Google is a multinational technology company specializing in Internet-related services and products, including online advertising technologies, search engine, cloud computing, software, and hardware."
# }