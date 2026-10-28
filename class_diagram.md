```mermaid

classDiagram
    class Patient {
        +int patientId
        +String name
        +int upcomingAppointmentsCount
        +viewAvailability(Doctor doctor)
        +bookAppointment(String date, String time)
    }
    
    class Doctor {
        +int doctorId
        +String name
        +List~String~ availableSlots
        +acceptAppointment(Appointment appt)
        +declineAppointment(Appointment appt)
    }
    
    class Appointment {
        +int appointmentId
        +String date
        +String time
        +String status
        +updateStatus(String newStatus)
    }
    
    class ClinicSystem {
        +int MAX_APPOINTMENTS
        +checkAppointmentLimit(Patient patient) bool
        +notifyStatus(Patient patient, Appointment appt)
    }

    Patient "1" -- "*" Appointment : books
    Doctor "1" -- "*" Appointment : reviews
    ClinicSystem ..> Patient : monitors limit
    ClinicSystem ..> Appointment : manages status
    ```
