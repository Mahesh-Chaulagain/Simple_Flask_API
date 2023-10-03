from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

# To create API route we can mark them with different methods like:
# GET-> request data from a specified resourcce
# POST-> create a resource
# PUT-> update a resource
# DELETE-> delete a resource

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "ram sharma",
        "email": "ram@gmail.com"
    }
#Query parameter: an extra value that is included after the main path."?" symbol used to pass different query parameters
# like "get-user/123?extra=hello"

    extra = request.args.get("extra") #.args stores all query parameters in dictionary
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data),200 #200 is the default status code of success

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data),201

if __name__=="__main__":    #run flask application
    app.run(debug=True)