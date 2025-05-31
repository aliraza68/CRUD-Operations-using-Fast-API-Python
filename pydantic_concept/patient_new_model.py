from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


# creating a Patient Model (schema)
# properties of the Patient
class NewPatient(BaseModel):

    name: str
    email: str
    age: int
    weight: float
    married: bool
    allergies: Optional[ List[str] ] = None
    contact_details: Optional[ Dict[str, str] ] = None

    # custom data validation
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["gmail.com", "yahoo.com"]

        # Extract domain
        patient_email_domain = value.split("@")[-1]

        if patient_email_domain not in valid_domains:
            raise ValueError("Not a valid email.")
        
        return value
    
    @field_validator("age")
    @classmethod
    def age_validator(cls, value):
        if ( 0 < value < 100 ):
            return value
        
        else:
            raise ValueError("Age should be between 0 and 100")


    # custom transformation
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()


