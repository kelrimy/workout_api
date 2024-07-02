# workout_api/categorias/controller.py

from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from fastapi_pagination import Page, paginate

from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar uma nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut
)
async def create_categoria(
    db_session: DatabaseDependency, 
    categoria_in: CategoriaIn = Body(...)
):
    try:
        categoria_out = CategoriaOut(id=uuid4(), created_at=datetime.utcnow(), **categoria_in.dict())
        categoria_model = CategoriaModel(**categoria_out.dict(exclude={'id'}))

        db_session.add(categoria_model)
        await db_session.commit()
    except IntegrityError as e:
        if 'already exists' in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_303_SEE_OTHER, 
                detail=f'Já existe uma categoria cadastrada com o nome: {categoria_in.nome}'
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail='Ocorreu um erro ao inserir os dados no banco'
            )

    return categoria_out

@router.get(
    '/', 
    summary='Consultar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=Page[CategoriaOut],
)
async def read_categorias(
    db_session: DatabaseDependency,
    limit: int = Query(default=10, description='Quantidade de registros por página'),
    offset: int = Query(default=0, description='Número de registros a serem ignorados no início'),
) -> Page[CategoriaOut]:
    query = select(CategoriaModel)
    categorias = await db_session.execute(query.offset(offset).limit(limit))
    return paginate(categorias, limit, offset)
