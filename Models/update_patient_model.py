from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

class UpdatePatient(BaseModel):
    # model fields (attributes)
    name: Annotated[ Optional[str], Field(default = None, description = "Name of the patient") ]
    city: Annotated[ Optional[str], Field(default = None, description = "City where the patient is living") ]
    age: Annotated[ Optional[int], Field(default = None, gt = 0, lt = 120, description = "Age of the patient") ]
    gender: Annotated[ Optional[Literal["male", "female", "others"]], Field(default = None, description = "Gender of the patient") ]
    height: Annotated[ Optional[float], Field(default = None, gt = 0, description = "Height of the patient in meters")]
    weight: Annotated[ Optional[float], Field(default = None, gt = 0, description = "Weight of the patient in kgs")]
