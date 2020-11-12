import requests
import json
url="http://localhost:8880/form"
r=requests.get(url)
#print(r)
#print(r.headers)

#print(r.status_code)
#print(r.text)
s=input("your name: ")
d=input("your date: ")
c=input("your course: ")
datos={
    "name":s,
    "data":d,
    "course":c
}
p=requests.post(url,data=datos)
z=p.content.decode("utf-8")
if p.status_code==200:
    if z.find("¡Alumno inscripto correctamente!")>-1:
        print("all under control")
    else:
        print("no yaba")
else:
    print("a7a")
















#j=r.json()
#datos={"courses":10}
#p=requests.put(url,json=datos)
#d=requests.delete(url)
'''print(r.content)
j=r.json()["student"]
print("name: ",j["name"])
print("courses: ",j["courses"])
for i in j["students"]:
    print("id: ",i["id"])
    print("name: ", i["name"])
    print("courses: ", i["courses"])
    print("------------")

p=requests.post(url,data=datos)
z=p.content.decode("utf-8")
print(z)
if z.find("¡Mensaje enviado correctamente!")>-1 :
    print("todo bien")
else:
    print("no yaba")



#print(r)
datos=(("hoda",3),
       ("juana",14),
       ("shady",8),
       ("pedro",2))
for i,b in datos:

    p=requests.post(url,json={"name":i,"courses":b})
    print(p.content)
    print(p.json())'''
