# Importing the FastApi class
from fastapi import FastAPI

# Creating an app object
app = FastAPI()

class ToDoList:
    ID = 1

    def __init__(self, name):
        self.__name = name
        self.__tasks = []

    def add_task(self, todo):
        id = ToDoList.ID
        todo["id"] = id
        self.__tasks.append(todo)
        ToDoList.ID += 1
        return id

    def get_task(self):
        return self.__tasks

    def modify_task(self, id, body):
        for todo in self.__tasks:
            if (int(todo["id"])) == id:
                todo["Activity"] = body["Activity"]
                return {
                    "data": f"Todo with id {id} has been updated"
                }
        return {
            "data": f"This Todo with id {id} is not found!"
        }

    def delete_task(self, id):
        for todo in self.__tasks:
            if int(todo["id"]) == id:
                self.__tasks.remove(todo)
                return {
                    "data": f"Todo with id {id} has been deleted!"
                }
        return {
            "data": f"Todo with id {id} was not found!"
        }

my_list = ToDoList("My")
# Default route

# A minimal app to demonstrate the get request
@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping": "Pong"}

# Post -- > Create Todo
@app.post("/todo", tags=["Todos"])
async def add_todo(task: dict) -> dict:
    id = my_list.add_task(task)
    todo = "A Todo "+str(id)+" is added!"
    return {
        "data": todo
    }

# GET -- > Read Todo
@app.get("/todo", tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": my_list.get_task()}

# PUT  -- > Update Todo
@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict) -> dict:
    return my_list.modify_task(id, body)

# DELETE --> Delete Todo
@app.delete("/todo/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    return my_list.delete_task(id)


