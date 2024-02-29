from pydantic import BaseModel


class Aluno(BaseModel):
    id: int
    nome: str