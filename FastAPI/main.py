from fastapi import FastAPI

app = FastAPI()

# URL local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return 'Hola FastAPI'


# URL local: http://127.0.0.1:8000/url

@app.get("/url")
async def root():
    return {"url_curso": "https://mouredev.com/python"}

# Inicio del server: uvicorn main:app --reload

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# Operación POST --> crear datos en el server
# Operación GET --> leer datos del server
# Operación PUT --> actualizar datos del server
# Operación DELETE --> borrar datos del server
