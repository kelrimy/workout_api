# workout_api/centro_treinamento/schemas.py

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: str = Field(description='Nome do centro de treinamento', example='CT A', max_length=50)


class CentroTreinamentoOut(BaseSchema):
    nome: str = Field(description='Nome do centro de treinamento', example='CT A', max_length=50)
