from flask import Flask, redirect, url_for, render_template, request,jsonify
import pickle
import pickle
import os
import glob
from tensorflow.keras.models import load_model
import json 


ls_pickles=glob.glob("FLASK APP/data_store/*")
path_nn = "FLASK APP/data_store/nn_model.h5"
ls_models=[]

for i in ls_pickles:
    if ".pkl" not in i:
        continue
    with open(i, 'rb') as f:
        ls_models.append(pickle.load(f))

# 0- complete data 21
# 1- scalar 
# 2 - important features

nn_model=load_model(path_nn)



app = Flask(__name__)

#@app.route("/")
#def home():
#    return render_template("base.html")

y_max = 3308.467553
@app.route("/fetch", methods=["POST"])
def main():

    data= request.get_json(force=True)
    print("data",data)
    for i in data:
        ls_models[0][i]=data[i]
    #ls_models[1].transform(ls_models[0].values.reshape(1,-1))
    scaled_x = ls_models[1].transform(ls_models[0].values.reshape(1,-1))
    ans=nn_model.predict(scaled_x)[0][0]*y_max
    
    return jsonify(json.dumps({"ans":ans}))


if __name__ == "__main__":
    print(os.getcwd())
    app.run(debug=True)