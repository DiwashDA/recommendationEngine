from copyreg import pickle
from urllib import response
from flask import Flask,request,jsonify
from flask_cors import CORS
import Drug_Recommendation_Output
import pickle
import json

app = Flask(__name__)
# CORS(app) 
model = pickle.load(open('drug.pkl', 'rb'))

        
@app.route('/drug', methods=['POST'])
def recommend_drugs(): 
    medicine = request.form['med']
    res = Drug_Recommendation_Output.recommend(medicine)
    return {"data": res}
    


if __name__=='__main__':
    app.run(port=8888, debug=True)

