# API-CIFRA-VERNAM

# 🔐 Cifra de Vernam em Bits
**Integrante:** Paulo Bajona

---

## 🧠 Descrição
Este projeto implementa uma API para **criptografia e descriptografia de mensagens** utilizando a **Cifra de Vernam bit a bit**.
A criptografia funciona convertendo cada caractere da mensagem e da chave para **binário (8 bits)**, aplicando **XOR bit a bit** e retornando uma **string de 0 e 1**.
A descriptografia aplica novamente o XOR coma a mesma chave para recuperar o texto original.

---

## ⚙️ Tecnologias utilizadas
- **Python 3.x**
- **FastAPI** → Criação da API e geração automática da interface Swagger
- **Pydantic** → Validação de entrada de dados
- **Uvicorn** → Servidor da API

---

## 🚀 Como executar o projeto

1. **Instalar as dependências**
   ```
   pip install -r requirements.txt
   ```

   Conteúdo do `requirements.txt`:
   ```
   fastapi
   uvicorn
   pydantic
   ```

2. **Executar o servidor**
   ```
   uvicorn main:app --reload
   ```

3. **Acessar a interface Swagger**
   Abra no navegador:
   ```
   http://127.0.0.1:8000/docs
   ```
   Aqui você pode testar os endpoints de **criptografia** e **descriptografia** diretamente.

4. **Ou usar o Postman**
   - **Endpoint de criptografia:** `POST http://127.0.0.1:8000/encrypt`
   - **Endpoint de descriptografia:** `POST http://127.0.0.1:8000/decrypt`
   - Enviar requisições em **JSON**, conforme os exemplos abaixo.
