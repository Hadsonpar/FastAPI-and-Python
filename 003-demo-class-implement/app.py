from fastapi import FastAPI
from pydantic import BaseModel # import pydantic for use on body of web api
"""
The union() method returns a set that contains all items 
from the original set, and all items from the specified set(s).
"""
app = FastAPI()

@app.get('/')
def home():
    return {"message": "demo class implement"}

class Employe(BaseModel):    
    first_name: str
    last_name: str
    year_old: int
    web_page: str

data =  {    
        'first_name': 'Hadson',
        'last_name': 'Paredes Cordova',
        'year_old': 36,
        'web_page': 'http://hadsonpar.com'
        }

employe = Employe(**data)

@app.get("/items/{item_id}")
def item(item_id: int):    
    return {"item_id": item_id, "firts": employe.first_name, "lasts": employe.last_name, "year_old": employe.year_old, "web": employe.web_page}