from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.get_model import download_model
from core.logger import Logger
from config.init_config import load_model_paths

logger = Logger("webui")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

TOML_PATH = "config/paths.toml"
init_config = load_model_paths(TOML_PATH)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# To run the webui, run the following command:
# uvicorn webui:app --reload
