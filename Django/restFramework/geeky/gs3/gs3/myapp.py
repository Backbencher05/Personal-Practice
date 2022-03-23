import requests

URL = 'http://127.0.0.1:8000/stu/'

res = requests.get(URL)
print(res.json)