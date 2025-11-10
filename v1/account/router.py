from typing import Literal
from ninja import Router, Schema

router = Router()


class RootResponse(Schema):
    message: Literal["it works."]


@router.get("/", response=RootResponse)
async def account_root(request):
    return {"message": "it works."}
