from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello() -> str:
    return "hello, world"
