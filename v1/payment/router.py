from ninja import Router

router = Router()


@router.get("/")
async def payment_root(request):
    return {"message": "it works."}
