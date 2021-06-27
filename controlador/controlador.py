from typing import Dict
from modelo.materia import Materia
from modelo.estudiante import Estudiante
from modelo.universidad import Universidad
import json


class Controlador:
    def __init__(self) -> None:
        self.universidad = Universidad("UTP")
        self.load()

    def get_universidad(self) -> Universidad:
        return self.universidad
    
    def crear_estudiante(self, nombre, apellido, cedula, sexo) -> Estudiante:
        obj_estudiante = Estudiante(nombre, apellido, cedula, sexo)
        self.universidad.agregar_estudiante(obj_estudiante)
        return obj_estudiante

    def crear_materia(self, nombre:str, codigo:str, estudiante:Estudiante) -> Materia:
        obj_materia = Materia(nombre, codigo)
        estudiante.agregar_materia(obj_materia)
        return obj_materia
    
    def get_str_materias(self, estudiante:Estudiante):
        str_materias:str = "----------- "+ estudiante.get_apellido() + " -----------" + "\n"
        if len(estudiante.get_materias()) == 0:
            str_materias += "No tiene materias matriculadas \n"
        else:
            for materia in estudiante.get_materias():
                str_materias += "Nombre: " + materia.get_nombre() + "\n"
                str_materias += "Nota: " + str(materia.get_nota()) + "\n"
                str_materias += "----------------------------------------\n"
        return str_materias

    def save(self):
        estudiantes = self.universidad.get_estudiantes()
        diccionario_principal:dict = dict()
        index:int = 1
        for estudiante in estudiantes:
            dict_estudiante = {
                "nombre": estudiante.get_nombre(),
                "apellido": estudiante.get_apellido(),
                "cedula": estudiante.get_cedula(),
                "sexo": estudiante.get_sexo(),
                "materias": [ {"Nombre:":m.get_nombre(), "Codigo":m.get_codigo(), "Nota:":m.get_nota()} for m in estudiante.get_materias()]
            }
            diccionario_principal["0"+str(index)] = dict_estudiante
            index += 1
        band:bool = False
        try:
            with open('modelo/bd.json', 'w') as fichero:
                json.dump(diccionario_principal,fichero)
                band = True
        except:
            print("Error al guardar los datos")
        return band

    def load(self):
        band:bool = False
        diccionario: dict = dict()
        try:
            with open('modelo/bd.json') as fichero:
                diccionario = json.load(fichero)
                for dict_estudiante in diccionario.values():
                    nombre:str = dict_estudiante["nombre"]
                    apellido:str = dict_estudiante["apellido"]
                    cedula:str = dict_estudiante["cedula"]
                    sexo:str = dict_estudiante["sexo"]
                    obj_estudiante:Estudiante = self.crear_estudiante(nombre,apellido,cedula,sexo)
                    for materia in dict_estudiante["materias"]:
                        obj_materia = self.crear_materia(materia["Nombre"],obj_estudiante)
                        self.calificar_materia(obj_estudiante, materia["codigo"], materia["nota"])
                band = True
        except:
            print("Error al cargar los datos")
        return band
    
    def calificar_materia(self, estudiante:Estudiante, codigo_materia:str, nota:float):
        estudiante.consultar_materia(codigo_materia).set_nota(nota)
