from flask import Flask,render_template,request
import numpy as np
from error import give_pred

app = Flask(__name__)

@app.route("/")
@app.route("/Hello")
def home():
    return render_template("website1.html")

@app.route("/result",methods=['POST','GET'])
def result():
    outpt= request.form.to_dict()
    Current=outpt["current"]
    Volt=outpt['volt']
    Temp=outpt['temp']
    Humidity=outpt['humidity']
    Vibration=outpt['vibration']
    results=give_pred(Current,Volt,Temp,Humidity,Vibration)
    return render_template("website1.html",name=results)

if __name__=='__main__':
    app.run(debug=True,port=5000)
 