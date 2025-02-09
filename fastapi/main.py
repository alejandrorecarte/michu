from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.lobbies import router as lobbies_router
from routers.users import router as users_router
import logging

app = FastAPI()

app.include_router(users_router, prefix="/user", tags=["Users"])
app.include_router(lobbies_router, prefix="/lobby", tags=["Lobbies"])

# Agregar middleware para CORS (Compartir recursos entre orígenes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Permitir solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Configuración del logger para registrar mensajes
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(name)s - %(asctime)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('fastapi.log')  # Guardar los logs en el archivo fastapi.log
    ]
)

# Crear un logger para esta aplicación
logger = logging.getLogger(__name__)

# Evento de inicio de la aplicación
@app.on_event("startup")
async def startup_event():
    """Evento que se ejecuta al iniciar la aplicación"""
    logger.info("Application started")

# Evento de cierre de la aplicación
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")