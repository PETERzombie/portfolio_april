from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/drawing", response_class=HTMLResponse)
async def read_drawing(request: Request):
    return templates.TemplateResponse("drawing.html", {"request": request})

@app.get("/painting", response_class=HTMLResponse)
async def read_painting(request: Request):
    return templates.TemplateResponse("painting.html", {"request": request})

@app.get("/photography", response_class=HTMLResponse)
async def read_photography(request: Request):
    return templates.TemplateResponse("photography.html", {"request": request})

@app.get("/webdev", response_class=HTMLResponse)
async def read_webdev(request: Request):
    return templates.TemplateResponse("webdev.html", {"request": request})