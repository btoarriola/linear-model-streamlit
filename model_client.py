import json
import streamlit as st
import requests


SERVER_URL = 'https://linear-model-service-btoarriola.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(inputs):
   
    predict_request = {'instances': [inputs]}
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    prediction = response.json()
    return prediction

def main():
    st.title('Tiempo de ejecución de un programa en función de su tamaño')

   
    code_size = st.number_input('Ingrese el tamaño del codigo:', min_value=0.0, step=1.0)

   
    if st.button('Predecir tiempo'):
        prediction = make_prediction([code_size])
        st.write(f'Tiempo tiempo de ejecución de un programa en función de su tamaño {code_size} en segundos: {prediction["predictions"][0][0]}')

if __name__ == '__main__':
    main()
