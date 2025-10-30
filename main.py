from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Cifra de Vernam em bits",
    description="API para criptografia e descriptografia usando a Cifra de Vernam bit a bit.",
    version="1.0.0"
)

class EncryptRequest(BaseModel):
    message: str
    key: str

class EncryptResponse(BaseModel):
    textoCifrado: str
    chave: str

class DecryptRequest(BaseModel):
    textoCifrado: str
    chave: str

class DecryptResponse(BaseModel):
    textoClaro: str

def text_to_bits(text: str) -> str:
    return ''.join(f'{ord(c):08b}' for c in text)

def bits_to_text(bits: str) -> str:
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def vernam_bits(message: str, key: str) -> str:
    if len(message) != len(key):
        raise ValueError("A chave deve ter o mesmo tamanho da mensagem")
    message_bits = text_to_bits(message)
    key_bits = text_to_bits(key)
    cipher_bits = ''.join('0' if mb == kb else '1' for mb, kb in zip(message_bits, key_bits))
    return cipher_bits

@app.post("/encrypt", response_model=EncryptResponse)
def encrypt(req: EncryptRequest):
    try:
        cipher_bits = vernam_bits(req.message, req.key)
        return {"textoCifrado": cipher_bits, "chave": req.key}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decrypt", response_model=DecryptResponse)
def decrypt(req: DecryptRequest):
    try:
        cipher_bits = req.textoCifrado
        key_bits = text_to_bits(req.chave)
        if len(cipher_bits) != len(key_bits):
            raise ValueError("O tamanho do texto cifrado e da chave em bits não corresponde")
        plain_bits = ''.join('0' if cb == kb else '1' for cb, kb in zip(cipher_bits, key_bits))
        texto_claro = bits_to_text(plain_bits)
        return {"textoClaro": texto_claro}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
