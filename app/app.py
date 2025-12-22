from fastapi import FastAPI

app = FastAPI()

message = "Hello world!"

@app.get("/hello-world")
def hello_world():
    return message