# System Brief - HealthConnect

## 1. Descripción del Sistema
HealthConnect es una plataforma diseñada para digitalizar y optimizar la gestión de consultas médicas, permitiendo un flujo eficiente desde la solicitud del paciente hasta la atención del especialista que se encargar de la consulta y de brindar una mejor y mas fluida atencion.

## 2. Problema ha resuelve
Actualmente, muchas clínicas pequeñas y medianas gestionan sus citas de forma manual o desarticulada, lo que provoca:
* Traslape de horarios.
* Falta de seguimiento al estado de las citas.
* Dificultad para asignar médicos según su especialidad de forma rápida.

## 3. Stakeholders
* **Pacientes:** Usuarios que solicitan atención médica.
* **Personal Administrativo:** Encargados de organizar la agenda y asignar médicos.
* **Médicos:** Profesionales que visualizan su agenda y registran el fin de la consulta.

## 4. Alcance (Scope)
* Registro de pacientes y médicos.
* Gestión de citas (creación, asignación y actualización de estado).
* Filtrado de médicos por especialidad.

## 5. Fuera de Alcance (No-Scope)
* Procesamiento de pagos y facturación.
* Módulo de farmacia e inventarios.
* Consultas por video (Telemedicina).

## 6. Diagrama de Contexto (Mermaid)
```mermaid
graph TD
    A[Paciente] -- Solicita Cita --> B(HealthConnect)
    C[Administrativo] -- Asigna Médico --> B
    D[Médico] -- Actualiza Estado --> B
    B -- Notifica/Confirma --> A