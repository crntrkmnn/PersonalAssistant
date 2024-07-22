# appointments.py

import json
import os

APPOINTMENTS_FILE = 'appointments.json'

def load_appointments():
    if os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, 'w') as file:
        json.dump(appointments, file, indent=4)

def add_appointment(appointment_text):
    appointments = load_appointments()
    appointment_id = len(appointments) + 1
    appointments[appointment_id] = appointment_text
    save_appointments(appointments)
    print("Randevu eklendi!")

def list_appointments():
    appointments = load_appointments()
    if not appointments:
        print("Henüz randevu yok.")
    for appointment_id, appointment_text in appointments.items():
        print(f"{appointment_id}: {appointment_text}")
