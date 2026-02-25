# Programa de gestión de notas de alumnos
# Autor: Jose
# Fecha: 25/02/2026

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    return (nota1 + nota2 + nota3) / 3

def obtener_calificacion(media):
    """
    Devuelve la calificación textual según la media.

    Args:
        media (float): La media aritmética del alumno.

    Returns:
        str: Calificación textual (Sobresaliente, Notable, Aprobado o Suspenso).
    """
    # Se usa elif para evitar comprobar condiciones innecesarias
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def esta_aprobado(media):
    """
    Indica si el alumno está aprobado o suspendido.

    Args:
        media (float): La media aritmética del alumno.

    Returns:
        bool: True si aprobado, False si suspendido.
    """
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False

def mostrar_alumno(nombre, nota1, nota2, nota3):
    """
    Muestra por pantalla los datos completos de un alumno.

    Args:
        nombre (str): Nombre del alumno.
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.
    """
    media = calcular_media(nota1, nota2, nota3)  # Calculamos la media antes de mostrar
    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    print("Media: " + str(media))
    print(obtener_calificacion(media))
    print("----------------------")

def main():
    """
    Función principal que ejecuta el programa con datos de ejemplo.
    """
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)

main()
