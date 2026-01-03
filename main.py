from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "RBX_BotFlagger API is Live", "status": "Ready"}
