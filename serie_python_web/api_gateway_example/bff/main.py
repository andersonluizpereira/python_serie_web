from fastapi import FastAPI

# Criação de instância do FastAPI
app = FastAPI()


@app.get("/v1/cards")
def read_root():
    return {"message": "Welcome V1 HOME CARDS!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
