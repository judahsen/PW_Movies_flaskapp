#Users Routes
from flask import request
from app import app
from database import users

@app.route('/')
def landing_page():
    return {
        "Movies from these three GENRES" : "1:Superheros,2:Wild-West,3:Monsterverse,4:Supernatral,5:Paranormal,5:Romcom,6:Holidays"
    }

@app.get('/users')
def get_users():
    return {
        "users" : list(users.values())
    }

@app.get("/users/<int:id>")
def get_ind_user(id):
    if id in users:
        return {
            "user" : users[id]
        }
    return {
        "UH OH, something went wrong" : "invalid user id"
    }

@app.post("/user")
def create_user():
    data = request.get_json()
    print(data)
    users[data["id"]] = data
    return {
        "post request recieved":f"{data["username"]} has been created"
    }

@app.put("/user")
def update_user():
    data = request.get_json()
    if data["id"] in users:
        users[data["id"]] = data
        return {
            "user updated" : users[data["id"]]
        }
    
@app.delete("/user")
def delete_user():
    data = request.get_json()
    if data["id"] in users:
        del users[data["id"]]
        return {
            "user deleted" : f"{data["username"]} has been deleted"
        }
    return {
        "err" : "can't delete that user they aren't there"
    }