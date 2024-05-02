from mylib.logic import wiki as wikilogic
from mylib.logic import search_wiki
from mylib.logic import phrase as wikiphrases

# print(wikilogic())

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """page to search in wikipedia"""
    result = search_wiki(value)
    return {"results": result}


@app.get("/wiki/{name}")
async def search(name: str):
    """To retreive wikipedia page"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """retrieve wikipedia page and return phrases"""
    result = wikiphrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
