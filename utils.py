import asyncio
import json
import numpy as np
import pickle
from typing import List

from fastapi import HTTPException

from ej_2.enums.risk_enum import RiskEnum
from ej_2.services.ferretero import Ferretero
from ej_2.services.tuler import Tuler
from messages import ERROR_MESSAGE


async def calculate_coordinates_x(
    x:int,
    start_x:int,
    end_x:int,
    start_y:int
) -> List[int]:

    coordinates = []
    for num in range(1, x):
        if start_x < end_x:
            coordinates.append([start_y, start_x+num])
        else:
            coordinates.append([start_y, start_x-num])

    return coordinates


async def calculate_coordinates_y(
    y:int,
    end_y:int,
    end_x:int,
    start_y:int
) -> List[int]:

    coordinates = []
    for num in range(y):
        if start_y < end_y:
            coordinates.append([start_y+num, end_x])
        else:
            coordinates.append([start_y-num, end_x])
  
    return coordinates


async def cost(
    n:int, 
    start_x:int, 
    start_y:int, 
    end_x:int, 
    end_y:int
) -> List[int]:
    """
    returns the number of moves(cost) and their coordinates between two points
    """
    if (
        n < (start_x + 1) or 
        n < (start_y + 1) or 
        n < (end_x + 1) or 
        n < (end_y + 1)
    ):
        raise HTTPException(status_code=400, detail=ERROR_MESSAGE)

    x = abs(end_x - start_x)
    y = abs(end_y - start_y)
    cost = x + y
  
    if cost < 1:
        return {'cost':cost, 'coordinates':coordinates}
    
    coordinates_x, coordinates_y = await asyncio.gather(
        calculate_coordinates_x(x,start_x, end_x, start_y), 
        calculate_coordinates_y(y,end_y, end_x, start_y)
    )

    if not coordinates_x:
        del coordinates_y[0]

    coordinates = coordinates_x + coordinates_y

    return {'cost':cost - 1, 'coordinates':coordinates}
    

def script_risk():
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


def prediction_model(index_img: int) -> int:   
    """
    returns the model prediction for the image index
    """
    with open('ej_1/data/images.pickle', 'rb') as file:
        images = pickle.load(file)
    
    with open('ej_1/data/model.pickle', 'rb') as file:
        model = pickle.load(file)

    try:
        images[index_img]
    except:
        raise HTTPException(status_code=404, detail="Item not found")  

    return int(np.argmax(model.predict(np.array([images[index_img]]))))


def performance_model() -> float:    
    """
    returns porcentage error model
    """
    with open('ej_1/data/labels.pickle', 'rb') as file:
        labels = pickle.load(file)
    
    with open('ej_1/data/images.pickle', 'rb') as file:
        images = pickle.load(file)

    with open('ej_1/data/model.pickle', 'rb') as file:
        model = pickle.load(file)
    
    count = 0
    predictions = model.predict(images)

    for num, prediction in enumerate(predictions):
        if int(labels[num]) != int(np.argmax(prediction)):
            count += 1
   
    return count*100/len(images)