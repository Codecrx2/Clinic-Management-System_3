import pandas as pd

# Function to add a patient to the CSV file
def add_patient(name, age, gender, address, phone):
    patients = pd.read_csv('patients.csv')
    patient_id = patients['id'].max() + 1
    new_patient = pd.DataFrame({'id': patient_id, 'name': name, 'age': age, 'gender': gender, 'address': address, 'phone': phone}, index=[0])
    patients = pd.concat([patients, new_patient], ignore_index=True)
    patients.to_csv('patients.csv', index=False)

# Function to schedule an appointment and save it to the CSV file
def schedule_appointment(patient_id, doctor, date, time):
    appointments = pd.read_csv('appointments.csv')
    appointment_id = appointments['id'].max() + 1
    new_appointment = pd.DataFrame({'id': appointment_id, 'patient_id': patient_id, 'doctor': doctor, 'date': date, 'time': time}, index=[0])
    appointments = pd.concat([appointments, new_appointment], ignore_index=True)
    appointments.to_csv('appointments.csv', index=False)

# Function to get patient information from the CSV file
def get_patient_info(patient_id):
    patients = pd.read_csv('patients.csv')
    patient = patients.loc[patients['id'] == patient_id]
    if patient.empty:
        return None
    return patient.to_dict('records')[0]

# Function to get appointments for a patient from the CSV file
def get_appointments(patient_id):
    appointments = pd.read_csv('appointments.csv')
    appointments = appointments.loc[appointments['patient_id'] == patient_id]
    if appointments.empty:
        return None
    return appointments.to_dict('records')
