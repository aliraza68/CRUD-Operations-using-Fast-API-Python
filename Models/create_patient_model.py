
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

# Model of Patient (all properties / fields of patient)
class CreatePatient(BaseModel):

    p_id: Annotated[str, Field(..., description = "ID of the patient", examples = ["P001"])]
    name: Annotated[str, Field(..., description = "Name of the patient")]
    city: Annotated[str, Field(..., description = "City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=120, description = "Age of the patient")]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description = "Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description = "Height of the patient in meters")]
    weight: Annotated[float, Field(..., gt=0, description = "Weight of the patient in kgs")]

    
    # computed fields using pydantic
    @computed_field
    @property
    def bmi(self) -> float:
        # rounded to 2 digits
        computed_bmi =  round( self.weight / (self.height ** 2), 2 )
        return computed_bmi  
    
    @computed_field
    @property
    def verdict(self) -> str:
        if (self.bmi < 18.5):
            return "Under-weight"

        elif (self.bmi < 25):
            return "Normal"
        
        elif (self.bmi < 30):
            return "Normal"
        
        else:
            return "Obese"
        


        
