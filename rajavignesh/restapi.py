from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def get():
    return "hello"

@app.route("/print",methods = ["POST"])
def print():
    payload = request.json
    name = payload["name"]
    age  = payload["age"]
    res ={
      "Status" : "success",
        "name" : name,
        
        "age"  : age
    }
    return jsonify(res),202

@app.route("/add/<int:a>/<int:b>",methods = ["GET"])
def add(a,b):
    return f"sum {a} + {b} is {a+b}"

@app.route("/users",methods =["GET"])
def p():
    name = request.args.get("name")
    msg = f"Hi {name}, Good Afternoon"
    print(name)
    res ={
        "status"  : "Success",
        "message" : msg
        
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port = 5000,debug=True)