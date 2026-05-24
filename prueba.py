
import numpy as np

# Función de clasificación (REQUERIDA)
def clasificar_sesion(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Leer número entero validado
def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except:
            print("Ingresa un número válido.")

# Pedir datos al usuario (mínimo 5)
def leer_sesiones():
    while True:
        n = leer_entero("¿Cuántas sesiones desea ingresar? ")
        if n >= 5:
            break
        else:
            print("Debe ingresar al menos 5 sesiones.")

    matriz = []

    for i in range(n):
        print(f"\nSesión {i+1}")
        id_cliente = leer_entero("ID Cliente: ")
        duracion = leer_entero("Duración (segundos): ")
        clics = leer_entero("Eventos Clics: ")

        matriz.append([id_cliente, duracion, clics])

    return np.array(matriz)

# Generar informe
def generar_informe(matriz):
    informe = []
    for fila in matriz:
        id_cliente, duracion, clics = fila
        clasificacion = clasificar_sesion(duracion, clics)
        informe.append((id_cliente, clasificacion))
    return informe

# Mostrar tabla
def mostrar_tabla(informe):
    print("\nInforme de compromiso de sesiones:\n")
    print("+------------+---------------+")
    print("| ID Cliente | Clasificación |")
    print("+------------+---------------+")

    for id_cliente, clasificacion in informe:
        print(f"| {str(id_cliente).center(10)} | {clasificacion.center(13)} |")

    print("+------------+---------------+")

# ✅ Programa principal
sesiones = leer_sesiones()
informe = generar_informe(sesiones)
mostrar_tabla(informe)
