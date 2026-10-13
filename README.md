# 💼 Portafolio Digital — Miguel Troncoso

### Evaluación Módulo 8: Desarrollo de portafolio de un producto digital

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-121013?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

---

## 🔗 Portafolio en línea

**<https://migueltroncoso.github.io/modulo_8/>**

Sitio estático publicado con **GitHub Pages**. Reúne el perfil profesional, los proyectos
del curso, el caso de estudio técnico, la investigación de empresa y la matriz FODA.

📄 **Documento de entrega (PDF):** [`docs/Portafolio_Modulo_8_Miguel_Troncoso.pdf`](docs/Portafolio_Modulo_8_Miguel_Troncoso.pdf)

---

## 📌 Descripción

Este repositorio contiene el **portafolio digital** desarrollado para la evaluación del Módulo 8.
El objetivo es mostrar de forma clara y atractiva una experiencia técnica concreta: quién soy, qué
sé hacer, cómo lo hago y por qué puedo aportar valor a un equipo de tecnología.

El portafolio se construyó como un **producto digital propio** (sitio web responsive hecho con
HTML, CSS y JavaScript, sin dependencias de build) y se complementa con un **documento PDF** que
contiene la investigación de empresa, el caso de estudio y el análisis FODA.

---

## 📋 Matriz de cumplimiento de la consigna

| Requerimiento oficial | Entregable | Estado |
| :--- | :--- | :---: |
| **1. Investigación de empresa** | Sección *Empresa* del sitio + sección 1 del PDF: Fintual analizada en valores, productos, tecnologías, metodologías e innovación (tabla). | ✅ |
| **3 formas de aportar valor** | Tres aportes concretos (backend Python/Django, calidad de datos y documentación técnica). | ✅ |
| **3 preguntas para el reclutador** | Tres preguntas incluidas en el sitio y en el PDF. | ✅ |
| **2. Portafolio con mínimo 3 proyectos** | Alke Wallet (M7), TaskMaster (M6) y ClickAndGo (M5), con descripción, stack, resultados y enlaces. | ✅ |
| **Información personal de contacto** | Email, GitHub, LinkedIn y ubicación en la sección *Contacto*. | ✅ |
| **Caso de estudio** | Sección *Caso de estudio*: descripción, desafío, solución, herramienta, aprendizajes, métricas, habilidades y justificación. | ✅ |
| **3. PLUS: Matriz FODA** | 5 fortalezas, 5 oportunidades de mejora, 5 amenazas y 5 oportunidades de mercado. | ✅ |
| **Entregable en PDF** | `docs/Portafolio_Modulo_8_Miguel_Troncoso.pdf` con portada, investigación y enlace al portafolio. | ✅ |
| **Calidad técnica y comunicacional** | Diseño responsive, accesibilidad, navegación, documentación y evidencias visuales. | ✅ |

---

## 🧭 Contenido del sitio

| Sección | Contenido |
| :--- | :--- |
| **Inicio** | Presentación, rol, propuesta de valor y accesos rápidos (CV/PDF, GitHub, LinkedIn, email). |
| **Sobre mí** | Perfil profesional, enfoque de trabajo y trayectoria por módulos del curso. |
| **Habilidades** | Lenguajes, frameworks, bases de datos y herramientas/prácticas. |
| **Proyectos** | Alke Wallet, TaskMaster y ClickAndGo con capturas, stack y enlaces. |
| **Caso de estudio** | Alke Wallet: integridad financiera con el ORM de Django (8 puntos exigidos). |
| **Empresa** | Investigación de Fintual: tabla de análisis, aportes de valor y preguntas para el reclutador. |
| **FODA** | Matriz personal 2x2 con cinco elementos por cuadrante. |
| **Contacto** | Correo, GitHub, LinkedIn y disponibilidad. |

---

## 🧪 Caso de estudio (resumen)

**Alke Wallet — integridad financiera con el ORM de Django**

- **Desafío:** evitar saldos inconsistentes ante retiros sin fondos, transferencias inválidas u
  operaciones concurrentes, en un modelo con relaciones 1:1, 1:N y M:N.
- **Solución:** actualización de saldo en transacción atómica con `select_for_update`, validaciones
  de negocio en el modelo, reversa de movimientos y CRUD con vistas basadas en clases.
- **Métricas:** 36/36 pruebas aprobadas, 3 tipos de relación, 6 consultas personalizadas y 100 % del
  CRUD cubierto.
- **Repositorio:** <https://github.com/MiguelTroncoso/modulo_7>

---

## 🗂️ Proyectos incluidos

| Proyecto | Módulo | Descripción | Repositorio / demo |
| :--- | :---: | :--- | :--- |
| **Alke Wallet** | 7 | Billetera digital en Django con ORM, migraciones, CRUD y 36 tests. | [modulo_7](https://github.com/MiguelTroncoso/modulo_7) |
| **TaskMaster** | 6 | Plataforma de proyectos y tareas con autenticación y dashboard. | [Modulo_6](https://github.com/MiguelTroncoso/Modulo_6) |
| **ClickAndGo** | 5 | E-commerce de consola con SQLite, arquitectura por capas y guion P01–P19. | [Demo en vivo](https://inacap.superflash.site) |

---

## 📁 Estructura del repositorio

```
modulo_8/
├── index.html                       # Sitio del portafolio (una sola página)
├── .nojekyll                        # Evita el procesamiento Jekyll en GitHub Pages
├── assets/
│   ├── css/styles.css               # Estilos, tema oscuro y diseño responsive
│   ├── js/main.js                   # Navegación, animaciones y progreso de scroll
│   └── img/                         # Capturas de proyectos, avatar y favicon
├── docs/
│   ├── Portafolio_Modulo_8_Miguel_Troncoso.pdf   # Documento de entrega (8 páginas)
│   ├── Entrega_Modulo_8_Miguel_Troncoso.md       # Versión Markdown del documento
│   └── screenshots/                 # Capturas del sitio (desktop y móvil)
├── tools/
│   ├── build_portfolio_pdf.py       # Genera el PDF de entrega con reportlab
│   └── capture_portfolio.py         # Genera las capturas del sitio con Playwright
└── README.md
```

---

## ▶️ Ejecución local

El sitio es 100 % estático: basta con servirlo con cualquier servidor HTTP.

```bash
# Clonar el repositorio
git clone https://github.com/MiguelTroncoso/modulo_8.git
cd modulo_8

# Levantar un servidor local
python3 -m http.server 8000
# Abrir http://127.0.0.1:8000
```

### Regenerar el PDF y las capturas (opcional)

```bash
# PDF de entrega (requiere reportlab)
python3 tools/build_portfolio_pdf.py

# Capturas del sitio (requiere playwright + Chrome)
python3 tools/capture_portfolio.py
```

---

## ✅ Calidad y cierre del producto

- **Funcionalidad:** navegación, enlaces y descarga del PDF verificados en desktop y móvil.
- **Usabilidad:** estructura por secciones, menú móvil, foco visible y `skip-link` accesible.
- **Rendimiento:** sin dependencias de build, imágenes optimizadas y carga diferida (`loading="lazy"`).
- **SEO / metadatos:** `title`, `description`, Open Graph, favicon y `lang="es"`.
- **Documentación:** README, informe en Markdown y capturas de evidencia.

---

## 👨‍💻 Autor

- **Miguel Troncoso**
- Email: [miguel.troncoso36@gmail.com](mailto:miguel.troncoso36@gmail.com)
- GitHub: [@MiguelTroncoso](https://github.com/MiguelTroncoso)
- LinkedIn: [linkedin.com/in/miguel-troncoso](https://www.linkedin.com/in/miguel-troncoso/)
- Portafolio: <https://migueltroncoso.github.io/modulo_8/>
- Evaluación: **Módulo 8 — Desarrollo de portafolio de un producto digital**
