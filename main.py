from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="HealthConnect API",
    description="MVP funcional para la gestión y optimización de consultas médicas.",
    version="1.0.0"
)

# --- BASE DE DATOS EN MEMORIA SIMULADA ---
# Inicializamos con un registro de ejemplo para pruebas de consulta
appointments_db = [
    {
        "id": 1,
        "patient_name": "Carlos Gomez",
        "phone": "87654321",
        "specialty": "Pediatria",
        "status": "Pendiente",
        "doctor_name": None
    }
]
id_counter = 2  # El siguiente ID que se asignará de forma única


# --- MODELOS DE VALIDACIÓN PYDANTIC (Data Validation) ---
class AppointmentCreate(BaseModel):
    patient_name: str = Field(..., min_length=1, description="Nombre del paciente")
    phone: str = Field(..., min_length=1, description="Teléfono de contacto")
    specialty: str = Field(..., min_length=1, description="Especialidad solicitada")

class StatusUpdate(BaseModel):
    status: str = Field(..., description="Nuevo estado de la cita (ej. Asignada, Finalizada)")
    doctor_name: Optional[str] = Field(None, description="Nombre del médico asignado si aplica")


# --- ENDPOINTS REQUERIDOS POR EL MVP ---

# 1. POST /appointments (Creación - HISTORIA MUST HU-01)
@app.post("/appointments", status_code=status.HTTP_201_CREATED, summary="Registrar solicitud de cita")
def create_appointment(appointment: AppointmentCreate):
    global id_counter
    
    # Validación de negocio básica (Error 400 simulado si mandan datos vacíos con espacios)
    if not appointment.patient_name.strip() or not appointment.phone.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre del paciente y el teléfono no pueden estar vacíos."
        )
        
    new_appointment = {
        "id": id_counter,
        "patient_name": appointment.patient_name.strip(),
        "phone": appointment.phone.strip(),
        "specialty": appointment.specialty.strip(),
        "status": "Pendiente",
        "doctor_name": None
    }
    appointments_db.append(new_appointment)
    id_counter += 1
    return new_appointment


# 2. GET /appointments (Consulta General - Endpoint adicional)
@app.get("/appointments", summary="Listar todas las citas")
def list_appointments():
    return appointments_db


# 3. GET /appointments/{id} (Consulta específica - Control de estado)
@app.get("/appointments/{id}", summary="Consultar estado de una cita")
def get_appointment(id: int):
    for appt in appointments_db:
        if appt["id"] == id:
            return appt
    # Error 404 si el ID no existe en la memoria
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cita con ID {id} no encontrada."
    )


# 4. PATCH /appointments/{id}/status (Actualización - HISTORIA MUST HU-02)
@app.patch("/appointments/{id}/status", summary="Asignar médico o actualizar estado")
def update_appointment_status(id: int, update_data: StatusUpdate):
    for appt in appointments_db:
        if appt["id"] == id:
            # Validar que si cambia a "Asignada" se envíe un médico obligatoriamente
            if update_data.status.strip() == "Asignada" and not update_data.doctor_name:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Se requiere el nombre de un médico para cambiar el estado a 'Asignada'."
                )
            
            appt["status"] = update_data.status.strip()
            if update_data.doctor_name:
                appt["doctor_name"] = update_data.doctor_name.strip()
            return appt
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cita con ID {id} no encontrada."
    )