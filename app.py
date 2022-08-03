from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

model=pickle.load(open('model.pkl','rb'))

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
def predict():
        
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)
    
    
    return render_template('index.html', prediction_text='Final report: {}'.format(prediction))




if __name__ == " __main__ ":
    app.run(debug=True)
    
