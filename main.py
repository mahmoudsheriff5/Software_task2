class Appointment:
    def __init__(self, appointmentId: int, date: str, time: str):
        self.appointmentId = appointmentId
        self.date = date
        self.time = time
        self.status = "Pending" 

    def updateStatus(self, newStatus: str):
        self.status = newStatus


class Doctor:
    def __init__(self, doctorId: int, name: str, availableSlots: list):
        self.doctorId = doctorId
        self.name = name
        self.availableSlots = availableSlots

    def acceptAppointment(self, appt: Appointment):
        appt.updateStatus("Accepted")
        return "Accepted"

    def declineAppointment(self, appt: Appointment):
        appt.updateStatus("Declined")
        return "Declined"
        
    def reviewAppointment(self, appt: Appointment, will_accept: bool):
        if will_accept:
            return self.acceptAppointment(appt)
        else:
            return self.declineAppointment(appt)


class Patient:
    def __init__(self, patientId: int, name: str):
        self.patientId = patientId
        self.name = name
        self.upcomingAppointmentsCount = 0

    def viewAvailability(self, doctor: Doctor):
        print(f"Doctor {doctor.name}'s available slots: {doctor.availableSlots}")
        return doctor.availableSlots

    def bookAppointment(self, system, doctor: Doctor, date: str, time: str, doctor_will_accept: bool = True):
        print(f"\n--- {self.name} is attempting to book an appointment on {date} at {time} ---")
        system.processBookingRequest(self, doctor, date, time, doctor_will_accept)


class ClinicSystem:
    def __init__(self, max_appointments: int):
        self.MAX_APPOINTMENTS = max_appointments
        self.appointment_counter = 1

    def checkAppointmentLimit(self, patient: Patient) -> bool:
        return patient.upcomingAppointmentsCount < self.MAX_APPOINTMENTS

    def notifyStatus(self, patient: Patient, appt: Appointment):
        print(f"Notification to {patient.name}: Your appointment on {appt.date} at {appt.time} has been {appt.status}.")

    def processBookingRequest(self, patient: Patient, doctor: Doctor, date: str, time: str, doctor_will_accept: bool):
        if not self.checkAppointmentLimit(patient):
            print("Error: Maximum appointment limit reached")
            return

        appt = Appointment(self.appointment_counter, date, time)
        self.appointment_counter += 1
        
        review_result = doctor.reviewAppointment(appt, doctor_will_accept)
        
        if review_result == "Accepted":
            patient.upcomingAppointmentsCount += 1
            self.notifyStatus(patient, appt)
        else:
            self.notifyStatus(patient, appt)


if __name__ == "__main__":
    clinic = ClinicSystem(max_appointments=4)

    dr_abdullah = Doctor(doctorId=1, name="abdullah raafat", availableSlots=["2023-11-10 10:00", "2023-11-11 14:00"])
    dr_mahmoud = Doctor(doctorId=2, name="mahmoud sherief", availableSlots=["2023-11-12 09:00", "2023-11-13 11:00"])
    
    patient_hana = Patient(patientId=101, name="hana maged")
    patient_youssef = Patient(patientId=102, name="youssef ramy")

    patient_hana.viewAvailability(dr_abdullah)

    patient_hana.bookAppointment(clinic, dr_abdullah, "2023-11-10", "10:00", doctor_will_accept=True)
    patient_hana.bookAppointment(clinic, dr_abdullah, "2023-11-11", "14:00", doctor_will_accept=True)
    patient_hana.bookAppointment(clinic, dr_mahmoud, "2023-11-12", "09:00", doctor_will_accept=True)
    patient_hana.bookAppointment(clinic, dr_mahmoud, "2023-11-13", "11:00", doctor_will_accept=True)

    patient_hana.bookAppointment(clinic, dr_abdullah, "2023-11-14", "12:00", doctor_will_accept=True)

    patient_youssef.bookAppointment(clinic, dr_mahmoud, "2023-11-15", "15:00", doctor_will_accept=False)