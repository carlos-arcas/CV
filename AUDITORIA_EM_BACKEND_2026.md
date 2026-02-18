# Auditoría técnica del CV (enfoque Engineering Manager Backend)

## 1) Señales técnicas visibles

### Lo que sí suma
- **Hablas de separación de dominio e infraestructura** y de reducir complejidad accidental. Eso es señal de criterio de diseño más allá de “hacer que funcione”.
- En experiencia incluyes **ETL por capas**, **adaptadores**, **pytest** y **logging estructurado**, lo cual apunta a una base correcta de ingeniería backend.
- En “Cómo trabajo” aparecen prácticas sanas (rollback, supuestos, operabilidad).

### Lo que falta para demostrar profundidad real
- Se menciona arquitectura, pero **casi no hay evidencia verificable** (volumen, latencia, throughput, incidentes, restricciones reales, decisiones con coste).
- No se ve **diseño de dominio concreto**: no hay agregados, invariantes, entidades/VO, reglas críticas ni ejemplos de modelado.
- No hay señales sólidas de **concurrencia**, **aislamiento transaccional**, **idempotencia**, **consistencia eventual**, **reintentos**, **DLQ**, etc.
- No hay detalle de **errores/edge cases de producción**: tipos de fallos, estrategia de recuperación, observabilidad operativa.
- El stack proyecta más **automatización + datos + desktop/CLI** que backend web productivo (faltan APIs HTTP, auth, contratos, versionado, despliegue de servicios).

## 2) Proyectos

### Diagnóstico
- Se presentan explícitamente como **“aprendizaje práctico”**: eso baja seniority percibido.
- Buen formato (contexto/problema/decisión/resultado/aprendizaje), pero los “resultados” son cualitativos y sin pruebas duras.
- No aparecen trade-offs exigentes (por qué A y no B bajo restricciones de coste/tiempo/fiabilidad).
- Escalabilidad poco demostrada: hay organización de código, pero no señales de presión real (concurrencia, colas, lock contention, límites DB, backpressure).

### Conclusión sobre proyectos
- Están bien para **Mid técnico ordenado**.
- No alcanzan por sí solos “Senior backend” sin evidencia de operación en producción o decisiones difíciles con impacto medible.

## 3) Señales negativas / red flags

- **Claim fuerte con evidencia débil**: “arquitectura limpia” aparece mucho, pero faltan artefactos/ejemplos concretos.
- **Backend web poco visible**: no se ven Django/FastAPI/DRF, contratos API, auth, caching, despliegue de servicios, ni observabilidad de APIs.
- **Sesgo a tooling interno** (ETL, BI, CLI/desktop). Útil, pero distinto de backend de producto web a escala.
- **Métricas ausentes**: sin antes/después (errores, tiempo de proceso, MTTR, incidencias, coste infra).

## 4) Nivel proyectado

**Nivel proyectado actual: Mid / Mid+ (más cerca de Mid+ en data/automatización que en backend web puro).**

### Por qué
- A favor: criterio arquitectónico básico, intención de testing, y foco en mantenibilidad/operabilidad.
- En contra para Senior: falta evidencia de sistemas backend web en producción, decisiones bajo carga/incidentes, y profundidad en fiabilidad transaccional y escalado.

## 5) Qué necesitaría ver para considerarlo sólido backend

## Cambios concretos en el CV
1. Reescribe 3-4 bullets de experiencia con formato **Problema → Decisión → Trade-off → Métrica**.
2. Añade una sección “**Producción y fiabilidad**” con:
   - manejo de errores (timeouts, retries, circuit breaker),
   - estrategia transaccional (atomicidad, idempotencia),
   - observabilidad (logs, métricas, trazas).
3. Si apuntas a Python/Django, incluye explícitamente:
   - API design (REST/DRF),
   - auth/autorización,
   - migraciones, índices, tuning SQL,
   - tests de integración/contrato.
4. Cambia “proyecto de aprendizaje” por “**sistema con decisiones de ingeniería**” cuando haya evidencia.

## Cambios en proyectos
- Publica 1 proyecto “ancla” backend web real (Django/DRF o FastAPI) con:
  - modelo de dominio explícito,
  - API versionada,
  - persistencia transaccional,
  - tareas asíncronas,
  - observabilidad,
  - batería de tests (unit + integración + contrato),
  - README con ADRs y postmortem corto de un fallo real/simulado.

## Señales de producción real que subirían tu nivel
- Métricas concretas (p95/p99, error rate, throughput, tiempo de batch, reducción de incidencias).
- Evidencia de decisiones difíciles (consistencia vs latencia, coste vs rendimiento, simplificación vs flexibilidad).
- Ejemplo de incidente: detección, mitigación, RCA y acción preventiva.

## 6) Veredicto final

### ¿Te pasaría a entrevista técnica?
**Sí, pero con reservas, para calibrar profundidad real.**

### Condición para pasar con más confianza
Necesitas que el CV deje de sonar a “arquitectura bien intencionada” y pase a “ingeniería backend demostrada” con evidencia dura: métricas, incidentes, transacciones, concurrencia y API web real.

## 10 preguntas si pasas a entrevista
1. Cuéntame una decisión arquitectónica donde sacrificaras flexibilidad para ganar simplicidad operativa. ¿Qué coste asumiste?
2. ¿Cómo modelarías en Django una operación crítica que debe ser idempotente y transaccional?
3. Describe un incidente real (o muy plausible) por datos corruptos/race condition. ¿Cómo lo detectaste y evitaste recurrencia?
4. ¿Cuándo usarías consistencia eventual frente a consistencia fuerte en un backend Python?
5. ¿Qué estrategia de retries aplicarías ante fallos intermitentes sin duplicar efectos secundarios?
6. Enséñame cómo diseñarías tests de contrato para una integración externa inestable.
7. ¿Qué métricas y alertas mínimas pondrías en una API para detectar degradación antes de que impacte al usuario?
8. ¿Cómo decidirías entre Celery, cron y procesamiento síncrono para un caso de negocio concreto?
9. Dame un ejemplo de optimización SQL real: problema inicial, hipótesis, cambio (índice/query), resultado.
10. Si mañana el tráfico sube x10, ¿qué cuello de botella atacarías primero y por qué?
