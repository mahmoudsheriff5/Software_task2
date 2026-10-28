sequenceDiagram
    autonumber
    actor Patient
    participant ClinicSystem
    participant Appointment
    participant Doctor

    Patient->>ClinicSystem: bookAppointment(date, time)
    ClinicSystem->>ClinicSystem: checkAppointmentLimit(patient)
    
    alt Limit Exceeded (>= N)
        ClinicSystem-->>Patient: Error: Maximum appointment limit reached
    else Limit OK (< N)
        ClinicSystem->>Appointment: create(date, time, status="Pending")
        ClinicSystem->>Doctor: reviewAppointment(appointment)
        
        alt Doctor Accepts
            Doctor->>Appointment: updateStatus("Accepted")
            Doctor-->>ClinicSystem: Confirm acceptance
            ClinicSystem->>Patient: notifyStatus("Accepted")
        else Doctor Declines
            Doctor->>Appointment: updateStatus("Declined")
            Doctor-->>ClinicSystem: Confirm declination
            ClinicSystem->>Patient: notifyStatus("Declined")
        end
    end
