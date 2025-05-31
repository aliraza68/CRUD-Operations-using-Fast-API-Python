from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# creating a Patient Model (schema)
# properties of the Patient
class Patient(BaseModel):

    name: Annotated[str, Field(..., max_length = 50, title = "Name of the patient", description="")]
    email: Annotated[EmailStr, Field(..., title = "Patient valid email")]
    age: Annotated[int, Field(..., gt = 0, lt = 120, title = "Patient age should be less tahn 120")]
    weight: Annotated[float, Field(..., gt = 0.0, title = "Patient weight")]
    married: Annotated[bool, Field(default = False, title = "Patient martial status (True/False)")]
    
    allergies: Annotated[Optional[ List[str] ], Field(default = None)] # optional field
    contact_details: Annotated[Optional[ Dict[str, str] ], Field(default = None)] # Optional field
    

