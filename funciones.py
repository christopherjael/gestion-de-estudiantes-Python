from peewee import *
import os
from prettytable import PrettyTable
import webbrowser

db = SqliteDatabase('Central_DB.db')
db.connect()

pt = PrettyTable()


def limpiar():
    os.system('cls')
    pass



class estudiante(Model):
    matricula = CharField(10)
    nombre = CharField(50)
    apellido = CharField(50)
    n1 = IntegerField()
    n2 = IntegerField()

    class Meta:
        database = db
    pass

db.create_tables([estudiante])

def mostrasEstudiantes():
    print('Lista de estudiante\n')
    pt.field_names = ['Matricula', 'Nombre', 'Apellido', 'Nota 1', 'Nota 2', 'Promedio','EQ']
    for i in estudiante.select():
        prom = float((i.n1 + i.n2)/2)
        pt.add_row([i.matricula, i.nombre, i.apellido, i.n1, i.n2, prom, calcularEQ(prom)])
        pass
    return pt
    pass

def calcularEQ(promedio):
    eq = 'F'
    if promedio >= 90:
        eq = 'A'
    elif promedio >= 80 and promedio < 90:
        eq = 'B'
    elif promedio >= 70 and promedio < 80:
        eq = 'C'
        pass

    return eq

def agregar():
    limpiar()
    print('Agregando Estudiante')
    est = estudiante()
    est.matricula = input('Introduce la matricula\n> ')
    est.nombre = input('Introduce el nombre\n> ')
    est.apellido = input('Introduce el apllido\n> ')
    est.n1 = input('Introduce la nota 1\n> ')
    est.n2 = input('Introduce la nota 2\n> ')
    est.save()
    input('Presione ENTER')
    pass

def confirmarDato(campo, valor):
    print('El campo '+campo+' tiene el valor '+valor)
    tmp = input('Indroduce el nuevo valor o dejelo vacio\n> ')
    if tmp == '':
        return valor
    else:
        return tmp
        pass
    pass



def modificar():
    limpiar()
    print(mostrasEstudiantes)()
    print(' ')
    idx = input('Indroce la matricula del estudiante o presione x para cancelar\n> ')
    if idx == 'x':
        return False
    est = estudiante.select().where(estudiante.matricula == idx).get()

    est.matricula = confirmarDato('Matricula',est.matricula)
    est.nombre = confirmarDato('Nombre',est.nombre)
    est.apellido = confirmarDato('Apellido',est.apellido)
    est.n1 = int(confirmarDato('Nota 1',str(est.n1)))
    est.n2 = int(confirmarDato('Nota 2',str(est.n2)))
    est.save()
    print('Registro Modificado')
    input('Presione ENTER')
    limpiar()
    pass



def eliminar():
    limpiar()
    print(mostrasEstudiantes())
    print(' ')
    idx = input('Indroce la matricula del estudiante para eliminarlo o presione x para cancelar\n> ')
    if idx == 'x':
        return False
    est = estudiante.select().where(estudiante.matricula).get()
    print(f'El estudiante MATRICULA: {est.matricula} con NOMBRE: {est.nombre}, hacido eliminado.')
    est.delete_instalce()
    input('Presione ENTER')
    pass

def exportar():
    data = mostrasEstudiantes()
    html = data.get_html_string()
    tabla_html = html.replace('<table>', '<table class ="table table-bordered mx-4">')
    f = open('index.html', 'w')
    f.write(f"""
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title>Estudiantes</title>
    </head>

    <body>
    <h3 class="title text-center">Datos de los estudiantes</h3>
    <div class="container">
        {tabla_html}
    </div>
    </body>

    </html>
    """)
    f.close
    print('Exportando estudiantes, espere un momento...')
    webbrowser.open('index.html')