import requests
import json 
from pprint import pprint
f=requests.get("http://join.navgurukul.org/api/partners")
s=json.loads(f.text)
l=[]
for i in s:
    for j in s[i]:
        l.append(j["id"])
    # print(l)
list1=[]
def assending():
    l.sort()
    # print(l)
    for j in range(len(l)):
        for k in range(len(s["data"])):
            if l[j]==s["data"][k]["id"]:
                b=s["data"][k]
                list1.append(b)
    with open("newfile.json","w") as f:
      json.dump(list1,f,indent=4)  
                
def dessending():
    l.sort(reverse = True)
    # print(l)
    for j in range(len(l)):
        for k in range(len(s["data"])):
            if l[j]==s["data"][k]["id"]:
                b=s["data"][k]
                list1.append(b)
    with open("newfile.json","w") as f:
       json.dump(list1,f,indent=4)


def user():
    print("assending[1] or dessending[2")        
    n=input("enter the choice:-")
    if n=="1":
        assending()
    elif n=="2":
        dessending()
    else:
        print("plz enter valid choise") 
        user()
user()        




