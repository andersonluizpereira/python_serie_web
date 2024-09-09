O **Sidecar Pattern** é um padrão de design arquitetônico usado principalmente em ambientes de microserviços. Ele envolve o uso de um **componente secundário** (chamado "sidecar") que é implantado ao lado de um serviço principal para fornecer funcionalidades auxiliares, como monitoramento, proxy, logging ou segurança.

### Exemplo:
Imagine um serviço de autenticação que precisa de logging detalhado de cada requisição. Em vez de incluir essa lógica diretamente no serviço, você pode criar um **sidecar** que captura e envia os logs para um sistema central. Esse sidecar roda em paralelo ao serviço principal, sem que este precise ser modificado.

#### Como funciona:
- O serviço principal continua focado em suas responsabilidades (ex: autenticação).
- O sidecar lida com tarefas complementares (ex: logs, segurança).

### Vantagens:
- Separação de responsabilidades.
- Reutilização do sidecar em outros serviços.
- Flexibilidade e escalabilidade.

Esse padrão é muito usado em plataformas como **Kubernetes**, onde o sidecar é implementado como um container adicional no mesmo pod do serviço principal.

# # # Estrutura de arquivos:
````.
├── __init__.py
├── bff
│   ├── Dockerfile
│   ├── __init__.py
│   └── main.py
├── docker-compose.yml
├── readme.md
└── service
    ├── Dockerfile
    ├── __init__.py
    └── main.py

````
1. Código do serviço principal (bff/main.py):
````
import requests from fastapi import FastAPI

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
````
2. Dockerfile para o serviço principal (bff/Dockerfile):
````
FROM python:3.9-slim

WORKDIR /app

RUN pip install --only-binary :all: fastapi[all] requests

COPY . /app

CMD ["python", "main.py"]
````