import requests


# endpoint = ("https://httpbin.org/")
endpoint = ("http://127.0.0.1:8000/")

get_response = requests.get(endpoint) 

print(get_response.json())