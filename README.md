# FastAPI

### O que é o FastAPI?

FastAPI é um moderno e rápido framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python. Oferece alta performance, é fácil de aprender e codar, e está pronto para produção.

### Async

Código assíncrono significa que a linguagem tem um modo de dizer para o computador/programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar.

# Projeto

## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI, criada para integrar duas paixões: desenvolvimento e treinamento. É uma API pequena, focada em demonstrar como utilizar o FastAPI de forma prática e simplificada.

## Modelagem de Entidade e Relacionamento - MER

![MER](/mer.jpg "Modelagem de Entidade e Relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), juntamente com as seguintes bibliotecas: `alembic`, `SQLAlchemy`, `pydantic`. Os dados são armazenados no PostgreSQL, utilizando Docker para a gestão do banco de dados.

## Execução da API

Para executar o projeto, recomenda-se usar `pyenv` com a versão 3.11.4 do Python para o ambiente virtual. Após instalar o `pyenv`, execute:

pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt

Para iniciar o banco de dados com Docker Compose:

make run-docker

Para criar uma nova migração:

make create-migrations d="nome_da_migration"

Para aplicar as migrações e criar o banco de dados:

make run-migrations

## API

Para iniciar a API, execute:

make run

Acesse a documentação da API em: http://127.0.0.1:8000/docs

## Desafio Final

- Adicionado query parameters nos endpoints:
- Atleta:
- nome
- cpf
- Customização do retorno dos endpoints:
- GET all Atleta:
- nome
- centro_treinamento
- categoria
- Manipulação de exceção de integridade dos dados em cada módulo/tabela:
- sqlalchemy.exc.IntegrityError: "Já existe um atleta cadastrado com o cpf: x"
- Status Code: 303
- Adição de paginação utilizando fastapi-pagination:
- limit e offset

## Referências

FastAPI: https://fastapi.tiangolo.com/
Pydantic: https://docs.pydantic.dev/latest/
SQLAlchemy: https://docs.sqlalchemy.org/en/20/
Alembic: https://alembic.sqlalchemy.org/en/latest/
Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/
