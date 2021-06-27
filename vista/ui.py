from modelo.estudiante import Estudiante
from controlador.controlador import Controlador

class Ui:

    def __init__(self) -> None:
        self.controlador:Controlador = Controlador()
        self.menu()
        
    def menu(self):
        opc:int = 0
        while opc != -1:
            print("---------- Universidad " + self.controlador.get_universidad().get_nombre() + "----------")
            print("")
            print("1 -> Crear estudiante")
            print("2 -> Consultar estudiante")
            print("3 -> Consultar todos los estudiantes")
            print("4 -> Matricular materia")
            print("5 -> Calificar estudiante")
            print("6 -> Guardar todos los cambios")
            print("-1 -> Salir")
            opc = int(input("Por favor ingrese una opción: "))

            if opc == 1:
                nombre:str = input("Ingrese nombre del estudiante: ")
                apellido:str = input("Ingrese apellido del estudiante: ")
                cedula:str = input("Ingrese cédula del estudiante: ")
                sexo:str = input("Ingrese sexo del estudiante: ")
                self.controlador.crear_estudiante(nombre,apellido,cedula,sexo)
                print("Estudiante creado con éxito")

            elif opc == 2:
                cedula:str = input("Ingrese cédula del estudiante: ")
                obj_estudiante:Estudiante = self.controlador.get_universidad().buscar_estudiante(cedula)
                print("")
                print("---------- Estudiante ----------")
                print(obj_estudiante)
                print(self.controlador.get_str_materias(obj_estudiante))
            elif opc == 3:
                lista_estudiantes = self.controlador.get_universidad().get_estudiantes()
                contador:int = 1
                for estudiante in lista_estudiantes:
                    print(f"Estudiante {contador}: \n")
                    print(estudiante)
                    print(self.controlador.get_str_materias(estudiante))
                    contador += 1
            elif opc == 4:
                cedula:str = input("Por favor ingrese cédula de estudiante para matricular materia: ")
                obj_estudiante = self.controlador.get_universidad().buscar_estudiante(cedula)
                nombre_materia:str = input("Nombre de la materia a matricular: ")
                codigo_materia:str = input("Código de la materia: ")
                self.controlador.crear_materia(nombre_materia, codigo_materia, obj_estudiante)
                print("Materia matriculada con éxito")
            elif opc == 5:
                cedula:str = input("Ingrese cédula de estudiante: ")
                obj_estudiante = self.controlador.get_universidad().buscar_estudiante(cedula)
                if obj_estudiante != None:
                     codigo_materia = input("Ingrese el código de la materia: ")
                     nota:float = input("Ingrese la nota de la materia: ")
                     self.controlador.calificar_materia(obj_estudiante, codigo_materia, nota)
                else:
                    print("No se encuentra el estudiante.")
            elif opc == 6:
                resp = self.controlador.save()
                if resp:
                    print("Se guardaron los cambios con éxito!")
                else:
                    print("Ops!, No se guardaron los cambios con éxito!")

        """
        obj_estudiante = controlador.crear_estudiante("Juan","Perez","123456","M")
        controlador.crear_materia("Programación", obj_estudiante)
        controlador.crear_materia("Matemáticas", obj_estudiante)
        controlador.crear_materia("Coach", obj_estudiante)
        controlador.crear_materia("Administración", obj_estudiante)
        print(obj_estudiante)
        print(controlador.get_str_materias(obj_estudiante))
        """