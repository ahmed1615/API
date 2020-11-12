import requests
import json
import jsonpath

url="https://reqres.in/api/users?page=2"
r=requests.get(url)
print(r)
print(r.content)
print("---------")
r_j=json.loads(r.text)
print(r_j)
total=jsonpath.jsonpath(r_j,"total")
print(total)
print(total[0])
try:
    assert total[0]==11
except:
    print('no')
