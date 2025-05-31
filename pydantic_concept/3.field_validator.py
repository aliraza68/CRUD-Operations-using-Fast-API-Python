from patient_new_model import NewPatient


# insert patient data to database
def insert_patient_data(patient: NewPatient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient Age: {patient.age}")
    print(f"Is Patient married: {patient.married}")
    print(f"Patient martial status: {patient.married}")
    print(f"Patient allergies: {patient.allergies}")


    print("Data is inserted in database!")


# Main driver of the program
def main():
    patient_info = {
        "name": "Ali Raza",
        "email": "abc@gmail.com",
        "age" : -10,
        "weight": 70.5,
        "married" : True
    }

    # obj of patient
    p_obj = NewPatient(**patient_info)

    insert_patient_data(p_obj)

if __name__ == "__main__":
    main()