from sqlalchemy import Column, Integer, String
from app.database import Base

class Utilisateur(Base):
    __tablename__ = "Utilisateur"

    id_utilisateur = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    mot_de_passe = Column(String(100), nullable=False)
