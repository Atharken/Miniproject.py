import requests
import time

while True:


  
 name = input("enter your pokemon name\n:")

  
 url = f"https://pokeapi.co/api/v2/pokemon/{name}"

  
 response = requests.get(url)

  
 data = response.json()


  
 print(f"name : {data["name"]}")
  
 print(f"height : {data["height"]}")
  
 print(f"base_experience : {data["base_experience"]}")
  
 print(f"wheight : {data["weight"]}")
  
 for i in data["types"]:
      
     print(f"type : {i["type"]["name"]}")

     time.sleep(1)import requests
import time

while True:


  
 name = input("enter your pokemon name\n:")

  
 url = f"https://pokeapi.co/api/v2/pokemon/{name}"

  
 response = requests.get(url)

  
 data = response.json()


  
 print(f"name : {data["name"]}")
  
 print(f"height : {data["height"]}")
  
 print(f"base_experience : {data["base_experience"]}")
  
 print(f"wheight : {data["weight"]}")
  
 for i in data["types"]:
      
     print(f"type : {i["type"]["name"]}")

     time.sleep(1)