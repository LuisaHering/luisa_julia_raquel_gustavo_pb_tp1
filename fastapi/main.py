from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.health import health_router
from routes.predict import predict_router


app = FastAPI(
    title="Customer Support API"
)

app.include_router(auth_router)
app.include_router(health_router)
app.include_router(predict_router)