from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Sistema de Gestión Hospitalaria")

# Incluir las rutas
app.include_router(router, prefix="/api")