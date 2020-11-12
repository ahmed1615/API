import requests

url="https://reqres.in/api/users?page=2"
r=requests.delete(url)
m=requests.get(url)
print(m)
print(r.status_code)
assert r.status_code==204