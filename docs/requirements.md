# Requerimientos del Sistema - HealthConnect

## 1. Enlace al Backlog
Consulte el tablero de gestión del proyecto aquí:
[https://github.com/users/STRYKER-LUIS/projects/1/views/4?layout=board]

## 2. Lista de Historias de Usuario
| ID | Título | Prioridad |
|--|--|--|
| HU-01 | Registro de solicitud de cita por el paciente | Must |
| HU-02 | Asignación de médico a una cita pendiente | Must |
| HU-03 | Consulta de estado de cita por el paciente | Should |
| HU-04 | Finalización de consulta y cambio de estado | Should |
| HU-05 | Visualización de agenda diaria para el médico | Could |
| HU-06 | Filtrado de médicos por especialidad | Could |
| HU-07 | Cancelación de cita por parte del administrativo | Could |
| HU-08 | Reporte mensual de consultas atendidas | Won't |

## 3. Detalle de Historias Principales (Must)

### HU-01: Registro de solicitud de cita
**Criterios de Aceptación:**
* El sistema debe validar que el nombre y teléfono no estén vacíos.
* Se debe generar un ID único para la solicitud de cita.

**Escenario (Given/When/Then):**
* **Given:** Un paciente que ingresa al formulario de solicitud.
* **When:** Envía su nombre "Luis Diaz" y teléfono "54320564" y selecciona la especialidad "Pediatría".
* **Then:** El sistema registra la cita con estado "Pendiente" y devuelve un código de confirmación.

### HU-02: Asignación de médico a una cita pendiente
**Criterios de Aceptación:**
* Solo se pueden asignar médicos que pertenezcan a la especialidad solicitada.
* El estado de la cita debe cambiar de "Pendiente" a "Asignada".

**Escenario (Given/When/Then):**
* **Given:** Una cita en estado "Pendiente" para la especialidad "Cardiología".
* **When:** El administrativo selecciona al "Dr. Pérez" (especialista en Cardiología) y confirma la asignación.
* **Then:** La cita se actualiza con el nombre del médico y el estado cambia a "Asignada".

## 4. MVP Rationale
Para el Producto Mínimo Viable (MVP), se han priorizado las historias HU-01 y HU-02. La razón es que el flujo core del negocio depende de que exista una solicitud de servicio (cita) y un profesional asignado para atenderla. Sin estas dos funcionalidades, el sistema no cumple su propósito principal de intermediación médica. Se postergan los reportes y cancelaciones para fases posteriores para asegurar la estabilidad del flujo transaccional inicial.