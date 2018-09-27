from flask import Flask
from flask import request,jsonify
import json
from app import App

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to do list App"

@app.route("/tasks")
def tasks():
    return jsonify(tasks)

@app.route("/Account",methods=["POST"])
def Account_Add():
    ap = App()

    req_data =json.loads(request.data)

    name = req_data["username"]
    password = req_data["password"]

    return jsonify(ap.Add_Account(name,password))


@app.route("/login",methods=["POST"])
def Account_Login():
    ap = App()

    req_data =json.loads(request.data)

    name = req_data["username"]
    password = req_data["password"]

    return jsonify(ap.Account_login(name,password))
    


@app.route("/task",methods=["GET","POST"])
def task():
    if request.method == "GET":
        ap = App()

        return jsonify(ap.Tsks())

    if request.method == "POST":
        ap = App()
        req_data = json.loads(request.data)

        task_data = req_data["task"]
        
        return jsonify(ap.Create_task(task_data))

@app.route("/task/markfinished",methods=["PUT"])
def Mark_as_Finished():
    ap = App()
    req_data = json.loads(request.data)

    task_data = req_data["task"]
    task_finish = req_data["finish"]

    return jsonify(ap.Mark_as_finished(task_data,task_finish))

@app.route("/task/delete",methods=["DELETE"])
def Delete_Task(): 
    ap = App()
    req_data = json.loads(request.data)

    task_data = req_data["task"]

    return jsonify(ap.Delete_task(task_data))

@app.route("/task/deleteall",methods=["DELETE"])
def Delete_all_Task():
    ap = App()    

    return jsonify(ap.Delete_all_tasks())

if __name__== "__main__":

      
    app.run()
   