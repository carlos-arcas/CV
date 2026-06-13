# Copy estratégico del CV (Backend Python / Arquitectura)

## Versión ES (lista para pegar)

### Resumen profesional
Ingeniero backend Python con foco en arquitectura y diseño de sistemas mantenibles. Trabajo con Clean Architecture para separar dominio, aplicación e infraestructura, de forma que el producto pueda evolucionar sin degradar calidad ni velocidad de entrega. Mi especialidad es convertir procesos operativos frágiles en sistemas trazables con automatización, testing por riesgo y logging estructurado.

Busco aportar en equipos remotos que valoren diseño técnico, ownership y mejora continua, en roles senior con rango 30k–40k+ según alcance.

### Experiencia profesional
**AYESA — Proyectos Endesa (2019–Actualidad)**  
Diseño e implementación de soluciones backend y data para operación crítica.

**Endesa X (Marketing) (2024–Actualidad)**
- Diseñé pipelines ETL en Python con separación por capas (ingesta, transformación, publicación).
- Integré Salesforce (SOQL), SQL y Redshift mediante adaptadores para aislar infraestructura del dominio.
- Implementé validaciones automáticas y controles de calidad de datos antes de la publicación.
- Estandaricé datasets para BI con contratos de esquema y trazabilidad de transformaciones.
- Refactoricé utilidades hacia módulos testeables con pytest y logging estructurado.
- Entregué tooling CLI/desktop para usuarios no técnicos sobre un core de dominio compartido.
- **Impacto estimado:** 25–35% menos retrabajo operativo por errores de datos.

**Endesa Distribución (2019–2024)**
- Construí automatizaciones Python + SQL para extracciones recurrentes y ejecución reproducible.
- Separé reglas de negocio de consultas ad-hoc para reducir coste de mantenimiento.
- Introduje controles de calidad (nulos, duplicados, consistencia cruzada) en puntos críticos.
- Diseñé salidas orientadas a consumo operacional con versionado básico y documentación técnica.
- Formalicé criterios de entrega para facilitar continuidad del servicio entre equipos.
- **Impacto estimado:** mejora >30% en incidencias de reporting por discrepancias entre fuentes.

### Proyectos (descripción estratégica)
**Horas Sindicales**
- Reemplacé un flujo manual por una aplicación desktop con arquitectura por capas y puertos/adaptadores.
- Aislé reglas de negocio de UI e integración con Google Sheets para reducir acoplamiento.
- Implementé migraciones versionadas, pruebas por nivel y trazabilidad con logging estructurado.
- **Impacto estimado:** 35–45% menos tiempo de consolidación mensual; >50% menos incidencias de consistencia.

**ClinicDesk**
- Diseñé una aplicación multipágina con separación dominio/aplicación/infraestructura/ui.
- Convertí lógica acoplada a interfaz en casos de uso reutilizables (UI + CLI).
- Apliqué contratos explícitos para repositorios y pruebas de regresión sobre flujos críticos.
- **Impacto estimado:** ~30% menos pasos operativos y releases funcionales más predecibles.

**Batería Fotovoltaica**
- Construí un simulador técnico-financiero con separación estricta entre cálculo, persistencia y presentación.
- Implementé validación de entradas, suites de pruebas y almacenamiento estructurado (JSON/Parquet).
- Preparé base escalable para nuevos escenarios sin comprometer integridad del modelo.
- **Impacto estimado:** 40–60% menos tiempo de evaluación frente a análisis manual en hojas.

### Stack tecnológico (con criterio)
- **Arquitectura backend:** Clean Architecture, Ports & Adapters, Repository pattern, diseño de casos de uso.
- **Python engineering:** Python, pytest (unit/integration/contract), refactor orientado a mantenibilidad.
- **Operabilidad:** logging estructurado, documentación técnica, automatización reproducible.
- **Datos e integraciones:** SQL, SOQL, Redshift, SQLite, migraciones versionadas, ETL con validaciones.
- **Producto interno:** separación CLI + UI, packaging desktop/CLI, Power BI para consumo confiable.

### What I bring to a team
- Diseño sistemas que pueden escalar en complejidad sin escalar deuda técnica al mismo ritmo.
- Bajo el coste de cambio separando dominio e infraestructura desde el inicio.
- Convierto tareas manuales en automatizaciones auditables y mantenibles.
- Priorizo testing donde el riesgo real es mayor, no donde “queda bien”.
- Hago visible el comportamiento del sistema con logging estructurado y contratos claros.
- Alineo decisiones técnicas con impacto operativo (tiempo, fiabilidad, retrabajo).

---

## English version (professional)

### Professional Summary
Senior Python backend engineer focused on architecture and maintainable system design. I apply Clean Architecture to keep domain, application, and infrastructure concerns separated, so products can evolve without losing delivery speed or technical quality. I specialize in turning fragile operational workflows into traceable systems through automation, risk-based testing, and structured logging.

I am targeting remote senior roles in the 30k–40k+ range, depending on scope and architectural ownership.

### Professional Experience
**AYESA — Endesa Projects (2019–Present)**  
Design and implementation of backend/data solutions for critical operations.

**Endesa X (Marketing) (2024–Present)**
- Designed Python ETL pipelines with layered boundaries (ingestion, transformation, publishing).
- Integrated Salesforce (SOQL), SQL, and Redshift through adapters, isolating infrastructure from domain rules.
- Implemented automated data validation gates before dataset publication.
- Standardized BI datasets with schema contracts and transformation traceability.
- Refactored legacy utilities into testable modules using pytest and structured logging.
- Delivered CLI/desktop tooling for non-technical users on top of a shared domain core.
- **Estimated impact:** 25–35% reduction in operational rework due to data issues.

**Endesa Distribución (2019–2024)**
- Built Python + SQL automation for recurring extraction flows with reproducible execution.
- Separated business rules from ad-hoc querying to reduce maintenance cost.
- Introduced data quality controls (nulls, duplicates, cross-field consistency) on critical paths.
- Designed operational outputs with lightweight versioning and technical documentation.
- Standardized delivery criteria to improve service continuity across teams.
- **Estimated impact:** >30% improvement in reporting incidents caused by source discrepancies.

### Projects (strategic wording)
**Horas Sindicales**
- Replaced manual spreadsheet-driven operations with a layered desktop system using ports/adapters.
- Isolated business rules from UI and Google Sheets integration to reduce coupling.
- Implemented versioned migrations, multi-level tests, and structured logging for traceability.
- **Estimated impact:** 35–45% faster monthly consolidation; >50% fewer consistency incidents.

**ClinicDesk**
- Designed a multi-page desktop application with clear domain/application/infrastructure/UI boundaries.
- Moved UI-coupled logic into reusable use cases (shared across UI + CLI workflows).
- Applied explicit repository contracts and regression tests for critical flows.
- **Estimated impact:** ~30% fewer operational steps and more predictable feature releases.

**Batería Fotovoltaica**
- Built a technical-financial simulator with strict separation of calculation, persistence, and presentation.
- Added input validation, test suites, and structured storage (JSON/Parquet).
- Enabled scalable scenario evolution without compromising model integrity.
- **Estimated impact:** 40–60% faster scenario evaluation vs manual spreadsheet analysis.

### Technology Stack (context-driven)
- **Backend architecture:** Clean Architecture, Ports & Adapters, Repository pattern, use-case design.
- **Python engineering:** Python, pytest (unit/integration/contract), maintainability-oriented refactoring.
- **Operability:** structured logging, technical documentation, reproducible automation.
- **Data & integrations:** SQL, SOQL, Redshift, SQLite, versioned migrations, validated ETL.
- **Internal product delivery:** CLI + UI separation, desktop/CLI packaging, Power BI-ready datasets.

### What I bring to a team
- I design systems that scale in complexity without scaling technical debt at the same rate.
- I reduce change cost by separating domain and infrastructure early.
- I turn manual operations into auditable, maintainable automation.
- I prioritize testing based on real risk, not checkbox coverage.
- I make system behavior observable through structured logging and explicit contracts.
- I align technical decisions with measurable operational outcomes.

---

## Por qué este cambio mejora percepción senior
- Sustituye lenguaje de “ejecución de tareas” por lenguaje de **decisiones de diseño** y trade-offs.
- Aterriza tecnologías en **problemas concretos** (por qué se usan y qué riesgo reducen).
- Refuerza **ownership arquitectónico**: límites entre capas, contratos, coste de cambio.
- Introduce **impacto medible** con métricas estimadas y señaladas como tales (credibilidad > exageración).
- Muestra una narrativa de ingeniería: diseño, implementación, operabilidad y evolución.
