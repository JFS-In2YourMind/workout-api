from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate

from app.database import get_async_session
from app.models import Atleta
from app.schemas import AtletaCreate, AtletaOut

router = APIRouter(prefix="/atletas", tags=["Atletas"])

@router.post("/", response_model=AtletaOut)
async def criar_atleta(
    atleta: AtletaCreate,
    session: AsyncSession = Depends(get_async_session)
):
    novo_atleta = Atleta(**atleta.dict())

    session.add(novo_atleta)
    try:
        await session.commit()
        await session.refresh(novo_atleta)
        return novo_atleta
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )

@router.get("/", response_model=Page[AtletaOut])
async def listar_atletas(
    nome: str = Query(None),
    cpf: str = Query(None),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Atleta)

    if nome:
        query = query.where(Atleta.nome.ilike(f"%{nome}%"))

    if cpf:
        query = query.where(Atleta.cpf == cpf)

    result = await session.execute(query)
    atletas = result.scalars().all()
    return paginate(atletas)
