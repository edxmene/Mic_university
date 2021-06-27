class Materia:
    def __init__(self, nombre:str, codigo:str) -> None:
        self.nombre = nombre
        self.codigo = codigo
        self.nota:float = 0
    
    def __str__(self) -> str:
        str_materia = "Nombre: " + self.nombre + "\n"
        str_materia += "Código: " + str(self.codigo) + "\n"
        str_materia += "Nota: " + str(self.nota) + "\n"
        return str_materia

    """Métodos consultores"""
    def get_nombre(self)->str:
        return self.nombre

    def get_nota(self)->float:
        return self.nota

    def get_codigo(self)->str:
        return self.codigo

    """Métodos modificadores"""
    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def set_nota(self,nota):
        self.nota = nota
    
    def set_codigo(self,codigo:str):
        self.codigo = codigo
        