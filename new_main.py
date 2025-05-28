from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
import json

from Models.create_patient_model import CreatePatient
from Models.update_patient_model import UpdatePatient
from helper_methods import load_data, save_data


# creating an app
app = FastAPI()

    
# Home (root) URL
@app.get("/")
def hello():
    return {"message": "Patient Management System."}


# About company informaiton
@app.get("/about")
def about():
    return {"message" : "A fully functional API to manage your patient records."}

# view all patients data
@app.get("/view")
def view_all_patient():
    try:
        # get all patients
        data = load_data()
        return data
    
    except Exception as ex:
        print(f"Exception occurred: {ex}")
    

# get a particular Patient
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "ID of a patient in DB", 
                                        example = "P001")):
    # load all patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    # raising exception with proper status code
    raise HTTPException(status_code = 404, detail = "Patient not found!")

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description = "Sort data based on the height, weight, and bmi"), order: str = Query("asc", description = "Sort in asc or desc order")):
    
    valid_fields = ["weight", "height", "bmi"]
    sort_options = ["asc", "desc"]

    # some validations
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f"Invalid field, select from {valid_fields}")
    
    if order not in sort_options:
        raise HTTPException(status_code = 400, detail = f"Invalid sort-type, select from {sort_options}")
    
    # get all patients data
    data = load_data()

    # sort data based on sort-option
    is_sort_desc = True if order == "desc" else False
    sorted_data = sorted( data.values(), key = lambda x: x.get(sort_by, 0), reverse = is_sort_desc )
    
    # return sorted data
    return sorted_data

# create a new patient and save it in JSON file
@app.post("/create")
def create_patient(patient: CreatePatient):

    # load the existing data
    data = load_data()

    # check incomming patient is already exist
    if patient.p_id in data:
        raise HTTPException(status_code = 400, detail = "Patient already exists in DB!")

    # add new patient with patient_id to database
    data[patient.p_id] = patient.model_dump(exclude = ["p_id"])

    # save into json file
    save_data(data)
    return JSONResponse(status_code = 200, content = {"message": "Patient created successfully!"})

# update an existing patient ddata
@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, update_patient: UpdatePatient):
    #load existing data
    data = load_data()

    # check pateint is already exist
    if patient_id not in data:
        raise HTTPException(status_code = 404, detail= "Patient data, you want to alter, is not found in DB!")
    
    # get existing patient infor
    existing_patient_info = data[patient_id]

    # pydantic -> dict (extract fields which has changed)
    updated_patient_info = update_patient.model_dump(exclude_unset = True)

    # update values in exisitng patient info
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # dict -> pydantic model
    existing_patient_info["p_id"] = patient_id
    patient_pydantic_obj = CreatePatient(**existing_patient_info)

    # pydantic model -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude = "p_id")

    # add dictionay to data
    data[patient_id] = existing_patient_info    

    # save data
    save_data(data)

    return JSONResponse(status_code = 200, content={"message": "Patient updated successfully!"})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str = Path(..., description = "ID of the patient", example = "P001")):
    # load all the data
    data = load_data()

    # check pateint is already exist
    if patient_id not in data:
        raise HTTPException(status_code = 404, detail= "Patient data, you want to delete, is not found in DB!")
    
    # delete the record
    del data[patient_id]

    # save data
    save_data(data)

    # return 
    return JSONResponse(status_code = 200, content = {"message": "Patient data is deleted successfully!"})
