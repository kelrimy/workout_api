# workout_api/categorias/schemas.py

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: str = Field(description='Nome da categoria', example='Categoria A', max_length=50)


class CategoriaOut(BaseSchema):
    nome: str = Field(description='Nome da categoria', example='Categoria A', max_length=50)
