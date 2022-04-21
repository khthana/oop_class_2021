import requests
import json

act = {"id" : "3","Activity" : "Play football"}
r = requests.post("http://127.0.0.1:8000/todo",data=json.dumps(act))
print(r.json())

act = {"id" : "3","Activity" : "Play games"}
r = requests.put("http://127.0.0.1:8000/todo/3",data=json.dumps(act))
print(r.json())

r = requests.get("http://127.0.0.1:8000/todo")
print(r.json())

r = requests.delete("http://127.0.0.1:8000/todo/3")
print(r)
print(r.json())


