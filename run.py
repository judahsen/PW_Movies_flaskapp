from flask import Flask,request

app = Flask(__name__)


users = {
    1:{
        "id" : 1,
        "username" : "brandtC",
        "email" : "bc@movie.com"
    },
    2:{
        "id" : 2,
        "username" : "dylanS",
        "email" : "ds@movie.com"

    },
    3:{
        "id" : 3,
        "username" : "judahS",
        "email" : "js@movie.com"
    }
}

posts = {
    1 : {
        "author": 3,
        "director" : "Russo brothers",
        "title" : "Captain America-Winter Soldier",
        "release date":"April 4,2014",
        "personal view" : "Its the best superhero movie in recent times"
    },
    2 : {
        "author": 3,
        "director" : "James Wan",
        "title" : "The Conjuring",
        "release date":"July 19,2013",
        "personal view" : "I would say is one of the scariest movies I have seen "
    },
    3 : {
        "author": 3,
        "director" : "Gary Shore",
        "title" : "Dracula Untold",
        "release date":"Oct 10,2014",
        "personal view" : "A very underratted but one of my fav Dracula movie ",

    }
}


#Users Routes

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

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    users[data["id"]] = data
    return {
        "post request recieved":f"{data["username"]} has been created"
    }

@app.route("/user", methods=["PUT"])
def update_user():
    data = request.get_json()
    if data["id"] in users:
        users[data["id"]] = data
        return {
            "user updated" : users[data["id"]]
        }
    
@app.route("/user", methods=["DELETE"])
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