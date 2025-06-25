# 🧠 Sistema Inteligente de Gestión de Pacientes

Proyecto que integra tecnologías modernas para la gestión de pacientes, análisis clínico y asistencia inteligente en tiempo real mediante modelos de lenguaje.

## 🚀 Tecnologías utilizadas

- **FastAPI** – Backend rápido y ligero para la creación de APIs RESTful.
- **PostgreSQL** – Base de datos relacional robusta.
- **Triggers en PostgreSQL** – Cálculo automático del IMC al insertar/actualizar datos clínicos.
- **React.js + Bootstrap** – Interfaz moderna, responsiva y fácil de usar.
- **LangChain + LLM (RAG)** – Procesamiento de lenguaje natural con modelos preentrenados y recuperación aumentada de información.
- **Multiagentes** – Arquitectura de agentes especializados para procesamiento inteligente.
- **Análisis bioquímico R24** – Módulo de interpretación en tiempo real.

## 📦 Instalación

### Requisitos

- Python 3.10+
- Node.js 18+
- PostgreSQL
- `pip` y `npm` instalados

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/nombre_del_proyecto.git
cd nombre_del_proyecto
```

### 2. Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

## 🛠️ Estructura del proyecto

```
nombre_del_proyecto/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   └── routes/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   └── package.json
└── README.md
```

## ✨ Funcionalidades destacadas

- Registro y gestión de pacientes con validación de datos.
- Cálculo automático del IMC mediante triggers en PostgreSQL.
- Visualización de resultados bioquímicos R24 en tiempo real.
- Asistente IA con LangChain + LLM para preguntas clínicas.
- Interfaz gráfica React con operaciones CRUD completas.

## ✅ Casos de uso

1. Registro de nuevo paciente.
2. Carga de datos clínicos (peso, talla, bioquímicos).
3. Cálculo automático de IMC.
4. Consulta asistida por IA basada en el historial.
5. Visualización y edición de datos desde el panel administrativo.

## 🧪 Próximas mejoras

- Implementación de roles (nutricionista, médico, admin).
- Soporte para carga de PDF con extracción automática.
- Exportación de reportes clínicos.


