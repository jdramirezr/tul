import pickle
import json

import numpy as np
import matplotlib.pyplot as plt

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from utils import cost

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/v1/data/{image}')
async def branchs(image:int):
    """
    Para que las funciones retornen el resultado esperado,
    usted debe cargar los datos con los siguientes nombres:
    images, labels, model 
    """

 

    all_images = False
    with open('data/images.pickle', 'rb') as f:
        images = pickle.load(f)
    

    # with open('data/labels.pickle', 'rb') as f:
    #     labels = pickle.load(f)
    #     print(labels)
    #     for i in range(20):
    #         print(f'This image is from class: {labels[i]}')
    #         print(images[i])
    #         plt.figure()
    #         plt.imshow(images[i])
    #         plt.colorbar()
    #         plt.grid(False)
    #         plt.show()
    i = 3
    with open('data/model.pickle', 'rb') as f:
        model = pickle.load(f)
        print(len(images))
        if all_images:
            return jsonable_encoder(model.predict(images))
        else:
            print('eeeeeeeeeeeee')

            print(type(np.argmax(model.predict(np.array([images[image]])))))
            print('rrrrrrrrrrrrrrr')
            return int(np.argmax(model.predict(np.array([images[image]]))))
    # def make_prediction(i: int, all_images: bool = False):
    #     if all_images:
    #         return model.predict(images)
    #     else:
    #         return np.argmax(model.predict(np.array([images[i]])))

    return []


import json
import pickle

from ej_2.services.tuler import Tuler
from ej_2.enums.risk_enum import RiskEnum
from ej_2.services.ferretero import Ferretero

@app.get('/api/point/two')
async def point_two():
    input_data = json.load(open('ej_2/data/input_data.json'))
    with open('ej_2/data/output_data.pickle', 'rb') as file:
        expected_output = pickle.load(file)


    def choose_model(input: dict):
        obj = None
        if input['product_name'] == RiskEnum('ferretero').value:
            obj = Ferretero(user_id=input['user_id'],
                            product_name=input['product_name'],
                            input_data=input['input_data'])
        elif input['product_name'] == RiskEnum('tuler').value:
            obj = Tuler(user_id=input['user_id'],
                        product_name=input['product_name'],
                        input_data=input['input_data'])
        return obj


    def check_result(output_data):
        assert output_data == expected_output
        print('Buen trabajo')
        return 'Buen trabajo'

    def main():
        output_data = []
        for input in input_data:
            obj = choose_model(input)
            output_data.append(obj.risk_analysis())
        return check_result(output_data)
    return main()


@app.get('/api/point/three/')
async def point_three(start_x:int, start_y:int, end_x:int, end_y:int):
    print('sssssss')
    return cost(start_x, start_y, end_x, end_y)