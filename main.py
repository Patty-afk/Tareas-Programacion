from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from user import UserModel
from random import randint
from sqlmodel import select
from schemas import UserSchema

#para movies
from models import MoviesModel
from schemasMov import MovieSchema
from database import create_db_and_tables, SessionDep

app = FastAPI()
#fastapi dev main.py
"""
GET - Obtener algo
POST - Crear algo
PUT - Actualizar algo
DELETE - Eliminar
"""
#sirve para crear tablas en la base de datos
create_db_and_tables()

@app.post("/users")
async def create_user(user_data: UserSchema, database:SessionDep):
    user = UserModel(
        name= user_data.name,
        last_name= user_data.last_name,
        email = user_data.email,
        phone = user_data.phone
    )
    
    database.add(user)
    database.commit()
    database.refresh(user)
    return user

@app.get ("/users")
async def get_users(database: SessionDep):
    statement = select(UserModel)
    results = database.exec(statement)
    items = results.all()
    return items


#estamos haciendo un metodo que obtenga el usuario por un id el cual lo tomara desde la base de datos 
@app.get("/users/{user_id}")
async def get_user_by_id(user_id:int, database :SessionDep):
    user = database.get(UserModel, user_id)
    
    #si no encuentras un user, retornara el error 404 y en detalles, raise levanta una exepcion
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="usuario no encontrado")
    
    return user

#ruta post para crear una nueva pelicula

@app.post("/movies")
async def create_movie(movie_data: MovieSchema, database: SessionDep):
    #aqui creamos la instancia del modelo con los datos recibidos
    movie = MoviesModel(
        nombre = movie_data.nombre,
        año_estreno=movie_data.año_estreno,
        duracion = movie_data.duracion,
        director= movie_data.director,
        clasificacion=movie_data.clasificacion,
        genero= movie_data.genero   
    )
    
    database.add(movie)
    database.commit()
    database.refresh(movie) #actualiza la movie con los datos 
    return movie    

@app. get("/movies")
async def get_movies(database: SessionDep):
    statement= select(MoviesModel) #es la consulta para obtener las peliculas
    results = database.exec(statement)
    movies = results.all()
    return movies

#para obtener pelicula por ID Get
@app.get("/movies/{movie_id}")
async def get_movie_id(movie_id: int, database: SessionDep):
    movie = database.get(MoviesModel, movie_id) 
   
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Pelicula no encontrada")
    
    return movie