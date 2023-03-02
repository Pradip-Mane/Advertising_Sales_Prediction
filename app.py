import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)     # starting point of our app

##Load the model
regmodel=pickle.load(open('reg_adv_model.pkl', 'rb')) #rb

@app.route('/')
def home():
    return render_template("home.html")       

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]               
    output=regmodel.predict(np.array(data).reshape(1,-1))                   
    return render_template("home.html", prediction_text="The Impact of advertisiment on Sales is {}".format(output)) 
                   
    
if __name__=="__main__":
    app.run(debug=True)