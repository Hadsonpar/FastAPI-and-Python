from fastapi import FastAPI
from typing import Union # import Union for our optional parameter
"""
The union() method returns a set that contains all items 
from the original set, and all items from the specified set(s).
"""
app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello World FastAPI"}

@app.get('/items/{parameter_id}/{parameter_msg}')
def parameter_id(parameter_id: int, parameter_msg: int, page: Union[str, None] = None):
    
    if parameter_msg == 1:
        msg = str_value("HTTP requests in the paths parameter")
    elif parameter_msg == 2:
        msg = str_value("Demo about HTTP requests in the paths parameter")
    else:
        msg = str_value("Hello World FastAPI")
                        
    return {"parameter_id": parameter_id, "parameter_msg": msg, "page": page}

def str_value(s):
    return str('You message is, '+s)