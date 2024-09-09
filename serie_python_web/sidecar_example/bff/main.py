import requests
from fastapi import FastAPI

# Criação de instância do FastAPI
app = FastAPI()

# Função que faz uma chamada a um serviço externo
def call_external_service(url):
    response = requests.get(url)
    return str(response.json())

# Rota do FastAPI para lidar com a chamada ao serviço externo
@app.get("/home")
def handle_call_service():
    service_url = "http://services:8001/v1/services"
    try:
        data = call_external_service(service_url)
        return {"data": data}
    except:
        print("An exception occurred")

@app.get("/")
def read_root():
    return {"message": "Welcome BFF!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
