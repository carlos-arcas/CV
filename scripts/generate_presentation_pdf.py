from __future__ import annotations

from pathlib import Path

from reportlab.graphics import renderSVG
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Folleto Automatizaciones-Web Carlos Arcas.pdf"
QR_SVG = ROOT / "assets" / "img" / "presentacion-qr.svg"
PORTFOLIO_URL = "https://carlos-arcas.github.io/CV/"

INK = HexColor("#10233F")
BLUE = HexColor("#155BD5")
BLUE_SOFT = HexColor("#EAF2FF")
CYAN = HexColor("#08A7C2")
TEAL = HexColor("#0B927F")
YELLOW = HexColor("#E5AE26")
DIFFERENTIAL_SURFACE = HexColor("#FFFAEC")
SURFACE = HexColor("#F5F8FC")
LINE = HexColor("#D7E1EC")
MUTED = HexColor("#52657B")


SERVICES = (
    ("01", "Informes automáticos", "Excel, CSV, PDF o Power BI con la frecuencia necesaria.", "Menos copiar, pegar y revisar."),
    ("02", "Excel y macros", "Archivos lentos o frágiles convertidos en procesos estables.", "Menos errores y mantenimiento."),
    ("03", "Herramientas internas", "Aplicaciones para registrar, validar y controlar tareas.", "Trabajo guiado y trazable."),
    ("04", "Datos y SQL", "Consultas, cruces y consolidación de fuentes dispersas.", "Información fiable y accesible."),
    ("05", "Paneles e indicadores", "Actividad, estados, incidencias y datos clave para decidir.", "Lo importante, visible."),
    ("06", "Alertas y controles", "Avisos y comprobaciones automáticas que detectan errores.", "Los problemas llegan antes."),
    ("07", "Tareas masivas", "Importar, transformar o procesar archivos y registros.", "Horas de trabajo en pocos pasos."),
    ("08", "Usuarios y permisos", "Roles, accesos, histórico de cambios y auditoría.", "Cada persona ve lo necesario."),
    ("09", "Webs profesionales", "Páginas personalizadas, rápidas y adaptadas a móvil.", "Una presencia digital propia."),
    ("10", "E-commerce", "Catálogo, clientes, pedidos, pagos y administración.", "Venta online preparada para crecer."),
    ("11", "Portales privados", "Zonas de clientes o empleados con seguimiento.", "Información centralizada."),
    ("12", "Integraciones", "Conexión entre archivos, bases de datos, APIs y apps.", "Menos trabajo duplicado."),
)


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))


def style(name: str, size: float, leading: float, color=INK, bold: bool = False) -> ParagraphStyle:
    return ParagraphStyle(
        name=name,
        fontName="Arial-Bold" if bold else "Arial",
        fontSize=size,
        leading=leading,
        textColor=color,
        alignment=TA_LEFT,
        spaceAfter=0,
        spaceBefore=0,
    )


def draw_paragraph(canvas: Canvas, text: str, x: float, y_top: float, width: float, paragraph_style: ParagraphStyle) -> float:
    paragraph = Paragraph(text, paragraph_style)
    _, height = paragraph.wrap(width, 1000)
    paragraph.drawOn(canvas, x, y_top - height)
    return height


def qr_drawing(size: float) -> Drawing:
    widget = QrCodeWidget(PORTFOLIO_URL)
    bounds = widget.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    drawing = Drawing(size, size, transform=[size / width, 0, 0, size / height, 0, 0])
    drawing.add(widget)
    return drawing


def draw_service_card(canvas: Canvas, x: float, y_top: float, width: float, height: float, service: tuple[str, str, str, str]) -> None:
    number, title, description, value = service
    is_differential = number in {"09", "10", "11", "12"}
    canvas.setFillColor(DIFFERENTIAL_SURFACE if is_differential else white)
    canvas.setStrokeColor(HexColor("#EAD8A4") if is_differential else LINE)
    canvas.roundRect(x, y_top - height, width, height, 1.3 * mm, fill=1, stroke=1)
    canvas.setFillColor(YELLOW if is_differential else CYAN)
    canvas.rect(x, y_top - height, 1.2 * mm, height, fill=1, stroke=0)
    canvas.setFillColor(HexColor("#936E0B") if is_differential else BLUE)
    canvas.setFont("Arial-Bold", 5.8)
    canvas.drawString(x + 4 * mm, y_top - 4.8 * mm, number)
    draw_paragraph(canvas, title, x + 4 * mm, y_top - 7 * mm, width - 8 * mm, style(f"title-{number}", 8.2, 9.2, INK, True))
    draw_paragraph(canvas, description, x + 4 * mm, y_top - 12.3 * mm, width - 8 * mm, style(f"body-{number}", 6.25, 7.4, MUTED))
    canvas.setFillColor(TEAL)
    canvas.setFont("Arial-Bold", 5.8)
    canvas.drawString(x + 4 * mm, y_top - height + 4 * mm, value)


def build_pdf() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    QR_SVG.parent.mkdir(parents=True, exist_ok=True)
    renderSVG.drawToFile(qr_drawing(120), str(QR_SVG))

    canvas = Canvas(str(OUTPUT), pagesize=A4)
    page_width, page_height = A4
    margin = 12 * mm
    content_width = page_width - 2 * margin
    canvas.setTitle("Carlos Arcas - Presentación para empresas")
    canvas.setAuthor("Carlos Arcas")
    canvas.setSubject("Automatización, herramientas internas y desarrollo web")

    top = page_height - 10 * mm
    canvas.setFillColor(BLUE)
    canvas.roundRect(margin, top - 10 * mm, 10 * mm, 10 * mm, 1.8 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Arial-Bold", 9)
    canvas.drawCentredString(margin + 5 * mm, top - 6.7 * mm, "CA")
    canvas.setFillColor(INK)
    canvas.setFont("Arial-Bold", 11.5)
    canvas.drawString(margin + 14 * mm, top - 3.8 * mm, "Carlos Arcas")
    canvas.setFillColor(MUTED)
    canvas.setFont("Arial", 7)
    canvas.drawString(margin + 14 * mm, top - 8.2 * mm, "Analista Programador · Automatización")
    canvas.setFont("Arial-Bold", 6.8)
    canvas.drawRightString(page_width - margin, top - 6 * mm, "SEVILLA · REMOTO")

    hero_top = top - 15 * mm
    hero_height = 42 * mm
    canvas.setFillColor(SURFACE)
    canvas.setStrokeColor(LINE)
    canvas.roundRect(margin, hero_top - hero_height, content_width, hero_height, 1.5 * mm, fill=1, stroke=1)
    canvas.setFillColor(BLUE)
    canvas.rect(margin, hero_top - hero_height, 2 * mm, hero_height, fill=1, stroke=0)
    canvas.setFillColor(BLUE)
    canvas.setFont("Arial-Bold", 6.5)
    canvas.drawString(margin + 7 * mm, hero_top - 7 * mm, "AUTOMATIZACIÓN PARA EMPRESAS")
    draw_paragraph(canvas, "Convierto procesos manuales en herramientas claras y fiables.", margin + 7 * mm, hero_top - 10.5 * mm, 105 * mm, style("hero", 19, 20.5, INK, True))
    draw_paragraph(canvas, "Automatizo informes, mejoro Excel complejos y creo aplicaciones internas para reducir pasos, errores y dependencia de una sola persona.", margin + 120 * mm, hero_top - 9 * mm, 57 * mm, style("hero-summary", 7.6, 10, MUTED))

    results_top = hero_top - hero_height - 4 * mm
    result_width = content_width / 3
    results = (("Menos tareas repetitivas", "Procesos automáticos y guiados"), ("Datos más fiables", "Validaciones y trazabilidad"), ("Más autonomía", "Herramientas mantenibles"))
    for index, (title, text) in enumerate(results):
        x = margin + index * result_width
        canvas.setFillColor(white)
        canvas.setStrokeColor(LINE)
        canvas.rect(x, results_top - 13 * mm, result_width, 13 * mm, fill=1, stroke=1)
        canvas.setFillColor(TEAL)
        canvas.setFont("Arial-Bold", 7)
        canvas.drawString(x + 5 * mm, results_top - 5.2 * mm, title)
        canvas.setFillColor(MUTED)
        canvas.setFont("Arial", 6.2)
        canvas.drawString(x + 5 * mm, results_top - 9.2 * mm, text)

    heading_y = results_top - 20 * mm
    canvas.setFillColor(BLUE)
    canvas.setFont("Arial-Bold", 6.3)
    canvas.drawString(margin, heading_y, "CAPACIDADES PARA NECESIDADES REALES")
    canvas.setFillColor(INK)
    canvas.setFont("Arial-Bold", 14)
    canvas.drawString(margin, heading_y - 6.5 * mm, "¿Qué puedo hacer por tu empresa?")

    cards_top = heading_y - 11 * mm
    gap = 3 * mm
    card_width = (content_width - 2 * gap) / 3
    card_height = 25.5 * mm
    row_gap = 2.5 * mm
    for index, service in enumerate(SERVICES):
        row, column = divmod(index, 3)
        x = margin + column * (card_width + gap)
        y_top = cards_top - row * (card_height + row_gap)
        draw_service_card(canvas, x, y_top, card_width, card_height, service)

    contact_y = 36 * mm
    contact_height = 35 * mm
    canvas.setFillColor(BLUE_SOFT)
    canvas.setStrokeColor(HexColor("#BCD0EC"))
    canvas.roundRect(margin, contact_y, content_width, contact_height, 1.5 * mm, fill=1, stroke=1)
    canvas.setFillColor(BLUE)
    canvas.rect(margin, contact_y + contact_height - 1.8 * mm, content_width, 1.8 * mm, fill=1, stroke=0)
    canvas.setFillColor(BLUE)
    canvas.setFont("Arial-Bold", 6)
    canvas.drawString(margin + 6 * mm, contact_y + 26 * mm, "PRIMER DIAGNÓSTICO")
    draw_paragraph(canvas, "Revisamos el problema y buscamos una solución proporcionada.", margin + 6 * mm, contact_y + 23 * mm, 105 * mm, style("contact", 11.2, 12.5, INK, True))
    canvas.setFillColor(MUTED)
    canvas.setFont("Arial", 6.2)
    canvas.drawString(margin + 6 * mm, contact_y + 8.2 * mm, "Para empezar: un ejemplo, los pasos actuales, el problema y el resultado esperado.")
    canvas.setFillColor(BLUE)
    canvas.setFont("Arial-Bold", 6.7)
    canvas.drawString(margin + 6 * mm, contact_y + 4 * mm, "carlos.arcas.alcala@gmail.com  ·  carlos-arcas.github.io/CV/")

    qr_size = 21 * mm
    qr_x = page_width - margin - qr_size - 5 * mm
    qr_y = contact_y + 9 * mm
    canvas.setFillColor(white)
    canvas.rect(qr_x - 1.5 * mm, qr_y - 7 * mm, qr_size + 3 * mm, qr_size + 9 * mm, fill=1, stroke=0)
    qr_drawing(qr_size).drawOn(canvas, qr_x, qr_y)
    canvas.setFillColor(INK)
    canvas.setFont("Arial-Bold", 5.2)
    canvas.drawCentredString(qr_x + qr_size / 2, qr_y - 2.5 * mm, "AMPLIAR")
    canvas.drawCentredString(qr_x + qr_size / 2, qr_y - 5 * mm, "INFORMACIÓN")

    canvas.setFillColor(MUTED)
    canvas.setFont("Arial", 5.8)
    canvas.drawString(margin, 10 * mm, "Carlos Arcas · Automatización, datos y desarrollo de soluciones")
    canvas.drawRightString(page_width - margin, 10 * mm, "Presentación profesional")
    canvas.save()


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
