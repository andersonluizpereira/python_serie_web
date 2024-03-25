from fastapi import FastAPI
import requests
import pybreaker
import redis

# Configuração do circuit breaker
breaker = pybreaker.CircuitBreaker(
    fail_max=3,  # Número máximo de falhas permitidas
    reset_timeout=60  # Tempo em segundos antes de tentar reabrir o circuit breaker
)
# Criação de instância do FastAPI
app = FastAPI()


# Função que faz uma chamada a um serviço externo
@breaker
def call_external_service(url):
    response = requests.get(url)
    return str(response.json())


# Configuração do Redis para fallback
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def buscar_dados(chave):
    return redis_client.get(chave)

# Rota do FastAPI para lidar com a chamada ao serviço externo
@app.get("/pokemons")
def handle_call_service():
    service_url = "http://localhost:8081/v1/pokemons"
    chave = "minha_chave"
    try:
        cached_data = buscar_dados(chave)
        if cached_data:
            return {"data": cached_data.decode("utf-8")}
        data = call_external_service(service_url)
        redis_client.set(chave, data)
        return {"data": data}

    except pybreaker.CircuitBreakerError:
        # Se o circuit breaker estiver aberto, tentar obter os dados do Redis
        cached_data = buscar_dados(chave)
        if cached_data or None:
            return {"data": cached_data.decode("utf-8")}
        else:
            raise HTTPException(status_code=503, detail="Serviço indisponível e não há dados em cache")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
