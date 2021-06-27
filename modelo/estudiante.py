from modelo.materia import Materia

class Estudiante:
    def __init__(self, nombre, apellido, cedula, sexo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.sexo = sexo
        self.materias:list[Materia] = []
    
    def __str__(self) -> str:
        str_estudiante:str = "Nombre: " + self.nombre + '\n'
        str_estudiante += "Apellido: " + self.apellido + '\n'
        str_estudiante += "Cédula: " + self.cedula + '\n'
        str_estudiante += "Sexo: " + self.sexo + '\n'
        return str_estudiante

    """Métodos consultores"""

    def get_nombre(self)-> str:
        return self.nombre
    
    def get_apellido(self)-> str:
        return self.apellido

    def get_cedula(self)-> str:
        return self.cedula

    def get_sexo(self)-> str:
        return self.sexo

    def get_materias(self)-> list:
        return self.materias
    
    """Métodos modificadores"""

    def set_nombre(self, nombre:str):
        self.nombre = nombre
    
    def set_apellido(self, apellido:str):
        self.apellido = apellido
    
    def set_apellido(self, sexo:str):
        self.sexo = sexo

    def set_materias(self,materias:list):
        self.materias = materias

    def agregar_materia(self, materia:Materia):
        self.materias.append(materia)
    
    def eliminar_materia(self, nombre_materia:str) -> Materia:
        filtro_materias = list(filter(lambda obj_materia: obj_materia.get_nombre().lower() == nombre_materia.lower(), self.materias))
        index = self.materias.index(filtro_materias[0])
        m_eliminada = self.materias.pop(index)
        return m_eliminada
    
    def consultar_materia(self, codigo_materia:str) -> Materia:
        filtro_materias = list(filter(lambda obj_materia: obj_materia.get_codigo().lower() == codigo_materia.lower(), self.materias))
        return filtro_materias[0]