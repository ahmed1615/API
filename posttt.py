import requests
import json
import jsonpath
url="https://reqres.in//api/users"

file=open("jee.json","r")
j=file.read()
r_j=json.loads(j)
print(r_j)

response=requests.post(url,r_j)
print(response.headers.get("content-length"))