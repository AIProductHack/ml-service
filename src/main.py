import uvicorn
from fastapi import FastAPI
from src.api import generation

app = FastAPI()

app.include_router(generation.router)


@app.get("/")
def root():
    return {200: "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
