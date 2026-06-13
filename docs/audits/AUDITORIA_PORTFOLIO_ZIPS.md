# Auditoría REAL desde ZIPs (sin GitHub token)

## 0) Alcance y restricciones aplicadas
- Auditoría realizada **solo por lectura estática** de código y estructura de los ZIPs locales.
- **No se ejecutaron tests**, **no se instalaron dependencias** y **no se modificó código fuente**.
- Si una afirmación no pudo validarse en archivos, se marca como **No verificable**.

---

## 1) Paso 1 — Localización de ZIPs

ZIPs localizados (rutas absolutas):
- `/workspace/CV/Horas_Sindicales-main (1).zip`
- `/workspace/CV/clinicdesk-main.zip`
- `/workspace/CV/Bateria_Fotovoltaica-main (1).zip`

Resultado: se encontraron los 3 proyectos requeridos.

---

## 2) Paso 2 — Descompresión y normalización

Carpetas de trabajo:
- `/workspace/portfolio/src/Horas_Sindicales`
- `/workspace/portfolio/src/clinicdesk`
- `/workspace/portfolio/src/Bateria_Fotovoltaica`

Verificación rápida de contenido:
- **Horas_Sindicales**: contiene `README.md`, `requirements.txt`, `app/`, `tests/`, `migrations/`, `packaging/`, `installer/`.
- **clinicdesk**: contiene `README.md`, `requirements.txt`, `clinicdesk/app/`, `tests/`, `docs/`.
- **Bateria_Fotovoltaica**: contiene `README.md`, `ARCHITECTURE.md`, `pyproject.toml`, `application/`, `domain/`, `infrastructure/`, `ui/`, `tests/`.

---

## 3) Resumen ejecutivo (10–15 líneas)

Este portfolio demuestra un perfil orientado a **aplicaciones desktop en Python con PySide6**, con foco en separación por capas y casos de uso en los tres repositorios. Evidencias claras de UI Qt/PySide6 aparecen en `Horas_Sindicales/app/ui`, `clinicdesk/app/pages` y `Bateria_Fotovoltaica/ui`. 

En persistencia, hay uso intensivo de **SQLite** en Horas_Sindicales y clinicdesk (repositorios y `schema.sql`), mientras que Bateria_Fotovoltaica prioriza persistencia de proyecto en **JSON/Parquet** (sin base SQL principal). 

En integración externa, Horas_Sindicales incorpora sincronización con **Google Sheets** (adaptadores/clientes dedicados). En exportación/reporting hay evidencia de PDF (Horas_Sindicales) y Excel (Bateria_Fotovoltaica). 

En testing, los tres proyectos tienen estructura de pruebas y uso de `pytest` (y mezcla con `unittest` en Horas_Sindicales), incluyendo separación unit/integration/performance en Bateria_Fotovoltaica.

En packaging/entrega para Windows, Horas_Sindicales es el más maduro (PyInstaller `.spec`, Inno Setup `.iss`, scripts release). clinicdesk muestra launchers `.bat` pero no se observan `.spec/.iss`. Bateria_Fotovoltaica incluye launcher `.bat` y scripts legacy, sin evidencia directa de empaquetado instalable actual.

Fortalezas: arquitectura por capas, dominio de PySide6, persistencia local, suites de tests presentes y documentación técnica. Debilidades: CI/CD **No verificable** (no evidencia de `.github/workflows` en los ZIP auditados), métricas de calidad/cobertura ejecutada **No verificable**, y señales de legado/duplicidad estructural en clinicdesk y Bateria_Fotovoltaica.

---

## 4) Auditoría por proyecto

## 4.1 Horas_Sindicales

### ¿Qué es?
Aplicación de escritorio PySide6 para gestión de horas sindicales, con persistencia SQLite, migraciones y sincronización bidireccional con Google Sheets.

### Evidencias

- **Arquitectura**
  - Separación explícita de capas en `app/application`, `app/domain`, `app/infrastructure`, `app/ui` (`/workspace/portfolio/src/Horas_Sindicales/README.md`).
  - Contratos/puertos en dominio mediante `Protocol` (`/workspace/portfolio/src/Horas_Sindicales/app/domain/ports.py`).
  - Caso de uso aislado en `app/application/use_cases/sync_sheets.py`.

- **Persistencia / Integraciones**
  - Repositorio SQLite: `/workspace/portfolio/src/Horas_Sindicales/app/infrastructure/repos_sqlite.py`.
  - Sistema de migraciones versionadas: `/workspace/portfolio/src/Horas_Sindicales/app/infrastructure/migrations.py` y carpeta `/workspace/portfolio/src/Horas_Sindicales/migrations/`.
  - Integración Google Sheets: `sheets_gateway_gspread.py`, `sheets_client.py`, `sheets_repository.py`, `sync_sheets_adapter.py` en `/workspace/portfolio/src/Horas_Sindicales/app/infrastructure/`.

- **UI desktop**
  - Modelos/elementos Qt en `/workspace/portfolio/src/Horas_Sindicales/app/ui/models_qt.py` y subárbol `/workspace/portfolio/src/Horas_Sindicales/app/ui/`.

- **Tests (sin ejecutar)**
  - Suite en `/workspace/portfolio/src/Horas_Sindicales/tests/` con subcarpetas `domain`, `application`, `infrastructure`, `pdf`.
  - Evidencia de `pytest` en `/workspace/portfolio/src/Horas_Sindicales/tests/conftest.py`.
  - Evidencia de `unittest` en `/workspace/portfolio/src/Horas_Sindicales/tests/test_solicitudes_historico.py`.

- **Packaging / entrega**
  - PyInstaller spec: `/workspace/portfolio/src/Horas_Sindicales/packaging/HorasSindicales.spec`.
  - Inno Setup: `/workspace/portfolio/src/Horas_Sindicales/installer/HorasSindicales.iss`.
  - Pipeline de release por BAT: `/workspace/portfolio/src/Horas_Sindicales/scripts/release/`.

- **Docs**
  - README y documentación funcional/técnica en `/workspace/portfolio/src/Horas_Sindicales/docs/` (ej. `reglas_negocio.md`, `release_windows.md`, `sincronizacion_google_sheets.md`).

### Bullets ATS (6–10)
- Desarrollé aplicación desktop en **Python + PySide6** para gestión operativa de horas sindicales con interfaz modular por capas (`app/ui`, `app/application`, `app/domain`, `app/infrastructure`).
- Implementé contratos de acceso mediante **ports/protocols** en dominio para desacoplar casos de uso de infraestructura (`app/domain/ports.py`).
- Construí persistencia local sobre **SQLite** con repositorios dedicados y soporte de operaciones de negocio (`app/infrastructure/repos_sqlite.py`).
- Diseñé y mantuve migraciones versionadas **up/down SQL** y utilidades CLI de migración (`migrations/*.sql`, `app/infrastructure/migrations_cli.py`).
- Integré sincronización bidireccional con **Google Sheets** usando adaptadores y clientes específicos (`sheets_gateway_gspread.py`, `sheets_client.py`, `sync_sheets_adapter.py`).
- Desarrollé generación de documentos **PDF** para solicitudes mediante módulo dedicado (`app/pdf/pdf_builder.py`, `app/pdf/service.py`).
- Preparé empaquetado de escritorio en Windows con **PyInstaller + Inno Setup** (`packaging/HorasSindicales.spec`, `installer/HorasSindicales.iss`).
- Estructuré pruebas automáticas con **pytest** (y cobertura de dominio/aplicación/infraestructura) en `tests/`.

### Tech highlights (entrevista)
- Evidencia fuerte de arquitectura por puertos y adaptadores (`app/domain/ports.py` + implementaciones en infraestructura).
- Integración real de terceros (Google Sheets) con manejo explícito de errores/rate limit (`app/infrastructure/sheets_errors.py`, `tests/infrastructure/test_sheets_rate_limit.py`).
- Flujo completo de producto desktop: UI + persistencia + documentos + instalador Windows.

---

## 4.2 clinicdesk

### ¿Qué es?
Aplicación de escritorio de gestión clínica (pacientes, citas, farmacia, personal, etc.) con UI PySide6 y persistencia SQLite.

### Evidencias

- **Arquitectura**
  - Capas funcionales bajo `clinicdesk/app/`: `domain`, `application`, `infrastructure`, `pages`, `controllers`.
  - Contratos de repositorio en dominio vía `ABC` y `abstractmethod` (`/workspace/portfolio/src/clinicdesk/clinicdesk/app/domain/repositorios.py`).
  - Casos de uso explícitos en `/workspace/portfolio/src/clinicdesk/clinicdesk/app/application/usecases/` (ej. `crear_cita.py`).

- **Persistencia / Integraciones**
  - Persistencia SQLite central en `/workspace/portfolio/src/clinicdesk/clinicdesk/app/infrastructure/sqlite/`.
  - Esquema SQL versionado por archivo base en `/workspace/portfolio/src/clinicdesk/clinicdesk/app/infrastructure/sqlite/schema.sql`.
  - Repositorios por agregado (citas, pacientes, médicos, personal, etc.) en el mismo subárbol.

- **UI desktop**
  - Uso extensivo de PySide6 en controladores y páginas (`clinicdesk/app/controllers/*.py`, `clinicdesk/app/pages/**/*.py`).
  - Formularios y diálogos Qt (`QDialog`) en módulos de páginas y dialogs.

- **Tests (sin ejecutar)**
  - Suite en `/workspace/portfolio/src/clinicdesk/tests/` con `conftest.py` y pruebas por módulo (`test_pacientes.py`, `test_citas.py`, etc.).
  - Dependencias de test en `/workspace/portfolio/src/clinicdesk/requirements-dev.txt` (`pytest`, `pytest-cov`).
  - Guía de testing en `/workspace/portfolio/src/clinicdesk/docs/TESTING.md`.

- **Packaging / entrega**
  - Launchers/scripts BAT: `/workspace/portfolio/src/clinicdesk/launch.bat`, `launcher.bat`, `run_tests.bat`.
  - `.spec/.iss` de instalador: **No verificable** en la evidencia encontrada.

- **Docs**
  - README operativo y guía de tests (`README.md`, `docs/TESTING.md`).

### Bullets ATS (6–10)
- Construí aplicación desktop de gestión clínica sobre **Python + PySide6**, con navegación por módulos asistenciales y administrativos (`clinicdesk/app/pages`).
- Implementé arquitectura por capas con separación **domain / application / infrastructure / UI** en `clinicdesk/app/`.
- Definí contratos de repositorio con **ABC/abstractmethod** para desacoplar lógica de negocio de persistencia (`domain/repositorios.py`).
- Desarrollé casos de uso para reglas clínicas y operativas (p. ej. creación de citas con validaciones y overrides) en `application/usecases/crear_cita.py`.
- Implementé persistencia relacional local con **SQLite** y repositorios por entidad (`infrastructure/sqlite/repos_*.py`).
- Gestioné esquema de base de datos mediante SQL explícito (`infrastructure/sqlite/schema.sql`).
- Añadí pruebas automáticas con **pytest** y fixtures para módulos críticos (`tests/conftest.py`, `tests/test_*.py`).
- Documenté flujos de ejecución y testing para onboarding técnico (`README.md`, `docs/TESTING.md`).

### Tech highlights (entrevista)
- Buen dominio de PySide6 en una app multipágina con diálogos transaccionales y controladores.
- Diseño con contratos de dominio reutilizables y repositorios concretos en SQLite.
- Cobertura funcional amplia por verticales (pacientes, citas, farmacia, personal, incidencias).

---

## 4.3 Bateria_Fotovoltaica

### ¿Qué es?
Simulador desktop BESS/FV en Python 3.11+ con PySide6, orientado a simulación energética, dimensionamiento y exportación de resultados.

### Evidencias

- **Arquitectura**
  - Estructura en `domain/`, `application/`, `infrastructure/`, `ui/` descrita en `/workspace/portfolio/src/Bateria_Fotovoltaica/README.md`.
  - Documento técnico de arquitectura en `/workspace/portfolio/src/Bateria_Fotovoltaica/ARCHITECTURE.md`.
  - Casos de uso y módulos de negocio en `application/use_cases.py`, `application/project_use_cases.py`, `application/finance/*`.

- **Persistencia / Integraciones**
  - Persistencia de proyecto en JSON/Parquet (`/workspace/portfolio/src/Bateria_Fotovoltaica/infrastructure/persistence/project_store.py`).
  - Lectura de datos tabulares CSV/Excel (`/workspace/portfolio/src/Bateria_Fotovoltaica/infrastructure/io/excel_reader.py`).
  - Exportación Excel en `/workspace/portfolio/src/Bateria_Fotovoltaica/infrastructure/io/excel_writer.py`.
  - SQLite/migraciones SQL: **No verificable** como mecanismo principal del proyecto actual.

- **UI desktop**
  - Uso intensivo de PySide6 en `ui/main_window.py`, `ui/pages/*`, `ui/components/*`, `ui/presentation_window.py`.
  - Dependencia declarada en `requirements.txt` y `pyproject.toml`.

- **Tests (sin ejecutar)**
  - Estructura explícita: `/workspace/portfolio/src/Bateria_Fotovoltaica/tests/{unit,integration,performance}`.
  - Configuración pytest en `/workspace/portfolio/src/Bateria_Fotovoltaica/pytest.ini`.
  - Múltiples pruebas de negocio, robustez y rendimiento en `tests/test_*.py`.

- **Packaging / entrega**
  - Launcher principal Windows: `/workspace/portfolio/src/Bateria_Fotovoltaica/00_EJECUTAR_SIMULADOR.bat`.
  - Scripts adicionales legacy en `tools/launcher/` y `docs/obsolete/.../scripts/`.
  - `.spec/.iss` de instalador actual: **No verificable**.

- **Docs**
  - README amplio de uso, testing y flujo funcional.
  - Documento de arquitectura dedicado (`ARCHITECTURE.md`).

### Bullets ATS (6–10)
- Desarrollé simulador desktop para análisis BESS/FV en **Python 3.11 + PySide6**, con enfoque en dimensionamiento y análisis de escenarios (`ui/`, `application/`).
- Estructuré el sistema por capas (**domain/application/infrastructure/ui**) con casos de uso explícitos (`application/use_cases.py`, `application/project_use_cases.py`).
- Implementé carga de datos energéticos desde **CSV/Excel** y normalización previa a simulación (`infrastructure/io/excel_reader.py`, `application/dataset_validator.py`).
- Implementé persistencia de proyectos en **JSON + Parquet** con migración ligera de esquema (`infrastructure/persistence/project_store.py`).
- Desarrollé módulos financieros para cálculo de KPIs y estrategia de oferta (`application/finance/financial_kpis.py`, `application/finance/offer_strategy.py`).
- Añadí exportación de resultados a **Excel** para entrega técnica/comercial (`infrastructure/io/excel_writer.py`).
- Estructuré pruebas automáticas en tres niveles (**unit/integration/performance**) (`tests/unit`, `tests/integration`, `tests/performance`).
- Documenté arquitectura y operación de producto en README y documento técnico (`README.md`, `ARCHITECTURE.md`).

### Tech highlights (entrevista)
- Proyecto sólido para narrar diseño de simuladores y trade-off entre exactitud/rapidez.
- Evidencia de flujo end-to-end: ingesta de datos, simulación, persistencia de proyecto y exportación.
- Buen material para entrevista en validación de datasets, KPIs y diseño de UI técnica en PySide6.

---

## 5) Matriz de habilidades (verificables)

| Área | Habilidad | Nivel | Evidencia (ruta/archivo) |
|---|---|---|---|
| Desktop | PySide6 / Qt Widgets | Avanzado | `Horas_Sindicales/app/ui/`, `clinicdesk/app/pages/`, `Bateria_Fotovoltaica/ui/` |
| Arquitectura | Separación por capas | Avanzado | `Horas_Sindicales/app/{domain,application,infrastructure,ui}`, `clinicdesk/app/{domain,application,infrastructure,pages}`, `Bateria_Fotovoltaica/{domain,application,infrastructure,ui}` |
| Arquitectura | Puertos/contratos de repositorio | Intermedio-Avanzado | `Horas_Sindicales/app/domain/ports.py`, `clinicdesk/app/domain/repositorios.py` |
| Persistencia | SQLite | Avanzado | `Horas_Sindicales/app/infrastructure/repos_sqlite.py`, `clinicdesk/app/infrastructure/sqlite/` |
| Persistencia | Migraciones SQL | Intermedio | `Horas_Sindicales/migrations/*.sql`, `Horas_Sindicales/app/infrastructure/migrations.py` |
| Integraciones | Google Sheets (gspread) | Intermedio | `Horas_Sindicales/app/infrastructure/sheets_gateway_gspread.py`, `docs/sincronizacion_google_sheets.md` |
| Testing | Pytest + fixtures | Intermedio-Avanzado | `*/tests/conftest.py`, `clinicdesk/requirements-dev.txt`, `Bateria_Fotovoltaica/pytest.ini` |
| Testing | Diseño de suites por tipo (unit/integration/performance) | Intermedio | `Bateria_Fotovoltaica/tests/{unit,integration,performance}` |
| Documentos | Generación PDF | Intermedio | `Horas_Sindicales/app/pdf/pdf_builder.py` |
| Datos | Lectura/Escritura Excel | Intermedio | `Bateria_Fotovoltaica/infrastructure/io/excel_reader.py`, `excel_writer.py` |
| Packaging Windows | PyInstaller + Inno Setup | Intermedio | `Horas_Sindicales/packaging/HorasSindicales.spec`, `installer/HorasSindicales.iss` |
| Automatización | Scripts BAT de lanzamiento/release | Intermedio | `Horas_Sindicales/scripts/release/*.bat`, `clinicdesk/launch*.bat`, `Bateria_Fotovoltaica/00_EJECUTAR_SIMULADOR.bat` |

---

## 6) Skills recomendadas para CV (priorizadas)

1. **Python Desktop Engineering (PySide6/Qt)**
2. **Arquitectura por capas + casos de uso + contratos de repositorio**
3. **Persistencia SQLite y diseño de repositorios**
4. **Integración con servicios externos (Google Sheets/gspread)**
5. **Testing con pytest (fixtures, suites por dominio)**
6. **Packaging y distribución en Windows (PyInstaller/Inno Setup)**
7. **Procesamiento de datos tabulares (CSV/Excel) y exportación**
8. **Documentación técnica y operativa de producto**

(Ordenadas por recurrencia y solidez de evidencia en los 3 repositorios).

---

## 7) Mejoras Top 8 (alto retorno, sin tocar código ahora)

1. **Estandarizar README de los 3 repos** con secciones homogéneas (arquitectura, ejecución, testing, packaging, troubleshooting).
2. **Añadir evidencia visual/demo** (GIF o video corto) para UI de cada proyecto.
3. **Agregar CI mínima** (lint + tests) cuando haya acceso a GitHub Actions (actualmente No verificable en ZIP).
4. **Publicar matriz de compatibilidad** (Python/OS/dependencias) en docs de cada repo.
5. **Formalizar estrategia de versionado y changelog** (`CHANGELOG.md`) por release.
6. **Unificar convenciones de testing** (pytest como estándar; documentar cuándo se usa unittest).
7. **Documentar claramente pipeline de empaquetado** en clinicdesk y Bateria_Fotovoltaica (si aplica) para igualar madurez de Horas_Sindicales.
8. **Añadir documento de arquitectura “as-built”** en clinicdesk (equivalente al `ARCHITECTURE.md` de Bateria_Fotovoltaica).

---

## 8) Observaciones de verificabilidad

- Métricas cuantitativas de rendimiento/cobertura reales: **No verificable** sin ejecutar tests/herramientas.
- Estado de CI/CD remoto y pipelines en GitHub: **No verificable** en auditoría basada solo en ZIPs locales.
- Adopción estricta de “Clean Architecture” completa (inversión de dependencias end-to-end en todos los módulos): **Parcialmente verificable** (hay separación por capas y contratos en repos clave, pero no se auditó ejecución ni acoplamiento dinámico).

