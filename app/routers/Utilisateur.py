from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.Utilisateur import UtilisateurRead, UtilisateurCreate, UtilisateurUpdate
from app.crud.Utilisateur import (
    get_utilisateurs,
    get_utilisateur,
    create_utilisateur,
    update_utilisateur,
    delete_utilisateur,
)
from app.database import get_async_session

router = APIRouter()

@router.get("/utilisateurs", response_model=List[UtilisateurRead])
async def read_utilisateurs(db: AsyncSession = Depends(get_async_session)):
    return await get_utilisateurs(db)

@router.get("/utilisateurs/{utilisateur_id}", response_model=UtilisateurRead)
async def read_utilisateur(utilisateur_id: int, db: AsyncSession = Depends(get_async_session)):
    utilisateur = await get_utilisateur(db, utilisateur_id)
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

@router.post("/utilisateurs", response_model=UtilisateurRead, status_code=status.HTTP_201_CREATED)
async def create_new_utilisateur(utilisateur_data: UtilisateurCreate, db: AsyncSession = Depends(get_async_session)):
    utilisateur_dict = utilisateur_data.dict()
    utilisateur = await create_utilisateur(db, utilisateur_dict)
    return utilisateur

@router.put("/utilisateurs/{utilisateur_id}", response_model=UtilisateurRead)
async def update_existing_utilisateur(utilisateur_id: int, update_data: UtilisateurUpdate, db: AsyncSession = Depends(get_async_session)):
    utilisateur = await update_utilisateur(db, utilisateur_id, update_data.dict(exclude_unset=True))
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

@router.delete("/utilisateurs/{utilisateur_id}", response_model=UtilisateurRead)
async def delete_existing_utilisateur(utilisateur_id: int, db: AsyncSession = Depends(get_async_session)):
    utilisateur = await delete_utilisateur(db, utilisateur_id)
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur
