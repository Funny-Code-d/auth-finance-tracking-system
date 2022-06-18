
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from db.base import database
from endpoints import token




tags_metadata = [
    {
        "name" : "token",
        "description" : "В данном разделе реализован функционал работы с токеном: создание, рефреш, удаление."
    },
]


app = FastAPI(
    title="Авторизация в информационой системе контроля личных расходов (API)",
    version='1.0.0',
    openapi_tags=tags_metadata
)



app.include_router(token.route, prefix='/api/token', tags=['token'])

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <h1>REST API авторизации в информационной системе учёта расходов</h1>
    <p>Owner by Sosnin Denis</p>
    <p><a href='/docs/'>Docs</a></p>
    """

# @app.get("/api/{token}/users/")
# async def root(token: str):
#         return {
#         "message": "Hello World",
#         "token" : token
#         }

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8002, host='0.0.0.0', reload=True)