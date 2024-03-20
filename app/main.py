from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def get():
    return {"message" : "Hello world."}