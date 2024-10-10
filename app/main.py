from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Memoki API!"}

@app.get("/health")
async def health_check():
    return {"status": "OK", "message": "This service is healthy"}
