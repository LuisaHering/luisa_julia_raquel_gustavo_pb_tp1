from fastapi import APIRouter
from models.schemas import PredictRequest, PredictResponse

predict_router = APIRouter()

@predict_router.post("/predict", response_model=PredictResponse)
async def predict(data: PredictRequest):
    texto = data.text.lower()

    if "reembolso" in texto:
        intent = "refund"
    else:
        intent = "general_support"

    return {"intent": intent}