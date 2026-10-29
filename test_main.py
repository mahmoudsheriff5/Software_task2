import unittest
from main import Appointment, Doctor, Patient, ClinicSystem

class TestClinicSystem(unittest.TestCase):
    def test_appointment_limit(self):
        clinic = ClinicSystem(max_appointments=4)
        dr = Doctor(1, "Test Doctor", ["10:00"])
        patient = Patient(101, "Test Patient")
        
        # Test initial count
        self.assertEqual(patient.upcomingAppointmentsCount, 0)
        
        # Book up to limit
        for i in range(4):
            patient.bookAppointment(clinic, dr, f"2023-11-1{i}", "10:00", doctor_will_accept=True)
            
        self.assertEqual(patient.upcomingAppointmentsCount, 4)
        
        # Check limit reached
        self.assertFalse(clinic.checkAppointmentLimit(patient))

if __name__ == '__main__':
    unittest.main()
