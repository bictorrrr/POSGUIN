# POSGUIN

POSGUIN es un sistema de punto de venta en desarrollo. El proyecto combina un backend construido con [FastAPI](https://fastapi.tiangolo.com/) y un frontend en [React](https://react.dev/) con [Vite](https://vitejs.dev/).

## Instalación

### Requisitos
- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/) para la base de datos.
- [Python 3.13](https://www.python.org/) y [Poetry](https://python-poetry.org/) para el backend.
- [Node.js](https://nodejs.org/) (con npm) para el frontend.

### Clonar el repositorio
```bash
git clone <URL-del-repo>
cd POSGUIN
```

### Base de datos
Levanta PostgreSQL con Docker:
```bash
docker compose -f docker/docker-compose.yml up -d
```

### Backend
Instala dependencias y ejecuta el servidor de desarrollo:
```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

### Frontend
Instala dependencias y ejecuta la aplicación:
```bash
cd frontend
npm install
npm run dev
```

El backend expone endpoints de usuario básicos en `http://localhost:8000`, mientras que el frontend se ejecuta en `http://localhost:5173` por defecto.

