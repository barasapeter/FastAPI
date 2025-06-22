from fastapi import FastAPI
from web import explorer
from web import creature


app: FastAPI = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
