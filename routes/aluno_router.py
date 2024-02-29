from typing import List
from fastapi import APIRouter, HTTPException

from models.Aluno import Aluno

lista_alunos = [
    Aluno(id=1, nome="João"),
    Aluno(id=12, nome="Maria"),
    Aluno(id=13, nome="José"),
    Aluno(id=14, nome="Ana"),
    Aluno(id=15, nome="Carlos"),
    Aluno(id=16, nome="Mariana"),
    Aluno(id=17, nome="Pedro"),
    Aluno(id=18, nome="Paula"),
    Aluno(id=19, nome="Lucas"),
    Aluno(id=20, nome="Luana"),
]

router = APIRouter()


@router.get(
    "/",
    tags=["alunos"],
    status_code=200,
    description="Listar todos os alunos",
    summary="Listar alunos",
    response_model=List[Aluno]
)
async def listar_alunos():

    print(lista_alunos)

    if lista_alunos.count == 0:
        raise HTTPException(status_code=204, detail="Nenhum aluno encontrado")

    return lista_alunos


@router.get(
    "/{aluno_id}",
    tags=["alunos"],
    status_code=200,
    description="Buscar aluno por ID",
    summary="Buscar aluno",
    response_model=None,
)
async def buscar_aluno(aluno_id: int):
    for aluno in lista_alunos:
        if aluno["id"] == aluno_id:
            return aluno

    raise HTTPException(status_code=404, detail="Aluno não encontrado")


@router.post(
    "/",
    tags=["alunos"],
    status_code=201,
    description="Cadastrar aluno",
    summary="Cadastrar aluno",
)
async def cadastrar_aluno(nome: str):
    aluno = {"id": len(lista_alunos) + 1, "nome": nome}
    lista_alunos.append(aluno)
    return aluno


@router.put("/{aluno_id}", tags=["alunos"], status_code=204)
async def atualizar_aluno(aluno_id: int, nome: str):
    for aluno in lista_alunos:
        if aluno["id"] == aluno_id:
            aluno["nome"] = nome
            break

    raise HTTPException(status_code=404, detail="Aluno não encontrado")
