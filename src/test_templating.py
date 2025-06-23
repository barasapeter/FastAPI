from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

import os

print("DIRECTORY: ", os.getcwd())


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {"request": request, "message": "Hello from FastAPI!"}
    return templates.TemplateResponse("index.html", context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("test_templating:app", reload=True)
