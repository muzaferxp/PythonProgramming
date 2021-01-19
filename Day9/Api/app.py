from flask import *
import json


app = Flask(__name__)

#creating a route
@app.route("/")
def home():
    return "Welcome"

@app.route("/data")
def data():
    return "data"

Login = False
@app.route("/customer_data")
def cust_data():
    if Login:
        f = open("E:/Python programming/Code/Day9/Api/temp.json", "r")
        data = json.load(f)
        f.close()
        mysql_data = [("adam","20"),("sam", "22"),("David", "25")]
        res = json.dumps({"data" : mysql_data})
        return res  
    else:
        return "You are not authenticated!"


if __name__ == "__main__":
    app.run()