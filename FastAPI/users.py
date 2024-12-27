from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
    userid: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(userid = 1, name = 'Alex', surname = 'Vazquez', url = 'https://alex.vazquez', age = 21),
              User(userid = 2, name = 'Jaime', surname = 'Pueyo', url = 'https://pajaime.com', age = 21),
              User(userid = 3, name = 'Fito', surname = 'Vazquez', url = 'https://fitoylabanda', age = 32)]

@app.get("/users")
async def users():
    return users_list


# Búsqueda por path 
@app.get("/user/{userid}")
async def user(ide: int):
    search_user(ide)
  
  
      
# Búsqueda por query
"""Para buscar por query:
Imaginemsos que tenemos la siguiente url --> https://alex.vazquez/users

Si queremos buscar por query, el id de un user por ejemplo, tenemos que empezar poniendo ? al inicio de
la búsqueda --> https://alex.vazquez/users/?id=7

Como estamos viendo, una vez ponemos ?, luego podemos poner el parametro que queramos, en mi caso, el id
del user

Por último, para concatener varios parámetros usamos & 
Ejemplo --> https://alex.vazquez/users/?id=7&name=alex"""


@app.get("/userquery/")
async def user(userid: int):
    search_user(userid)

def search_user(ide: int):
    users = filter(lambda user: user.userid == ide, users_list)
    try:
        return list(users)[0]
    except:
        return "{'error': 'No se ha encontrado el id buscado.'}"


# Hasta ahora solo hemos hecho peticiones GET al server. Ahora veremos las peticiones PUT, POST, DELETE

# Petición POST --> añade nuevos datos al server
@app.post("/user/")
async def add_user(user: User):
    if type(search_user(user.userid)) == User:
        return {"error": "El usuario ya existe."}
    else:
        users_list.append(user)


# Petición PUT --> actualiza datos del server
@app.put("/user/")
async def update_user(user: User):
    
    user_found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.userid == user.userid:
            users_list[index] = user
            user_found = True
    
    if not user_found:
        return {"error" : "No se ha actulizado el usuario"}
    
    return user


# Petición DELETE --> elimina datos del server
@app.delete("/user/{ide}")
async def del_user(ide: int):
    
    found = False
    
    for index, user in enumerate(users_list):
        if user.userid == ide:
            del users_list[index]
            found = True
    
    if not found:
        return {"error" : "No se ha podido eliminar el usuario."}
    
            



# Iniciar el server: uvicorn users:app --reload
