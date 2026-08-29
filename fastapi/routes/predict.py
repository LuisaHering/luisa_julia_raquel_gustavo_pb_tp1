from fastapi import APIRouter, Depends

from models.schemas import PredictRequest, PredictResponse
from security.jwt import validar_token_jwt


predict_router = APIRouter()


@predict_router.post("/predict", response_model=PredictResponse)
async def predict(
    data: PredictRequest,
    username: str = Depends(validar_token_jwt)
):
    texto = data.text.lower()

    if "reembolso" in texto:
        intent = "refund"
    else:
        intent = "general_support"

    return {"intent": intent}