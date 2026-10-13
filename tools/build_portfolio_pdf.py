"""Genera el documento PDF de entrega del Módulo 8 (Portafolio Digital).

Uso (con el runtime que incluye reportlab):
    python tools/build_portfolio_pdf.py

Salida: docs/Portafolio_Modulo_8_Miguel_Troncoso.pdf
"""

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RAIZ, "docs")
IMG = os.path.join(RAIZ, "assets", "img")
SALIDA = os.path.join(DOCS, "Portafolio_Modulo_8_Miguel_Troncoso.pdf")

# ---------------------------------------------------------------- paleta
INK = colors.HexColor("#0b1120")
INK_2 = colors.HexColor("#16233c")
ACCENT = colors.HexColor("#0f9d76")
ACCENT_2 = colors.HexColor("#2f6fd6")
WARN = colors.HexColor("#c8860d")
DANGER = colors.HexColor("#c0483f")
BODY = colors.HexColor("#1f2a37")
MUTED = colors.HexColor("#5b6b82")
LINE = colors.HexColor("#d7dee9")
SURFACE = colors.HexColor("#f2f5fa")

PORTFOLIO_URL = "https://migueltroncoso.github.io/modulo_8/"
GITHUB = "https://github.com/MiguelTroncoso"
LINKEDIN = "https://www.linkedin.com/in/miguel-troncoso/"
EMAIL = "miguel.troncoso36@gmail.com"


# ---------------------------------------------------------------- estilos
def construir_estilos():
    base = getSampleStyleSheet()
    e = {}
    e["h1"] = ParagraphStyle(
        "h1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=19,
        leading=23, textColor=INK, spaceBefore=4, spaceAfter=8,
    )
    e["h2"] = ParagraphStyle(
        "h2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=12.5,
        leading=16, textColor=ACCENT_2, spaceBefore=14, spaceAfter=6,
    )
    e["body"] = ParagraphStyle(
        "body", parent=base["BodyText"], fontName="Helvetica", fontSize=10.2,
        leading=15.4, textColor=BODY, alignment=TA_JUSTIFY, spaceAfter=7,
    )
    e["lead"] = ParagraphStyle(
        "lead", parent=e["body"], fontSize=11, leading=16.5, textColor=MUTED,
    )
    e["leadleft"] = ParagraphStyle(
        "leadleft", parent=e["lead"], alignment=TA_LEFT,
    )
    e["small"] = ParagraphStyle(
        "small", parent=e["body"], fontSize=8.8, leading=12.6, textColor=MUTED,
        alignment=TA_LEFT,
    )
    e["bullet"] = ParagraphStyle(
        "bullet", parent=e["body"], fontSize=9.9, leading=14.4, spaceAfter=4,
        leftIndent=12, bulletIndent=2,
    )
    e["cell"] = ParagraphStyle(
        "cell", parent=e["body"], fontSize=9.3, leading=13.4, alignment=TA_LEFT, spaceAfter=0,
    )
    e["cellb"] = ParagraphStyle(
        "cellb", parent=e["cell"], fontName="Helvetica-Bold", textColor=INK,
    )
    e["cellh"] = ParagraphStyle(
        "cellh", parent=e["cell"], fontName="Helvetica-Bold", textColor=colors.white, fontSize=9.4,
    )
    e["metric"] = ParagraphStyle(
        "metric", parent=e["body"], fontName="Helvetica-Bold", fontSize=16,
        leading=19, textColor=ACCENT, alignment=TA_CENTER, spaceAfter=1,
    )
    e["metricc"] = ParagraphStyle(
        "metricc", parent=e["cell"], alignment=TA_CENTER, fontSize=8.4, textColor=MUTED,
    )
    return e


E = construir_estilos()


def p(texto, estilo="body"):
    return Paragraph(texto, E[estilo])


def vineta(texto):
    return Paragraph(texto, E["bullet"], bulletText="\u2022")


# ---------------------------------------------------------------- portada
def dibujar_portada(canvas, doc):
    ancho, alto = A4
    canvas.saveState()

    canvas.setFillColor(INK)
    canvas.rect(0, 0, ancho, alto, stroke=0, fill=1)

    # Bandas decorativas
    canvas.setFillColor(ACCENT)
    canvas.rect(0, alto - 14, ancho, 14, stroke=0, fill=1)
    canvas.setFillColor(ACCENT_2)
    canvas.rect(0, alto - 20, ancho * 0.4, 6, stroke=0, fill=1)

    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(48, alto - 96, "PORTAFOLIO DIGITAL")
    canvas.setFillColor(colors.HexColor("#9aa8c0"))
    canvas.setFont("Helvetica", 10)
    canvas.drawString(48, alto - 114, "Modulo 8 - Desarrollo de portafolio de un producto digital")

    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 40)
    canvas.drawString(48, alto - 190, "Miguel Troncoso")

    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 15)
    canvas.drawString(48, alto - 220, "Desarrollador Web Junior  |  Python - Django - SQL")

    canvas.setStrokeColor(colors.HexColor("#2a3a56"))
    canvas.setLineWidth(1)
    canvas.line(48, alto - 244, ancho - 48, alto - 244)

    canvas.setFillColor(colors.HexColor("#c4d0e4"))
    canvas.setFont("Helvetica", 11.5)
    lineas = [
        "Portafolio de proyectos desarrollados durante la formacion intensiva en tecnologia,",
        "con investigacion de empresa, un caso de estudio tecnico y analisis FODA.",
    ]
    for i, linea in enumerate(lineas):
        canvas.drawString(48, alto - 274 - i * 18, linea)

    # Tarjeta de enlaces
    canvas.setFillColor(INK_2)
    canvas.roundRect(48, alto - 470, ancho - 96, 132, 12, stroke=0, fill=1)
    canvas.setFillColor(colors.HexColor("#9aa8c0"))
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(70, alto - 370, "PORTAFOLIO EN LINEA")
    canvas.drawString(70, alto - 408, "REPOSITORIO")
    canvas.drawString(70, alto - 446, "CONTACTO")

    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 11.5)
    canvas.drawString(220, alto - 370, PORTFOLIO_URL)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 11)
    canvas.drawString(220, alto - 408, GITHUB)
    canvas.setFont("Helvetica", 10)
    canvas.drawString(220, alto - 446, EMAIL + "   |   " + LINKEDIN)

    canvas.setFillColor(colors.HexColor("#6b7a92"))
    canvas.setFont("Helvetica", 9)
    canvas.drawString(48, 44, "Autor: Miguel Troncoso - Santiago, Chile - 2026")
    canvas.drawRightString(ancho - 48, 44, "Entrega de evaluacion - Modulo 8")

    # Vista previa del portafolio en linea
    ruta_hero = os.path.join(DOCS, "screenshots", "01_hero.png")
    if os.path.exists(ruta_hero):
        w = 430.0
        h = w * 900.0 / 1440.0
        x = (ancho - w) / 2.0
        y = 80.0
        canvas.setFillColor(colors.HexColor("#16233c"))
        canvas.roundRect(x - 9, y - 9, w + 18, h + 18, 12, stroke=0, fill=1)
        canvas.drawImage(ruta_hero, x, y, width=w, height=h, mask=None)

    canvas.restoreState()


def dibujar_pie(canvas, doc):
    ancho, alto = A4
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.7)
    canvas.line(48, 46, ancho - 48, 46)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(48, 34, "Miguel Troncoso - Portafolio Digital (Modulo 8)")
    canvas.drawRightString(ancho - 48, 34, "Pagina %d" % doc.page)
    canvas.restoreState()


# ---------------------------------------------------------------- bloques
def caja_metricas():
    datos = [
        [p("36/36", "metric"), p("3", "metric"), p("6", "metric"), p("54", "metric")],
        [
            p("Pruebas aprobadas<br/>en Alke Wallet", "metricc"),
            p("Tipos de relacion<br/>1:1, 1:N y M:N", "metricc"),
            p("Consultas<br/>personalizadas", "metricc"),
            p("Pruebas en todo<br/>el portafolio", "metricc"),
        ],
    ]
    tabla = Table(datos, colWidths=[(A4[0] - 96) / 4.0] * 4)
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SURFACE),
        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.7, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    return tabla


def tabla_empresa():
    filas = [
        [p("Dimension", "cellh"), p("Que me atrae y por que", "cellh")],
        [p("Valores y proposito", "cellb"),
         p("Democratizar la inversion con productos simples, transparentes y de bajo costo, "
           "promoviendo el ahorro de largo plazo por sobre la especulacion.", "cell")],
        [p("Tipo de productos", "cellb"),
         p("Fondos mutuos, ahorro automatico, APV y herramientas de planificacion, "
           "empaquetados en una experiencia digital simple de usar.", "cell")],
        [p("Tecnologias", "cellb"),
         p("Python como lenguaje central, bases de datos relacionales, servicios en la nube "
           "(AWS) y un fuerte trabajo de datos e integraciones financieras.", "cell")],
        [p("Metodologias", "cellb"),
         p("Equipos pequenos y autonomos, iteraciones cortas, revision de codigo y "
           "automatizacion: el mismo enfoque que aplique en mis proyectos.", "cell")],
        [p("Innovacion", "cellb"),
         p("Pioneros en fondos indexados de bajo costo en Chile y en automatizar decisiones "
           "financieras complejas a partir de datos.", "cell")],
    ]
    tabla = Table(filas, colWidths=[105, A4[0] - 96 - 105])
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK_2),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, SURFACE]),
        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.7, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    return tabla


def tabla_proyectos():
    filas = [
        [p("Proyecto", "cellh"), p("Mod.", "cellh"), p("Problema que resuelve", "cellh"),
         p("Stack", "cellh"), p("Resultado", "cellh")],
        [p("Alke Wallet", "cellb"), p("7", "cell"),
         p("Billetera digital: clientes, cuentas y transacciones con saldos consistentes.", "cell"),
         p("Python, Django, SQLite/PostgreSQL", "cell"),
         p("36/36 tests, 6 consultas personalizadas.", "cell")],
        [p("TaskMaster", "cellb"), p("6", "cell"),
         p("Gestion de proyectos y tareas con acceso aislado por usuario.", "cell"),
         p("Python, Django, Bootstrap", "cell"),
         p("18 tests, dashboard con KPIs.", "cell")],
        [p("ClickAndGo", "cellb"), p("5", "cell"),
         p("E-commerce de consola con persistencia y valor del dolar.", "cell"),
         p("Python, SQLite, POO, Flask", "cell"),
         p("Guion P01-P19 y despliegue en VPS.", "cell")],
    ]
    tabla = Table(filas, colWidths=[80, 40, 182, 105, 92])
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK_2),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, SURFACE]),
        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.7, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ]))
    return tabla


def celda_foda(titulo, color, elementos):
    contenido = [Paragraph(titulo, ParagraphStyle(
        "fodaH", parent=E["cellb"], fontSize=10.5, textColor=color, spaceAfter=5))]
    for el in elementos:
        contenido.append(Paragraph(el, ParagraphStyle(
            "fodaB", parent=E["cell"], fontSize=8.9, leading=12.4,
            leftIndent=9, bulletIndent=0, spaceAfter=2), bulletText="\u2022"))
    return contenido


def tabla_foda():
    fortalezas = [
        "Modelado de datos y logica de negocio con ORM.",
        "CRUD, autenticacion y admin en Django.",
        "Testing automatizado (54 pruebas aprobadas).",
        "Git, documentacion tecnica y buenas practicas.",
        "Aprendizaje autonomo y resolucion de problemas.",
    ]
    mejoras = [
        "Construir APIs REST con Django REST Framework.",
        "Profundizar JavaScript y un framework de frontend.",
        "Incorporar Docker y pipelines de CI/CD.",
        "Subir el ingles tecnico a nivel intermedio.",
        "Desplegar en la nube (AWS) con buenas practicas.",
    ]
    amenazas = [
        "Alta competencia entre perfiles junior.",
        "Ofertas que exigen experiencia previa.",
        "Evolucion acelerada de frameworks.",
        "Automatizacion con IA de tareas basicas.",
        "Contexto economico que enfria las contrataciones.",
    ]
    oportunidades = [
        "Alta demanda de perfiles Python, Django y datos.",
        "Digitalizacion de pymes y servicios publicos.",
        "Fintech y retail que necesitan datos e integraciones.",
        "Trabajo remoto que amplia el mercado a LatAm.",
        "Programas de talento junior en empresas tech.",
    ]
    datos = [
        [celda_foda("Fortalezas", ACCENT, fortalezas), celda_foda("Oportunidades de mejora", WARN, mejoras)],
        [celda_foda("Amenazas del mercado", DANGER, amenazas), celda_foda("Oportunidades del mercado", ACCENT_2, oportunidades)],
    ]
    tabla = Table(datos, colWidths=[(A4[0] - 96) / 2.0] * 2)
    tabla.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.8, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#eefaf5")),
        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#fdf6e9")),
        ("BACKGROUND", (0, 1), (0, 1), colors.HexColor("#fdeeec")),
        ("BACKGROUND", (1, 1), (1, 1), colors.HexColor("#eef3fd")),
    ]))
    return tabla


def imagen(archivo, ancho_max, alto_max=None):
    ruta = os.path.join(IMG, archivo)
    from reportlab.lib.utils import ImageReader
    iw, ih = ImageReader(ruta).getSize()
    alto = ancho_max * ih / iw
    if alto_max and alto > alto_max:
        alto = alto_max
        ancho_max = alto * iw / ih
    return Image(ruta, width=ancho_max, height=alto)


def imagen_centrada(archivo, ancho_max, alto_max=None):
    """Envuelve la imagen en una tabla para centrarla horizontalmente."""
    img = imagen(archivo, ancho_max, alto_max)
    tabla = Table([[img]], colWidths=[A4[0] - 96])
    tabla.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return tabla


# ---------------------------------------------------------------- documento
def construir():
    os.makedirs(DOCS, exist_ok=True)
    doc = SimpleDocTemplate(
        SALIDA, pagesize=A4,
        leftMargin=48, rightMargin=48, topMargin=56, bottomMargin=56,
        title="Portafolio Digital - Miguel Troncoso (Modulo 8)",
        author="Miguel Troncoso",
        subject="Evaluacion Modulo 8 - Desarrollo de portafolio de un producto digital",
    )

    story = [PageBreak()]  # la portada se dibuja con el canvas
    ancho_util = A4[0] - 96

    # ---------- Indice y resumen ----------
    story.append(p("Contenido", "h1"))
    indice = [
        ("1", "Investigacion de empresa: Fintual"),
        ("2", "Portafolio de proyectos"),
        ("3", "Caso de estudio: integridad financiera con el ORM de Django"),
        ("4", "Matriz FODA (PLUS)"),
        ("5", "Calidad del producto y cierre"),
    ]
    filas = [[p(n, "cellb"), p(t, "cell")] for n, t in indice]
    t = Table(filas, colWidths=[26, ancho_util - 26])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, LINE),
    ]))
    story.append(t)
    story.append(Spacer(1, 16))

    story.append(p("Resumen ejecutivo", "h2"))
    story.append(p(
        "Este documento reune los entregables de la evaluacion del Modulo 8. Primero presento la "
        "investigacion de una empresa real del sector tecnologico (Fintual) y las formas concretas "
        "en que podria aportar valor a su equipo. Luego presento mi portafolio de proyectos y "
        "desarrollo un caso de estudio tecnico sobre Alke Wallet, el proyecto mas desafiante de mi "
        "formacion. Finalmente, incluyo la matriz FODA como analisis personal del PLUS. El "
        "portafolio esta publicado y puede visitarse en el enlace indicado en la portada."))

    story.append(p("El portafolio en linea", "h2"))
    story.append(p(
        "El portafolio profesional esta publicado con GitHub Pages y reune la informacion de "
        "contacto, los tres proyectos, el caso de estudio y el analisis FODA en formato navegable: "
        "<b>%s</b>. Los repositorios de cada proyecto estan enlazados desde el mismo sitio." % PORTFOLIO_URL))
    story.append(Spacer(1, 6))
    story.append(caja_metricas())
    story.append(Spacer(1, 16))
    story.append(p("Perfil profesional", "h2"))
    story.append(p(
        "Desarrollador web junior con foco en backend. Trabajo con Python y Django construyendo "
        "aplicaciones completas: modelo de datos, logica de negocio, interfaz con plantillas y "
        "pruebas automatizadas. Me interesa especialmente la integridad de los datos y la "
        "documentacion clara de cada decision tecnica."))
    story.append(vineta("<b>Backend:</b> Python 3, Django 6, ORM, vistas basadas en clases, "
                        "autenticacion y panel de administracion."))
    story.append(vineta("<b>Datos:</b> SQL relacional, SQLite, PostgreSQL, migraciones y consultas "
                        "avanzadas (annotate, aggregate, raw y cursores)."))
    story.append(vineta("<b>Frontend:</b> HTML5, CSS3, Bootstrap 5 y plantillas Django (DTL)."))
    story.append(vineta("<b>Calidad:</b> Git y GitHub, testing automatizado y documentacion tecnica."))
    story.append(PageBreak())

    # ---------- 1. Empresa ----------
    story.append(p("1. Investigacion de empresa: Fintual", "h1"))
    story.append(p(
        "Seleccione a Fintual porque es una empresa real del ecosistema tecnologico chileno donde "
        "me gustaria trabajar: es una fintech que usa Python de forma intensiva, resuelve problemas "
        "de datos financieros y comparte el enfoque de producto simple y transparente que me motiva. "
        "La siguiente tabla resume, desde una perspectiva tecnica, que es lo que mas me atrae de la "
        "organizacion.", "lead"))
    story.append(Spacer(1, 6))
    story.append(tabla_empresa())

    story.append(p("3 formas concretas en que podria aportar valor", "h2"))
    story.append(vineta(
        "<b>Desarrollo backend en Python/Django:</b> construir y mantener funcionalidades con "
        "modelos de datos claros, migraciones ordenadas y validaciones robustas, tal como lo hice "
        "en Alke Wallet."))
    story.append(vineta(
        "<b>Calidad e integridad de datos:</b> aportar testing automatizado y revision de casos "
        "borde, un aspecto critico en productos financieros regulados."))
    story.append(vineta(
        "<b>Documentacion y comunicacion tecnica:</b> transformar decisiones y procesos en "
        "documentacion clara y reutilizable, una responsabilidad explicita del puesto."))

    story.append(p("3 preguntas para el reclutador", "h2"))
    story.append(vineta(
        "Como se organizan los equipos de producto y cuanto ownership tiene un perfil junior "
        "sobre el ciclo completo, desde la implementacion hasta el despliegue?"))
    story.append(vineta(
        "Que estrategia de testing y control de calidad utilizan en un producto financiero "
        "regulado?"))
    story.append(vineta(
        "Como es el proceso de onboarding y mentoria para perfiles junior, y que se espera de mi "
        "en los primeros tres meses?"))
    story.append(PageBreak())

    # ---------- 2. Portafolio ----------
    story.append(p("2. Portafolio de proyectos", "h1"))
    story.append(p(
        "Tres productos digitales desarrollados durante el curso, documentados, versionados con Git "
        "y probados. El detalle completo, con capturas y enlaces, esta en <b>%s</b>."
        % PORTFOLIO_URL,
        "leadleft"))
    story.append(Spacer(1, 8))
    story.append(tabla_proyectos())
    story.append(Spacer(1, 14))

    ancho_img = (ancho_util - 12) / 2.0
    fila_imgs = Table(
        [[imagen("alke-dashboard.png", ancho_img), imagen("taskmaster-dashboard.png", ancho_img)]],
        colWidths=[ancho_img, ancho_img],
    )
    fila_imgs.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 12),
    ]))
    story.append(fila_imgs)
    story.append(Spacer(1, 6))
    story.append(p(
        "Izquierda: panel de control de Alke Wallet (Modulo 7). "
        "Derecha: dashboard de TaskMaster (Modulo 6).", "small"))
    story.append(Spacer(1, 12))
    story.append(KeepTogether([imagen_centrada("clickandgo-diagrama.png", 250)]))
    story.append(PageBreak())

    # ---------- 3. Caso de estudio ----------
    story.append(p("3. Caso de estudio: Alke Wallet", "h1"))
    story.append(p(
        "Integridad financiera con el ORM de Django. Proyecto elegido por ser el mas representativo "
        "de mi crecimiento tecnico durante el curso.", "lead"))

    story.append(p("3.1 Descripcion de la actividad", "h2"))
    story.append(p(
        "Desarrollar una billetera digital en Django que permita administrar clientes, cuentas y "
        "transacciones (depositos, retiros y transferencias), con un modelo de datos relacional, "
        "operaciones CRUD completas, panel administrativo y consultas personalizadas al ORM."))

    story.append(p("3.2 Desafio principal", "h2"))
    story.append(p(
        "Garantizar que el saldo nunca quedara inconsistente: validar retiros sin fondos, impedir "
        "transferencias hacia la misma cuenta y asegurar que dos operaciones simultaneas no "
        "corrompieran el saldo, todo dentro de un modelo con relaciones uno a uno, uno a muchos y "
        "muchos a muchos."))

    story.append(p("3.3 Solucion propuesta", "h2"))
    story.append(vineta("Logica de saldo dentro de una transaccion atomica con bloqueo pesimista "
                        "(<font face='Courier'>select_for_update</font>)."))
    story.append(vineta("Validaciones de negocio en el modelo y refuerzo en el guardado para el "
                        "uso directo del ORM."))
    story.append(vineta("Recalculo de saldos y reversa automatica al eliminar un movimiento."))
    story.append(vineta("CRUD con vistas basadas en clases protegidas por autenticacion y "
                        "formularios con token CSRF."))
    story.append(vineta("Suite de pruebas que cubre modelos, relaciones, reglas de negocio y vistas."))

    story.append(p("3.4 Herramienta tecnica utilizada", "h2"))
    story.append(p(
        "Python 3.14 y Django 6.1 como stack principal; SQLite para desarrollo y PostgreSQL para "
        "produccion; Bootstrap 5 en la interfaz; Git y GitHub para el versionado; Django TestCase "
        "para las pruebas y Playwright para generar las evidencias visuales."))

    story.append(p("3.5 Principales aprendizajes", "h2"))
    story.append(vineta("Modelar relaciones complejas y traducirlas a migraciones versionadas."))
    story.append(vineta("Usar transacciones y bloqueos para proteger la integridad de los datos."))
    story.append(vineta("Escribir pruebas que documentan el comportamiento esperado del sistema."))
    story.append(vineta("Separar validacion de formularios, logica de modelo y presentacion."))

    story.append(p("3.6 Metricas de impacto", "h2"))
    story.append(caja_metricas())

    story.append(Spacer(1, 12))
    story.append(p("3.7 Habilidades tecnicas aplicadas", "h2"))
    story.append(p(
        "Python - Django ORM - SQL y PostgreSQL - Modelado de datos - Transacciones y concurrencia "
        "- Testing automatizado - Seguridad CSRF - Git - Documentacion tecnica."))

    story.append(p("3.8 Justificacion de la eleccion", "h2"))
    story.append(p(
        "Elegi este proyecto porque fue donde mas creci tecnicamente: pase de escribir consultas "
        "simples a razonar sobre integridad, concurrencia y calidad de datos. Es el mejor ejemplo "
        "del tipo de problema backend que quiero resolver profesionalmente y el que mejor demuestra "
        "mis habilidades actuales."))
    story.append(Spacer(1, 10))
    story.append(imagen_centrada("alke-consultas.png", ancho_util, alto_max=380))
    story.append(Spacer(1, 6))
    story.append(p(
        "Evidencia: vista de consultas personalizadas de Alke Wallet (ORM, SQL con raw() y "
        "cursores).", "small"))
    story.append(PageBreak())

    # ---------- 4. FODA ----------
    story.append(p("4. Matriz FODA (PLUS)", "h1"))
    story.append(p(
        "Analisis personal del punto de partida para insertarme en el mercado laboral IT, con cinco "
        "elementos en cada cuadrante.", "lead"))
    story.append(Spacer(1, 10))
    story.append(tabla_foda())
    story.append(Spacer(1, 14))
    story.append(p(
        "Conclusion del analisis: mis fortalezas se concentran en el backend y la calidad de datos, "
        "y mis mayores oportunidades de mejora estan en ampliar el stack hacia APIs, frontend, "
        "contenedores y nube. Las amenazas del mercado se compensan focalizando la busqueda en "
        "empresas que valoran perfiles junior con evidencia concreta de proyectos.", "body"))
    story.append(PageBreak())

    # ---------- 5. Calidad y cierre ----------
    story.append(p("5. Calidad del producto y cierre", "h1"))
    story.append(p(
        "Antes de publicar el portafolio revise los productos aplicando criterios de funcionalidad, "
        "usabilidad, rendimiento, seguridad y escalabilidad, e incorpore mejoras a partir de la "
        "revision del propio codigo.", "lead"))
    checklist = [
        ("Producto funcional", "Los tres proyectos ejecutan y pasan sus pruebas automatizadas."),
        ("Feedback incorporado", "Se ajustaron detalles de diseno, textos y navegacion del portafolio."),
        ("Documentacion minima", "Cada repositorio incluye README, informe y capturas de evidencia."),
        ("Presentacion preparada", "Este documento resume empresa, portafolio, caso de estudio y FODA."),
    ]
    filas = [[p(chk, "cellb"), p(desc, "cell")] for chk, desc in checklist]
    t = Table(filas, colWidths=[150, ancho_util - 150])
    t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, SURFACE]),
        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.7, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    story.append(t)

    story.append(p("Proximos pasos", "h2"))
    story.append(vineta("Publicar una API REST de Alke Wallet con Django REST Framework."))
    story.append(vineta("Contenerizar los proyectos con Docker e integrar pruebas en CI/CD."))
    story.append(vineta("Grabar un video demo del caso de estudio para YouTube como respaldo."))

    story.append(p("Conclusion", "h2"))
    story.append(p(
        "Este portafolio demuestra que puedo llevar un producto digital desde el modelo de datos "
        "hasta la interfaz, cuidando la integridad de la informacion y respaldando cada decision "
        "con pruebas y documentacion. Busco mi primera oportunidad como desarrollador junior para "
        "seguir creciendo sobre esta base y aportar valor a un equipo de producto."))
    story.append(Spacer(1, 18))
    story.append(p("Gracias por tu tiempo. Quedo disponible para una entrevista.", "lead"))
    story.append(Spacer(1, 6))
    story.append(p("Miguel Troncoso - " + EMAIL + " - " + PORTFOLIO_URL, "small"))

    doc.build(story, onFirstPage=dibujar_portada, onLaterPages=dibujar_pie)
    return SALIDA


if __name__ == "__main__":
    ruta = construir()
    print("PDF generado:", ruta)
