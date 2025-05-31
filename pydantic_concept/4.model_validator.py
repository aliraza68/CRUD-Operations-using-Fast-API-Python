from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import List, Dict, Optional


# Patient Model
class Patient(BaseModel):

    name: str
    email: str
    age: int
    weight: float
    married: bool
    allergies: List[str] = None
    contact_details: Dict[str, str] = None

    # model validation
    @model_validator(mode = "after")
    def validae_emergency_contact(cls, model):
        if ( (model.age >60) & ("emergency" not in model.contact_details) ):
            raise ValueError("Age greater than 60, nust have emergency contact no in contact details.")

        else:
            return model







def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print("Age", patient.age)
    print("Weight: ", patient.weight)
    print("Married: ", patient.married)
    print("Allergies: ", patient.allergies)
    print("Contact details: ", patient.contact_details)


    print("Data is inserted in database!")


# Main driver of the program
def main():
    patient_info = {
        "name": "Ali Raza",
        "email": "abc@gmail.com",
        "age": 90,
        "weight": 70.4,
        "married":True,
        "allergies": ["1", "2"],
        "contact_details":  {"contact": "122",   "emergency":"1234"}
    }

    # obj of patient
    p_obj = Patient(**patient_info)

    insert_patient_data(p_obj)

if __name__ == "__main__":
    main()