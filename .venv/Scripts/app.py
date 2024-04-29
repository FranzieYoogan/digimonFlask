import json
from flask import Flask, render_template, request
import flask
import requests


app = Flask(__name__)


@app.route("/", methods = ['POST','GET'])
def index():
 if(flask.request.method == "POST"):
  inputValue = request.form['inputValue']
  if(inputValue):
   response = requests.get(f'https://digi-api.com/api/v1/digimon/{inputValue}')
   if(response):
    data = response.text
    parse_json = json.loads(data)
    dataName = parse_json['name']
    dataImages = parse_json['images'][0]['href']



   
 
    return render_template('index.htm',response = str(dataName), responseImg = str(dataImages))

   else:
    error = "error"
    
    return render_template('index.htm',error = error)
   
  else:
    error = "error"
    
    return render_template('index.htm',error = error)

 return render_template('index.htm'); 


if __name__ == '__main__':  
   app.run(debug=True)