from fastapi import FastAPI
from app.routers import items

app = FastAPI()

# 기존 라우트
@app.get("/")
def read_root():
    return {"Hello": "World"}

# items 라우트 등록
app.include_router(items.router)
