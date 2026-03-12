class Estudiante:

    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.materias = []

    def inscribir_materia(self, materia):
        self.materias.append(materia)
        print(f'{self.nombre} se inscribió en {materia}')

    def presentarse(self):
        print(f'Hola, soy {self.nombre}')
        print(f'Tengo {self.edad} años')
        print(f'Estudio {self.carrera}')
        print(f'Materias inscritas: {len(self.materias)}')

    def estudiar(self, horas):
        print(f'{self.nombre} estudió {horas} horas')


tu_estudiante = Estudiante("Juan Sebastian Ramos Ovalle", 18, "Sistematización de Datos")

tu_estudiante.presentarse()

tu_estudiante.inscribir_materia("Programación")
tu_estudiante.inscribir_materia("Matemáticas")
tu_estudiante.inscribir_materia("Bases de Datos")

tu_estudiante.estudiar(5)