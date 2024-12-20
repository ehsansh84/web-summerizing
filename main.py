from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from bs4 import BeautifulSoup
from tools import get_contents, summarizer

app = FastAPI()

# Mount templates folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/fetch-content/", response_class=HTMLResponse)
async def fetch_content(request: Request, url: str = Form(...)):
    try:
        # Fetch the webpage content
        extracted_text = summarizer(get_contents(url))

    except Exception as e:
        extracted_text = f"Error fetching the URL: {e}"

    return templates.TemplateResponse("index.html", {"request": request, "content": extracted_text})
