def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def obtener_calificacion(media):
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def esta_aprobado(media):
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False

def mostrar_alumno(nombre, nota1, nota2, nota3):
    media = calcular_media(nota1, nota2, nota3)
    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    print("Media: " + str(media))
    print(obtener_calificacion(media))
    print("----------------------")

def main():
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)

main()
