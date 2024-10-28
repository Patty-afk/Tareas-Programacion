from pydantic import BaseModel

class MovieSchema(BaseModel):
    nombre: str
    año_estreno: int
    duracion : int
    director :str
    clasificacion: str
    genero: str
    