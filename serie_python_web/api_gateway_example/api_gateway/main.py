import requests
from fastapi import FastAPI

# Criação de instância do FastAPI
app = FastAPI()

BFF_URL = 'http://localhost:8001'
SERVICE_URL = 'http://localhost:8002'


# Função que faz uma chamada a um serviço externo
def call_external_service(url):
    response = requests.get(url)
    return str(response.json())


# Rota do FastAPI para lidar com a chamada ao serviço externo
@app.get('/apigateway/v1/cards')
def handle_call_service():
    service_url = f'{BFF_URL}/v1/cards'
    try:
        data = call_external_service(service_url)
        return {"data": data}
    except:
        print("An exception occurred")

# Rota do FastAPI para lidar com a chamada ao serviço externo
@app.get("/apigateway/v1/products")
def handle_call_service():
    service_url = f'{SERVICE_URL}/v1/products'
    try:
        data = call_external_service(service_url)
        return {"data": data}
    except:
        print("An exception occurred")

@app.get("/")
def read_root():
    return {"message": "Welcome API GATEWAY!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
