#!/usr/bin/python3
#Creado por DiegoAltF4

import requests
from bs4 import BeautifulSoup
r = requests.get("http://161.97.119.134:5000/m3g4k4bu_s3cre7")
soup = BeautifulSoup(r.text ,"lxml")
data = soup.find("p").get_text().split(" ")

print(data[10] + "----" + data[12])


res = int(data[10]) + int(data[12])

print(res)

post = requests.post("http://161.97.119.134:5000/m3g4k4bu_s3cre7" , data={"result":res})
print(post.text)
