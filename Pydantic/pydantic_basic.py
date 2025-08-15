# pydantic --> strict type & data validation

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)


patient_info={'name':'Bhagwati','age':20,'weight':45.0}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
