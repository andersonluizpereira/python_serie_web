from fastapi import FastAPI

# Criação de instância do FastAPI
app = FastAPI()

@app.get("/v1/services")
def read_root():
    return {"message": "Welcome Services!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
