# workout_api/centro_treinamento/controller.py

from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from fastapi_pagination import Page, paginate

from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo centro de treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut
)
async def create_centro_treinamento(
    db_session: DatabaseDependency, 
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
):
    try:
        centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), created_at=datetime.utcnow(), **centro_treinamento_in.dict())
        centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.dict(exclude={'id'}))

        db_session.add(centro_treinamento_model)
        await db_session.commit()
    except IntegrityError as e:
        if 'already exists' in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_303_SEE_OTHER, 
                detail=f'Já existe um centro de treinamento cadastrado com o nome: {centro_treinamento_in.nome}'
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail='Ocorreu um erro ao inserir os dados no banco'
            )

    return centro_treinamento_out

@router.get(
    '/', 
    summary='Consultar todos os Centros de Treinamento',
    status_code=status.HTTP_200_OK,
    response_model=Page[CentroTreinamentoOut],
)
async def read_centros_treinamento(
    db_session: DatabaseDependency,
    limit: int = Query(default=10, description='Quantidade de registros por página'),
    offset: int = Query(default=0, description='Número de registros a serem ignorados no início'),
) -> Page[CentroTreinamentoOut]:
    query = select(CentroTreinamentoModel)
    centros_treinamento = await db_session.execute(query.offset(offset).limit(limit))
    return paginate(centros_treinamento, limit, offset)
