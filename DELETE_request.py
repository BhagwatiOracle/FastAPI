from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str,Field(...,description='ID of the patient', examples=['P001'])]
    name: Annotated[str,Field(...,description='Name of the patient')]
    city: Annotated[str, Field(...,description='City where the patient is living')]
    age: Annotated[str,Field(...,description='Age of the patient')]
    gender: Annotated[Literal['male','female','others'], Field(...,description='Gender of the patient')]
    height: Annotated[float, Field(...,gt=0,description='Height of the patient in mtrs')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the patient in kgs')]

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient deleted'})


