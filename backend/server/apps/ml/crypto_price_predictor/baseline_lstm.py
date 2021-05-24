import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from joblib import load
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


class LSTMPredictor:
    """
    LSTM predictior class used a baseline LSTM model for crypto Bitcoin price prediction.
    usage : created object of LSTMPredictor class then call compute_prediction method and pass the list
    of ten day price  function as input .

    return predict price of btc in US dollers.

    """
    def __init__(self):
        self.model = load_model("/home/saktiman/PyDev/Django_ml_service/research/crypto_price_model")
        self.datascaler = load("/home/saktiman/PyDev/Django_ml_service/research/btc_crypto_data_scaler.joblib")
        self.num_samples = 1
        self.time_steps = 10
        self.num_features = 1

    def preprocessing(self, input_data):
        # i might need to get data from database and then preprocess it and the predict and re
        if len(input_data) == 10:
            raise Exception( "please enter proper input data of length 10")
        df = pd.DataFrame(input_data, columns=['data'])
        input_data1 = df[['data']].values
        preprocessed_input_data = self.datascaler.transform(input_data1.reshape(-1, 1))
        num_samples = 1
        time_steps = 10
        num_features = 1
        preprocessed_input_data1 = preprocessed_input_data.reshape(num_samples, time_steps, num_features)
        return preprocessed_input_data1

    def predict(self, preprocessed_input_data):
        """ Predict method predict using lstm model """
        return self.model.predict(preprocessed_input_data)

    def postprocessing(self, raw_prediction):
        predicted_price = self.datascaler.inverse_transform(raw_prediction)
        return predicted_price

    def compute_prediction(self, input_data):
        try :
            preprocessed_input_data = self.preprocessing(input_data)
            raw_prediction = self.predict(preprocessed_input_data)
            predicted_price = self.postprocessing(raw_prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}
        return predicted_price[0][0]


if __name__=='__main__':
    input_data = [46762.99, 46431.5, 43538.04, 42849.78, 36690.09, 40526.64, 37252.01, 37449.73, 34655.25, 34969.05]
    lstm_predictor = LSTMPredictor()
    predictor_price = lstm_predictor.compute_prediction(input_data)
    print("the crypto price will be : $", predictor_price)