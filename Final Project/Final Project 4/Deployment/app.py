import numpy as np
import pickle

model = pickle.load(open('model/kmeans_model.pkl', 'rb'))

import flask

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in flask.request.form.values()]
    # print(float_features)
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    # print('------ prediction')
    # print(prediction)

    output = {0: 'Jumlah tertinggi adalah TENURE, untuk medium adalah PAYMENTS, dan nilai paling rendah adalah PURCHASES',
              1: 'Jumlah paling tinggi adalah PAYMENTS, untuk medium adalah TENURE, dan yang paling rendah adalah PURCHASES',
              2: 'Jumlah tertinggi PURCHASES dan PAYMENTS sedangkan terendah adalah TENURE'}

    return flask.render_template('main.html', prediction_text='{}'.format(output[prediction[0]]))