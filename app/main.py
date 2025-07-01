from fastapi import FastAPI
from app.database import engine, Base, test_connection
from app.routers import Utilisateur
app = FastAPI()

app.include_router(Utilisateur.router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await test_connection()
