from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from utils.get_model import download_model
from core.logger import Logger
from config.init_config import load_model_paths
import time


logger = Logger("webui")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

TOML_PATH = "config/paths.toml"
init_config = load_model_paths(TOML_PATH)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict/")
async def predict(request: Request, text: str = Form(...)):
    # model_path = init_config["model_path"]
    # model = download_model(model_path)
    # sleep for 10 seconds to simulate a long running process
    time.sleep(10)
    result = "Dummy result " + text
    return {"result": result}


# To run the webui, run the following command:
# uvicorn webui:app --reload
