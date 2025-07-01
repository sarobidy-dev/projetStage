from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import text
from app.config import DATABASE_URL  # Vérifie que ta variable est bien configurée

# Crée l'engine asynchrone
engine = create_async_engine(DATABASE_URL, echo=True)

# Base déclarative SQLAlchemy
Base = declarative_base()

# Session async avec sessionmaker
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Générateur de session à utiliser dans FastAPI avec Depends()
async def get_async_session():
    async with async_session() as session:
        yield session

# Fonction pour tester la connexion
async def test_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            print("✅ Base de données connectée avec succès.")
    except Exception as e:
        print("❌ Échec de connexion à la base de données :", e)
