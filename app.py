from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return "Navigate games by adding '/number' to this web address eg. localhost:5000/01"

@app.get("/{id}", response_class=HTMLResponse)
async def first(request: Request, id:int):
    if id == 1:
        return templates.TemplateResponse("index01.html", context={"request": request})
    if id == 2:
        return templates.TemplateResponse("index02.html", context={"request": request})
    return RedirectResponse("/") 




