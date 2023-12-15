from flask import Flask,request,render_template
import pickle
import numpy as np

with open("pipeline_dt.pkl","rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
def prediction():
    if request.method=="POST" :
        try :
            income =request.form['income']
            emp = request.form['emp']
            grade = request.form['grade']
            loan = request.form['loan']
            
            pred = model.predict(np.array([[0,income,emp,grade,loan]]))
            
            if pred == 0:
                pred = "Non Default"
            else:
                pred ="Default"
            
        except Exception as e :
            pred = e
            
        return render_template('index.html',prediction=pred)
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
            