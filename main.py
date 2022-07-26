from fastapi import FastAPI

from utils import (
    cost, 
    script_risk, 
    prediction_model, 
    performance_model
)

app = FastAPI()


@app.get('/api/exercise/one/performance/')
async def exercise_one_performance():
    return performance_model()


@app.get('/api/exercise/one/{index_img}/')
async def exercise_one(index_img: int):
    return prediction_model(index_img)


@app.get('/api/exercise/two/')
async def exercise_two():
    return script_risk()


@app.get('/api/exercise/three/')
async def exercise_three(
    n:int, 
    start_x:int, 
    start_y:int, 
    end_x:int, 
    end_y:int
):
    return await cost(n, start_x, start_y, end_x, end_y)