from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from core.logger import Logger
from config.init_config import load_model_paths
from utils.pipeline import Pipeline


logger = Logger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

TOML_PATH = "config/paths.toml"
init_config = load_model_paths(TOML_PATH)
pipeline = Pipeline()


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict/")
async def predict(request: Request, text: str = Form(...)):
    result = pipeline.get_sentiment(text)
    return {"result": result}


# To run the webui, run the following command:
# uvicorn webui:app --reload
