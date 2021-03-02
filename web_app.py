from flask import Flask , request , jsonify , render_template
import pickle
import pandas as pd
import math
import numpy as np
app = Flask(__name__)
data = pd.read_csv("cleaned_data.csv")
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():

     location = sorted(data['location'].unique())


     return render_template('index.html' , location = location)

@app.route('/predict', methods=['POST'])
def predict():
     if request.method == "POST":
          location = request.form.get("location")
          total_sqft = request.form.get("total_sqft")
          bath = request.form.get("bath")
          bhk =  request.form.get("bhk")
          print(location,total_sqft,bath,bhk)
          
     


          val = pd.DataFrame([[ location , total_sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])

          output = int(model.predict(val)[0])
          return render_template('index.html',prediction_text = output)














          

     
     


     
if __name__ == '__main__':
     app.run(port=5010)
