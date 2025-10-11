class Patient:

    def _init_(self, patient_id, name, age, disease):
        self.patient_id = patient_id 
        self.name = name
        self.age = age
        self.disease = disease
        self.assigned_doctor = None 

class Doctor:

    def _init_(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

class Hospital:

    def _init_(self):
        self.doctors = {}
        self.patients = {}

    def admit_patient(self, patient):
        self.patients[patient.patient_id] = patient
        print(f"Patient: {patient.name} admitted.")

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def assign_doctor(self, patient_id, doctor_id):
        if patient_id in self.patients and doctor_id in self.doctors:
            self.patients[patient_id].assigned_doctor = self.doctors[doctor_id]
            print(f"Doctor {self.doctors[doctor_id].name} assigned to patient {self.patients[patient_id].name}.")
        else:
            print("Invalid patient ID or doctor ID.")

    def discharge_patient(self, patient_id):
        if patient_id in self.patients:
            print(f"Patient {self.patients[patient_id].name} discharged.")
            del self.patients[patient_id]
        else:
            print("Patient ID not found.")

    def show_patients(self):
        if not self.patients:
            print("No patient available")
        for patient in self.patients.values():
                print(f"Patient ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}, Assigned Doctor: {patient.assigned_doctor.name}")

            

# Simulation
hospital = Hospital()

doctor1 = Doctor("M.B.Ch.B101", "Dr. Yeboah", "Cardiology")
doctor2 = Doctor("M.B.Ch.B102", "Dr. Joel", "Neurology")
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

patient1 = Patient(101, "Jane Nkrabia", 25, "Heart Disease")
patient2 = Patient(102, "John Nsia", 30, "Migraine")

hospital.admit_patient(patient1)
hospital.admit_patient(patient2)

hospital.assign_doctor(101, "M.B.Ch.B101")
hospital.assign_doctor(102,"M.B.Ch.B102")

hospital.show_patients()

hospital.discharge_patient(101)
( hospital.show_patients())