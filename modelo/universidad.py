from modelo.estudiante import Estudiante

class Universidad:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.estudiantes:list[Estudiante] = []
    
    """Métodos consultores"""

    def get_nombre(self) -> str:
        return self.nombre

    def get_estudiantes(self) -> list:
        return self.estudiantes

    """Métodos modificadores"""

    def set_nombre(self, nombre):
        self.nombre = nombre   

    def set_estudiantes(self, estudiantes):
        self.estudiantes = estudiantes

    def agregar_estudiante(self, estudiante:Estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, cedula:str) -> Estudiante:
        obj_estudiante:Estudiante = None
        filtro_estudiante = list(filter(lambda obj_estudiante: obj_estudiante.get_cedula() == cedula, self.estudiantes))
        if len(filtro_estudiante) > 0:
            obj_estudiante = filtro_estudiante[0]
        return obj_estudiante
