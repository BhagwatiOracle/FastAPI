from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]


def update_patient_details(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)


patient_info={'name':'Bhagwati','age':20,'married':False,'weight':45.0,'allergies':['cold','cough','fever'],'contact_details':{'phone_number':'1235467','email':'xyz@gmail.com'}}

patient1 = Patient(**patient_info)

update_patient_details(patient1)