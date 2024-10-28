from sqlmodel import SQLModel, Field

#modelo de la tabla y su nombre 
class MoviesModel(SQLModel, table=True):
    __tablename__ = "movies" 
    
    #primary key es un identificador unico para cada registro en la tablita
    id: int = Field(primary_key=True)
    nombre: str
    año_estreno: int
    duracion : int
    director :str
    clasificacion: str
    genero: str