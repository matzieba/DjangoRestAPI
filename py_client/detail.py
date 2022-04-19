
import requests


endpoint ="http://localhost:8000/api/products/3"


get_response = requests.get(endpoint, json = {"title":'kupa'})

print(get_response.json())
