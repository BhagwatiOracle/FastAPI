from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies:Optional[List[str]]=None

def update_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)


patient_info={'name':'Bhagwati','age':20,'married':False,'weight':45.0}

patient1 = Patient(**patient_info)

update_patient_details(patient1)