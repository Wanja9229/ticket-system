from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

from app.config import settings
from app.core.exceptions import CustomException
from app.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Exception handler
@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.code,
        content={"detail": exc.message}
    )


# Include routers
from app.api.auth import super_admin, event_manager
from app.api.super_admin import events as super_admin_events
from app.api.event_manager import products as event_manager_products
from app.api.public import events as public_events

# Auth routers
app.include_router(
    super_admin.router,
    prefix="/api/auth/super-admin",
    tags=["Super Admin Auth"]
)
app.include_router(
    event_manager.router,
    prefix="/api/auth/event-manager",
    tags=["Event Manager Auth"]
)

# Super Admin routers
app.include_router(
    super_admin_events.router,
    prefix="/api/super-admin/events",
    tags=["Super Admin - Events"]
)

# Event Manager routers
app.include_router(
    event_manager_products.router,
    prefix="/api/event-manager/products",
    tags=["Event Manager - Products"]
)

# Public routers
app.include_router(
    public_events.router,
    prefix="/api/public/events",
    tags=["Public - Events"]
)


@app.get("/")
async def root():
    return {
        "message": "Ticket System API",
        "version": settings.VERSION,
        "docs": "/docs" if settings.DEBUG else "Disabled"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}