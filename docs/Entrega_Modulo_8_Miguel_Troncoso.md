# Portafolio Digital — Miguel Troncoso

## Evaluación Módulo 8: Desarrollo de portafolio de un producto digital

- **Proyecto / Etapa:** Portafolio profesional y preparación para el mercado laboral IT
- **Estudiante:** Miguel Troncoso
- **Email:** miguel.troncoso36@gmail.com
- **GitHub:** <https://github.com/MiguelTroncoso>
- **LinkedIn:** <https://www.linkedin.com/in/miguel-troncoso/>
- **Portafolio en línea:** <https://migueltroncoso.github.io/modulo_8/>
- **Documento PDF:** [`Portafolio_Modulo_8_Miguel_Troncoso.pdf`](Portafolio_Modulo_8_Miguel_Troncoso.pdf)

---

## Resumen ejecutivo

Este documento reúne los entregables de la evaluación del Módulo 8. Primero presento la
investigación de una empresa real del sector tecnológico (**Fintual**) y las formas concretas en que
podría aportar valor a su equipo. Luego presento mi **portafolio de proyectos** y desarrollo un
**caso de estudio técnico** sobre Alke Wallet, el proyecto más desafiante de mi formación.
Finalmente, incluyo la **matriz FODA** como análisis personal del PLUS.

---

## 1. Investigación de empresa: Fintual

Seleccioné a Fintual porque es una empresa real del ecosistema tecnológico chileno donde me gustaría
trabajar: es una fintech que usa **Python** de forma intensiva, resuelve problemas de datos
financieros y comparte el enfoque de producto simple y transparente que me motiva.

| Dimensión | Qué me atrae y por qué |
| :--- | :--- |
| **Valores y propósito** | Democratizar la inversión con productos **simples, transparentes y de bajo costo**, promoviendo el ahorro de largo plazo por sobre la especulación. |
| **Tipo de productos** | Fondos mutuos, ahorro automático, APV y herramientas de planificación, empaquetados en una experiencia digital fácil de usar. |
| **Tecnologías** | **Python** como lenguaje central, bases de datos relacionales, servicios en la nube (AWS) y un fuerte trabajo de datos e integraciones financieras. |
| **Metodologías de trabajo** | Equipos pequeños y autónomos, iteraciones cortas, revisión de código y automatización: el mismo enfoque que apliqué en mis proyectos. |
| **Enfoque en innovación** | Pioneros en fondos indexados de bajo costo en Chile y en automatizar decisiones financieras complejas a partir de datos. |

### 1.1 Tres formas concretas en que aportaría valor

1. **Desarrollo backend en Python/Django:** construir y mantener funcionalidades con modelos de
   datos claros, migraciones ordenadas y validaciones robustas, tal como lo hice en Alke Wallet.
2. **Calidad e integridad de datos:** aportar testing automatizado y revisión de casos borde, un
   aspecto crítico en productos financieros regulados.
3. **Documentación y comunicación técnica:** transformar decisiones y procesos en documentación
   clara y reutilizable, una responsabilidad explícita del puesto.

### 1.2 Tres preguntas para el reclutador

1. ¿Cómo se organizan los equipos de producto y cuánto *ownership* tiene un perfil junior sobre el
   ciclo completo, desde la implementación hasta el despliegue?
2. ¿Qué estrategia de *testing* y control de calidad utilizan en un producto financiero regulado?
3. ¿Cómo es el proceso de *onboarding* y mentoría para perfiles junior, y qué se espera de mí en
   los primeros tres meses?

---

## 2. Portafolio de proyectos

El portafolio está publicado en **<https://migueltroncoso.github.io/modulo_8/>** y reúne tres
productos digitales desarrollados durante el curso. Cada uno resuelve una problemática distinta y
fue documentado, versionado con Git y probado.

| Proyecto | Módulo | Problema que resuelve | Stack | Resultado |
| :--- | :---: | :--- | :--- | :--- |
| **Alke Wallet** | 7 | Billetera digital: clientes, cuentas y transacciones con saldos consistentes. | Python, Django, SQLite/PostgreSQL | 36/36 tests y 6 consultas personalizadas. |
| **TaskMaster** | 6 | Gestión de proyectos y tareas con acceso aislado por usuario. | Python, Django, Bootstrap | 18 tests y dashboard con KPIs. |
| **ClickAndGo** | 5 | E-commerce de consola con persistencia y valor del dólar. | Python, SQLite, POO, Flask | Guion P01–P19 y despliegue en VPS. |

### 2.1 Información de contacto del portafolio

- **Email:** miguel.troncoso36@gmail.com
- **GitHub:** <https://github.com/MiguelTroncoso>
- **LinkedIn:** <https://www.linkedin.com/in/miguel-troncoso/>
- **Ubicación:** Santiago, Chile · disponible para trabajo remoto.

---

## 3. Caso de estudio: Alke Wallet

> **Integridad financiera con el ORM de Django.** Proyecto elegido por ser el más representativo de
> mi crecimiento técnico durante el curso.

### 3.1 Descripción de la actividad

Desarrollar una billetera digital en Django que permita administrar **clientes, cuentas y
transacciones** (depósitos, retiros y transferencias), con un modelo de datos relacional,
operaciones CRUD completas, panel administrativo y consultas personalizadas al ORM.

### 3.2 Desafío principal

Garantizar que el saldo **nunca quedara inconsistente**: validar retiros sin fondos, impedir
transferencias hacia la misma cuenta y asegurar que dos operaciones simultáneas no corrompieran el
saldo, todo dentro de un modelo con relaciones uno a uno, uno a muchos y muchos a muchos.

### 3.3 Solución propuesta

- Lógica de saldo dentro de una **transacción atómica** con bloqueo pesimista (`select_for_update`).
- **Validaciones de negocio** en el modelo y refuerzo en el guardado para el uso directo del ORM.
- **Recálculo de saldos** y reversa automática al eliminar un movimiento.
- **CRUD con vistas basadas en clases** protegidas por autenticación y formularios con token CSRF.
- **Suite de pruebas** que cubre modelos, relaciones, reglas de negocio y vistas.

### 3.4 Herramienta técnica utilizada

Python 3.14 y Django 6.1 como *stack* principal; SQLite para desarrollo y PostgreSQL para producción;
Bootstrap 5 en la interfaz; Git y GitHub para el versionado; Django TestCase para las pruebas y
Playwright para generar las evidencias visuales.

### 3.5 Principales aprendizajes

- Modelar relaciones complejas y traducirlas a migraciones versionadas.
- Usar transacciones y bloqueos para proteger la integridad de los datos.
- Escribir pruebas que documentan el comportamiento esperado del sistema.
- Separar validación de formularios, lógica de modelo y presentación.

### 3.6 Métricas de impacto

| Métrica | Valor |
| :--- | :--- |
| Pruebas automatizadas aprobadas en Alke Wallet | **36 / 36** |
| Tipos de relación implementados (1:1, 1:N, M:N) | **3** |
| Consultas personalizadas (ORM, `raw()` y cursores) | **6** |
| Cobertura del CRUD con vistas basadas en clases | **100 %** |
| Regresiones de saldo detectadas en la suite | **0** |

### 3.7 Habilidades técnicas aplicadas

Python · Django ORM · SQL y PostgreSQL · Modelado de datos · Transacciones y concurrencia · Testing
automatizado · Seguridad CSRF · Git · Documentación técnica.

### 3.8 Justificación de la elección

Elegí este proyecto porque fue donde más crecí técnicamente: pasé de escribir consultas simples a
razonar sobre integridad, concurrencia y calidad de datos. Es el mejor ejemplo del tipo de problema
backend que quiero resolver profesionalmente y el que mejor demuestra mis habilidades actuales.

---

## 4. Matriz FODA (PLUS)

### Fortalezas (interno)

1. Modelado de datos y lógica de negocio con ORM.
2. CRUD, autenticación y administración en Django.
3. Testing automatizado (54 pruebas aprobadas en el portafolio).
4. Git, documentación técnica y buenas prácticas.
5. Aprendizaje autónomo y resolución de problemas.

### Oportunidades de mejora (interno)

1. Construir APIs REST con Django REST Framework.
2. Profundizar JavaScript y un framework de frontend.
3. Incorporar Docker y pipelines de CI/CD.
4. Subir el inglés técnico a nivel intermedio.
5. Desplegar en la nube (AWS) con buenas prácticas.

### Amenazas (externo)

1. Alta competencia entre perfiles junior en tecnología.
2. Ofertas que exigen experiencia previa.
3. Evolución acelerada de las herramientas y frameworks.
4. Automatización con IA que redefine tareas básicas.
5. Contexto económico que enfría las contrataciones.

### Oportunidades (externo)

1. Alta demanda de perfiles Python, Django y datos.
2. Digitalización de pymes y servicios públicos.
3. Fintech y retail que necesitan datos e integraciones.
4. Trabajo remoto que amplía el mercado a LatAm.
5. Programas de talento junior en empresas tecnológicas.

---

## 5. Calidad del producto y cierre

Antes de publicar el portafolio revisé los productos aplicando criterios de funcionalidad, usabilidad,
rendimiento, seguridad y escalabilidad, e incorporé mejoras a partir de la revisión del propio código.

| Criterio | Estado |
| :--- | :--- |
| ✅ Producto funcional | Los tres proyectos ejecutan y pasan sus pruebas automatizadas. |
| ✅ Feedback incorporado | Se ajustaron diseño, textos y navegación del portafolio. |
| ✅ Documentación mínima | Cada repositorio incluye README, informe y capturas de evidencia. |
| ✅ Presentación preparada | Este documento resume empresa, portafolio, caso de estudio y FODA. |

### Próximos pasos

- Publicar una API REST de Alke Wallet con Django REST Framework.
- Contenerizar los proyectos con Docker e integrar las pruebas en CI/CD.
- Grabar un video demo del caso de estudio para YouTube como respaldo del portafolio.

### Conclusión

Este portafolio demuestra que puedo llevar un producto digital desde el modelo de datos hasta la
interfaz, cuidando la integridad de la información y respaldando cada decisión con pruebas y
documentación. Busco mi primera oportunidad como desarrollador junior para seguir creciendo sobre
esta base y aportar valor a un equipo de producto.

---

*Gracias por tu tiempo. Quedo disponible para una entrevista.*

**Miguel Troncoso** · miguel.troncoso36@gmail.com · <https://migueltroncoso.github.io/modulo_8/>
