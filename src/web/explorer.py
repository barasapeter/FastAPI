from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

router: APIRouter = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> Explorer | None:
    return service.get_one(name)
