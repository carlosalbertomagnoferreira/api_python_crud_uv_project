import os
from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from models import Base, User

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://user:password@localhost:5432/meubanco"
)

# Cria engine assíncrona
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Factory para sessões assíncronas
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI(title="API de Usuários", version="1.0.0")


@app.get("/")
async def hello_world():
    return {"message": "Hello, Async World!"}


# ===== Listar todos os usuários =====
@app.get("/users")
async def get_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users


# ===== Criar novo usuário =====
@app.post("/users")
async def create_user(name: str, email: str):
    async with AsyncSessionLocal() as session:
        # Verifica se email já existe
        result = await session.execute(select(User).where(User.email == email))
        existing_user = result.scalar_one_or_none()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email já cadastrado")

        new_user = User(name=name, email=email)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


# ===== Atualizar usuário =====
@app.put("/users/{user_id}")
async def update_user(user_id: int, name: str = None, email: str = None):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        if name:
            user.name = name
        if email:
            # Verifica se email já está em uso
            result = await session.execute(select(User).where(User.email == email, User.id != user_id))
            existing_user = result.scalar_one_or_none()
            if existing_user:
                raise HTTPException(status_code=400, detail="Email já cadastrado")
            user.email = email

        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


# ===== Deletar usuário =====
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        await session.delete(user)
        await session.commit()
        return {"detail": "Usuário deletado com sucesso"}
