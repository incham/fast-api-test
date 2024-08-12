from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.item_service import ItemService

router = APIRouter()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return ItemService.get_item(item_id, q)

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return ItemService.update_item(item_id, item.name)
