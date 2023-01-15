from fastapi import APIRouter

from pydantic import BaseModel

from .models import User as Entity


router = APIRouter(prefix="/users")


@router.get("/{uid}")
async def get(uid: int):
    entity = await Entity.get_or_404(uid)
    return entity.to_dict()


class CreateModel(BaseModel):
    name: str


@router.post("/")
async def add(entity: CreateModel):
    entity_created = await Entity.create(nickname=entity.name)
    return entity_created.to_dict()


@router.delete("/{uid}")
async def delete(uid: int):
    entity = await Entity.get_or_404(uid)
    await entity.delete()
    return dict(id=uid)
