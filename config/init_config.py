from pydantic import BaseModel
import toml


class ModelPaths(BaseModel):
    name: str
    url: str
    path: str


def load_model_paths(path: str) -> ModelPaths:
    config_toml = toml.load(path)["model"]
    return ModelPaths(**config_toml)
