
import time
from funciones import *

limpiar()

while True:
    print('''
    Bienvenido al Administrador de estudiante de ASysComputers
    
    Digite la opcion que quiere realizar en los estudiantes:
    1-Agregar Estudiante
    2-Modificar Estudiante
    3-Elimnar Estudiante
    4-Exportar Datos de Estudiante
    5-Salir del programa
    ''')
    opcion = int(input('Indroduce una opción\n> '))
    if opcion == 1:
        #code
        agregar()
    elif opcion == 2:
        #code
        modificar()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        #code
        exportar()
    elif opcion == 5:
        print('Saliendo del programa....')
        time.sleep(2)
        break
    else:
        input('Introce una opción valida')
        limpiar()
