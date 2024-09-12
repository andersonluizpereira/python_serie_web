# API Gateway com Python

Este projeto é um exemplo básico de um **API Gateway** implementado com **FastAPI Unicorv** em Python. Ele atua como um ponto de entrada único para duas APIs de microsserviços, redirecionando as requisições para os serviços apropriados.

## Estrutura do Projeto
````.
├── __init__.py
├── api_gateway
│   ├── Dockerfile
│   ├── __init__.py
│   ├── main.py
│   └── readme.md
├── bff
│   ├── Dockerfile
│   ├── __init__.py
│   └── main.py
├── docker-compose.yml
└── service
    ├── Dockerfile
    ├── __init__.py
    └── main.py
````


- **API Gateway**: Responsável por rotear as requisições para os microsserviços.
- **Microservice 1**: Um serviço que retorna dados simulados.
- **Microservice 2**: Um serviço que processa dados enviados via POST.

## Requisitos

- Python 3.x

### 1. Clonar o repositório

```bash
git clone https://github.com/andersonluizpereira/python_serie_web.git
cd api-gateway-python
```
### 2. Instalar as dependências
Você pode usar um ambiente virtual para gerenciar as dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
pip install -r requirements.txt`

```
### 3. Como Executar
cd api_gateway
```bash
pytho3 api_gateway/main.py
```
cd..

cd bff
```bash
pytho3 bff/main.py
```
cd..

cd bff
```bash
pytho3 service/main.py
```
cd..
### 4. Como testar
#### 4.1 Testando path sem nada
```bash
curl -X GET http://0.0.0.0:8000/ -H "Content-Type: application/json"
```
## Resposta
{"message":"Welcome API GATEWAY!"}

#### 4.2 Testando path de chamado de bff
```bash
curl -X GET http://0.0.0.0:8000/apigateway/v1/cards -H "Content-Type: application/json"
```
## Resposta
{"data":"{'message': 'Welcome V1 HOME CARDS!'}"}

#### 4.3 Testando path de chamado de um service
```bash
curl -X GET http://0.0.0.0:8000/apigateway/v1/products -H "Content-Type: application/json"
```
## Explicação

### API Gateway (api_gateway/main.py)
O API Gateway atua como um proxy, recebendo requisições na porta 8000 e redirecionando para os microsserviços/bff de acordo com a rota.

A rota /bff/<path> encaminha a requisição para o bff.
A rota /service/<path> encaminha a requisição para o Microsserviço de produtos.

### BFF (bff/main.py)
Um serviço destinado para mobile, WEB ou third party (lib) simples que oferece uma rota 

### Service (service/main.py)
Um serviço que processa dados enviados via GET na rota /process e retorna uma resposta processada.
Chamando um serviço com alguma regra de negócio.

## Considerações Finais
Este é um exemplo básico de API Gateway com FastAPI com um BFF e um Microserviço de produtdos. O objetivo é demonstrar como um gateway pode servir como ponto de entrada único, direcionando requisições para diferentes microsserviços. Em aplicações reais, o API Gateway também pode lidar com autenticação, autorização, caching, balanceamento de carga, e mais.