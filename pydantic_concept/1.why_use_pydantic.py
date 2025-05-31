# Why pydantic is basically used
# for type validation
#for data validation
# we perform data validation before inserting it in database

# save data to database
def insert_patient_data(name: str, age: int):
    print(f"Patient Name: {name}")
    print(f"Patient Age: {age}")

    print(f"Data-type of Name: {type(name)}")
    print(f"Data-type of age: {type(age)}")

    print("Data is inserted in database!")

# Another way of restricting the user to provide correct input
# custom type validation
# it is a correct way yo validate but it is not so much scalable and extenable
def insert_patient_data_custom(name: str, age: int):
    # some validation
    if( (type(name) == str) & (type(age) == int) ):

        if(age < 0):
            raise ValueError("Patient age can not be zero!")
        
        else:
            print(f"Patient Name: {name}")
            print(f"Patient Age: {age}")
            print("Data is inserted in database!")

    else:
        raise TypeError("Incorrect data-type")


# main driver of the program
def main():
    insert_patient_data_custom("Test Patient", -1)

if __name__ == "__main__":
    main()