# Arquitectura del Sistema - HealthConnect

## 1. Descripción de la Arquitectura
Para este MVP, se ha seleccionado una arquitectura de **Capa Única (Monolito Simple)** orientada a micro-servicios mediante el framework **FastAPI**. El sistema se comunica a través de una interfaz RESTful que maneja datos en formato JSON.

## 2. Diagrama de Arquitectura (Mermaid)
```mermaid
graph TD
    A[Cliente / Swagger UI] -- HTTP Requests --> B(FastAPI Router)
    B -- Modelos Pydantic --> C{Lógica de Negocio}
    C -- CRUD --> D[(Almacenamiento en Memoria)]
    D -- Respuesta JSON --> A
