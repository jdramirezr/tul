## Welcome

**For run the exercises:** 

**Running with docker-compose** 
```
docker-compose build	
docker-compose up
url => http://0.0.0.0:8000/docs
```


**Running with virtualenv** 
```
pip install virtualenv
virtualenv venv
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
url => http://0.0.0.0:8000/docs 
```


**Exercises** 

**1. Point**

```
Url: http://0.0.0.0:8000/api/exercise/one/{index_img}/
Description: index_img is index of image, returns the prediction the model for that  image

Point Optional
url: http://0.0.0.0:8000/api/exercise/one/performance/
Description: returns porcentage error model

```
**2. Point**

``` 
Url: http://0.0.0.0:8000/api/exercise/two/
Description: returns 'Buen trabajo' if everything is fine
```

**3. Point**

```
Url: http://0.0.0.0:8000/api/point/three/?n=5&start_x=4&start_y=0&end_x=0&end_y=0
Description: returns the number of moves(cost) and their coordinates between two points
Input:
  n = dimension array
  start_x = Coordinated x point start
  start_y = Coordinated y point start
  end_x = Coordinated x point end
  end_y = Coordinated y point end

Output:
  cost = Cost total (Moves)
  coordinates = coordinates for each move
```
