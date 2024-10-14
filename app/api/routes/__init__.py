from ...core import app
from .accounts import Accounts

@app.get("/")
async def home():
    return {"message": "Welcome to the Memoki API!"}

routers = [
    Accounts().router,
]

for router in routers:
    app.include_router(router)
