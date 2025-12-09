from fastapi import FastAPI
from backend.api.employee_routes import router as employee_router
from backend.core.logging_config import logger

app = FastAPI(
    title="Employee Management System",
    description="API for managing employees, HR managers, and users",
    version="1.0.0"
)

app.include_router(employee_router)

logger.info("FastAPI application started")
