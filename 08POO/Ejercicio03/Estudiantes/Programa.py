from Estudiantes import Estudiante
from Curso import Curso

curso1 = Curso()
estudiante1 = Estudiante(1234,'Fabio','Holsen','Neyra',7.5)
estudiante2 = Estudiante(1236,'Carlos','Quilis','Munoz')
estudiante3 = Estudiante(1247,'Cristina','Velilla','Jerez')

curso1.agregarEstudiante(estudiante1)
curso1.agregarEstudiante(estudiante2)
curso1.agregarEstudiante(estudiante3)

estudiante1.muestraEstudiante()
curso1.buscarEstudianteObj(1236).muestraEstudiante()
