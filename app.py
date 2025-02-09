from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, StreamingResponse

app = FastAPI()
static = StaticFiles(directory="static")
app.mount("/static/TemplateData", StaticFiles(directory="static/TemplateData", html=True), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return "Navigate games by adding a number after current url eg. localhost:5000/1"

@app.get("/{id}")
async def first(request: Request, response:Response, id:int):
    response.headers["Content-Encoding"] = "gzip"
    if id == 1:
        return templates.TemplateResponse("index01.html", context={"request": request})
    if id == 2:
        return templates.TemplateResponse("index02.html", context={"request": request})
    return RedirectResponse("/") 


# FastAPI ei osaa asettaa Content-Encoding otsaketta gzip tiedostoille
@app.get("/static/{folder}/{filename}", response_class=FileResponse)
async def first(request: Request, folder:str, filename:str):
    path, _ = static.lookup_path(f"{folder}/{filename}")
    if filename.endswith(".js"):
        return FileResponse(path, media_type="javascript/application")
    if filename.endswith(".wasm.gz"):
        file = open(path, "rb")
        return StreamingResponse(file, headers={"Content-Encoding": "gzip"}, media_type="application/wasm")
    if filename.endswith(".gz"):
        fileresponse = FileResponse(path)
        fileresponse.headers.append("content-encoding", "gzip")
        return fileresponse
