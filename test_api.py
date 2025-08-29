import asyncio
import httpx

BASE_URL = "http://localhost:8000"

async def main():
    async with httpx.AsyncClient() as client:
        print("1️⃣ Teste: Criar usuário válido")
        response = await client.post(
            f"{BASE_URL}/users",
            params={"name": "Carlos", "email": "carlos@example.com"}
        )
        assert response.status_code == 200, response.text
        user = response.json()
        print("Usuário criado:", user)
        user_id = user["id"]

        print("\n2️⃣ Teste: Criar usuário com email duplicado (deve falhar)")
        response = await client.post(
            f"{BASE_URL}/users",
            params={"name": "Outro Carlos", "email": "carlos@example.com"}
        )
        assert response.status_code == 400, "Email duplicado não retornou erro"
        print("Erro corretamente detectado:", response.json())

        print("\n3️⃣ Teste: Listar usuários")
        response = await client.get(f"{BASE_URL}/users")
        users = response.json()
        assert len(users) >= 1, "Lista de usuários vazia"
        print("Usuários:", users)

        print("\n4️⃣ Teste: Atualizar usuário com email válido")
        response = await client.put(
            f"{BASE_URL}/users/{user_id}",
            params={"name": "Carlos Alberto", "email": "carlos.alberto@example.com"}
        )
        updated_user = response.json()
        assert updated_user["email"] == "carlos.alberto@example.com"
        print("Usuário atualizado:", updated_user)

        print("\n5️⃣ Teste: Atualizar usuário com email duplicado (deve falhar)")
        # Primeiro cria outro usuário
        response2 = await client.post(
            f"{BASE_URL}/users",
            params={"name": "Maria", "email": "maria@example.com"}
        )
        maria_id = response2.json()["id"]

        response = await client.put(
            f"{BASE_URL}/users/{maria_id}",
            params={"email": "carlos.alberto@example.com"}
        )
        assert response.status_code == 400
        print("Erro corretamente detectado ao tentar atualizar para email duplicado:", response.json())

        print("\n6️⃣ Teste: Deletar usuário")
        response = await client.delete(f"{BASE_URL}/users/{user_id}")
        assert response.status_code == 200
        print("Usuário deletado:", response.json())

        print("\n7️⃣ Teste: Deletar usuário inexistente (deve falhar)")
        response = await client.delete(f"{BASE_URL}/users/999999")
        assert response.status_code == 404
        print("Erro corretamente detectado:", response.json())

        print("\n✅ Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    asyncio.run(main())
