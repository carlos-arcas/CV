# Web profesional de Carlos Arcas

Landing profesional estatica para GitHub Pages, construida con HTML y CSS sin framework.

## Objetivo

Presentar el perfil de Carlos Arcas como Analista Programador y Consultor de Automatizacion especializado en:

- automatizacion de informes,
- migracion de Excel/VBA a Python,
- SQL, Excel avanzado y Power BI,
- herramientas ejecutables para usuarios no tecnicos,
- IA generativa y agentes IA aplicados al desarrollo con supervision.

## Estructura

```text
.
├── index.html              # Pagina principal publicada por GitHub Pages
├── assets/
│   ├── css/
│   │   └── styles.css      # Estilos de la landing
│   └── img/
│       └── og-image.svg    # Imagen Open Graph / redes sociales
├── docs/
│   ├── context/            # Contexto y briefing de contenido
│   ├── audits/             # Auditorias y revisiones previas
│   └── CV_COPY_ESTRATEGICO.md
├── robots.txt
├── sitemap.xml
└── README.md
```

## Ver en local

Opcion rapida:

```bash
python -m http.server 8000
```

Luego abrir:

```text
http://localhost:8000
```

## Publicacion

El repo esta preparado para GitHub Pages con `Deploy from a branch`:

- Rama: `main`
- Carpeta: `/(root)`

`index.html` debe permanecer en la raiz para que GitHub Pages lo publique directamente.

## Exportar CV a PDF

La propia web incluye botones de descarga que lanzan la impresion del navegador.
Tambien puede hacerse manualmente con:

```text
Ctrl + P > Guardar como PDF
```
