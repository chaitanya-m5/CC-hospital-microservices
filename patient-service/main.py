from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Patient Service",
    description="Manages patient information.",
    version="1.0.0"
)

patients = {
    1: {"id": 1, "name": "Rahul Sharma", "age": 35, "gender": "Male"},
    2: {"id": 2, "name": "Priya Patil", "age": 28, "gender": "Female"},
    3: {"id": 3, "name": "Arjun Kumar", "age": 42, "gender": "Male"},
}

@app.get("/health")
def health():
    return {"service": "patient-service", "status": "healthy"}

@app.get("/patients")
def get_patients():
    return list(patients.values())

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patients[patient_id]
