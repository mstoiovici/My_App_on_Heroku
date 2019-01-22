# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:55:55 2019

@author: maria
"""

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!!!!!"

@app.route("/Mariana")
def hello_someone():
    return "This will be Mariana's web app"

@app.route("/Mariana/<name>")     ##### how do I return the else statement in my html, cause if I don't give a name, I'll get a not found URL error
def hello_someone_else(name):
    return render_template("hello.html", name=name.title(), **locals())
######Get information from user

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print(form_data["email"])
    return "All OK"


if __name__=="__main__":
    app.run(debug=True)
