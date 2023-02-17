respuesta = "si"
calificacionesAlumnos = []

while respuesta == "si":
    calificacionesAlumnos.append(input("Escribe la calificación del siguiente alumno: "))

    respuesta = input("Escribe si para seguir añadiendo números")

print(calificacionesAlumnos)