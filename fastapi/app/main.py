from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from pydantic import BaseModel

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version="0.0.1",
    openapi_tags=settings.tags_metadata,
)

origins = ["http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputText(BaseModel):
    content: str


class WordCount(BaseModel):
    word_count: int


@app.get("/", include_in_schema=False)
def root():
    """
    Default endpoint

    Returns:
        JSON: Message to point users to visit /docs url for SwaggerUI interface.
    """
    return {
        "message": "Please visit host_ip:port/docs to view SwaggerUI interface. (http://127.0.0.1:8000/docs for local)"
    }


@app.post("/wordcount/", tags=["WordCounter"])
def count_words(text: InputText) -> WordCount:
    """
    Count number of words in a text.

    Args:
        text (InputText): Input text to count words from.

    Returns:
        WordCount: Number of words in the input text.
    """
    return WordCount(word_count=len(text.content.split()))


def use_route_names_as_operation_ids(my_app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function names.
    Should be called only after all routes have been added to the app.
    """
    for route in my_app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)
