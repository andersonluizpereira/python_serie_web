from fastapi import FastAPI
import requests
import pybreaker
# Configuração do circuit breaker
breaker = pybreaker.CircuitBreaker(
    fail_max=3,        # Número máximo de falhas permitidas
    reset_timeout=60   # Tempo em segundos antes de tentar reabrir o circuit breaker
)
# Criação de instância do FastAPI
app = FastAPI()
# Função que faz uma chamada a um serviço externo
@breaker
def call_external_service(url):
    response = requests.get(url)
    return response.json()
# Rota do FastAPI para lidar com a chamada ao serviço externo
@app.get("/pokemons")
def handle_call_service():
    service_url = "http://localhost:8081/v1/pokemons"
    try:
        data = call_external_service(service_url)
        return {"data": data}
    except pybreaker.CircuitBreakerError:
        raise HTTPException(status_code=503, detail="Serviço indisponível devido ao circuit breaker estar aberto")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)