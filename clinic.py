import pandas as pd

class Clinic:
    def __init__(self):
        self.patients = pd.read_csv('patients.csv')
        self.appointments = pd.read_csv('appointments.csv')

    def add_patient(self, name, age, gender, address, phone):
        patient_id = self.patients['id'].max() + 1
        new_patient = pd.DataFrame({'id': patient_id, 'name': name, 'age': age, 'gender': gender, 'address': address, 'phone': phone}, index=[0])
        self.patients = pd.concat([self.patients, new_patient], ignore_index=True)
        self.patients.to_csv('patients.csv', index=False)

    def schedule_appointment(self, patient_id, doctor, date, time):
        appointment_id = self.appointments['id'].max() + 1
        new_appointment = pd.DataFrame({'id': appointment_id, 'patient_id': patient_id, 'doctor': doctor, 'date': date, 'time': time}, index=[0])
        self.appointments = pd.concat([self.appointments, new_appointment], ignore_index=True)
        self.appointments.to_csv('appointments.csv', index=False)

    def get_patient_info(self, patient_id):
        patient = self.patients.loc[self.patients['id'] == patient_id]
        if patient.empty:
            return None
        return patient.to_dict('records')[0]

    def get_appointments(self, patient_id):
        appointments = self.appointments.loc[self.appointments['patient_id'] == patient_id]
        if appointments.empty:
            return None
        return appointments.to_dict('records')
__init__()
add_patient()
schedule_appointment()
get_patient_info()
get_appointments()
