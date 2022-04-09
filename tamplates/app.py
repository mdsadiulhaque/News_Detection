
from flask import Flask,escape, request, render_template

vactor =pickle.load(open("vectorizer.pkl", 'rb'))

import pickle

model = pickle.load(open("finalized_model.pkl", 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        news = request.form['news']
        print(news)
        predict = model.predict(vactor.transform([news]))[0]
        print(predict)
        
        return render_template("prediction.html", prediction_text="News headline is-> {}".format(predict))
    else:
      return render_template("prediction.html")






