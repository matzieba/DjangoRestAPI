import requests

#endpoint = "http://httpbin.org/anything"
#endpoint = "http://httpbin.org/status/200/"
endpoint ="http://localhost:8000/api/"


get_response = requests.post(endpoint, json = {"title":'kupa'})
#print(get_response.text)
#print(get_response.headers)
print(get_response.json())
