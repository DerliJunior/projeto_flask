import uvicorn
from fastapi import FastAPI
from routes import aluno_router


app = FastAPI(title="API de Alunos", version="0.0.1", description="Uma API Fast")

app.include_router(aluno_router.router, prefix="/api/v1/alunos", tags=["alunos"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
