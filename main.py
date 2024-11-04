from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")
app.mount("/img",StaticFiles(directory="img"),name="img")

templates = Jinja2Templates(directory="templates")

@app.get("/Home/", response_class = HTMLResponse)
def index(request: Request):
  context = {'request':request}
  return templates.TemplateResponse("index.html",context)

@app.get("/Home/hours", response_class=HTMLResponse)  # Remove .html extension
def hours(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("hours.html", context)

@app.get("/Home/contact", response_class=HTMLResponse)  # Remove .html extension
def contact(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("contact.html", context)