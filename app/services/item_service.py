from typing import Union

class ItemService:
    @staticmethod
    def get_item(item_id: int, q: Union[str, None] = None):
        # 여기에 비즈니스 로직이 들어갑니다
        return {"item_id": item_id, "q": q}

    @staticmethod
    def update_item(item_id: int, name: str):
        # 여기에 업데이트 로직이 들어갑니다
        return {"item_name": name, "item_id": item_id}
