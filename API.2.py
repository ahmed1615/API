import json
import requests
#url="http://localhost:7001/student"
#
#print(r)
#print(r.status_code)
#print(r.json())
#datos=(("ali",2),
#("hema",6),
#("jaka",5),
#("pollo",6)       )
#for n,c in datos:
#datos={"name":"panma"}
#r=requests.put("http://localhost:7001/student/3",json=datos)
#print(r.status_code)



#print("name",j["name"])
#print("coursos",j["courses"])


#for i in j ["students"]:
    #print("id",i["id"])
    #print("name",i["name"])
    #print("courses",i["courses"])

#url="http://localhost:8880/form"
#datos={"name":"ahmed",
      # "email":"ahmed@gmail.com",
      # "message":"i am here"}



#r=requests.post(url,data=datos)
#d=r.content.decode()
#if d.find("¡Mensaje enviado correctamente!")>-1:
  #  print("you massage is correct")
#else:
  #  print("a7a")
url="http://localhost:8880/form"
s=input("put your name: ")
d=input("put your date (dd/mm/yyyy): ")
c=input("put your name of the course: ")
datos={"student":s,
        "date":d,
        "course":c}
r=requests.post(url,data=datos)
cod=r.status_code

if cod==200:
    so=r.content.decode("utf-8")
    if so.find("¡Alumno inscripto correctamente!")>-1:
     print("yes u put all your date wait us to respond thank you")
    else:
        print ("plese complete your dates ")
else:
    print("el mawk3 msh mawgood")





