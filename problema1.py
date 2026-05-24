import numpy as np

"""Problema 1: Clasificación de compromiso de sesiones.

El usuario ingresa los datos de cada sesión en una matriz vacía de numpy.
Formato de cada fila: [ID Cliente, Duración (segundos), Eventos Clics]

Reglas:
- "Alto": Duración > 180s y Clics > 8
- "Bajo": Duración < 60s o Clics < 3
- "Medio": resto de casos
"""


def clasificar_sesion(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    if duracion < 60 or clics < 3:
        return "Bajo"
    return "Medio"


def crear_matriz_vacia():
    return np.empty((0, 3), dtype=int)


def agregar_sesion(matriz, id_cliente, duracion, clics):
    nueva_fila = np.array([[id_cliente, duracion, clics]], dtype=int)
    return np.vstack([matriz, nueva_fila])


def leer_entero(texto):
    while True:
        valor = input(texto).strip()
        if not valor:
            print("Por favor ingresa un número.")
            continue
        try:
            return int(valor)
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


def leer_sesiones():
    sesiones = crear_matriz_vacia()
    while True:
        cantidad = leer_entero("¿Cuántas sesiones deseas registrar? " )
        if cantidad >= 5:
            break
        print("Debes registrar al menos 5 sesiones.")
    for i in range(1, cantidad + 1):
        print(f"\nSesión {i}")
        id_cliente = leer_entero("ID Cliente: " )
        duracion = leer_entero("Duración (segundos): " )
        clics = leer_entero("Eventos Clics: " )
        sesiones = agregar_sesion(sesiones, id_cliente, duracion, clics)
    return sesiones

def generar_informe(matriz):
    informe = []
    for fila in matriz:
        id_cliente, duracion, clics = fila
        clasificacion = clasificar_sesion(duracion, clics)
        informe.append((int(id_cliente), clasificacion))
    return informe


def imprimir_tabla(headers, datos):
    if not datos:
        print("No hay datos para mostrar.")
        return
    
    # Calcular ancho de cada columna
    anchos = []
    for i, header in enumerate(headers):
        ancho_max = len(str(header))
        for fila in datos:
            ancho_max = max(ancho_max, len(str(fila[i])))
        anchos.append(ancho_max + 2)  # Padding
    
    # Línea superior
    linea = "+" + "+".join(["-" * ancho for ancho in anchos]) + "+"
    print(linea)
    
    # Encabezados
    fila_header = "|"
    for i, header in enumerate(headers):
        fila_header += f" {str(header).center(anchos[i] - 2)} |"
    print(fila_header)
    
    # Línea separadora
    print(linea)
    
    # Datos
    for fila in datos:
        fila_str = "|"
        for i, celda in enumerate(fila):
            fila_str += f" {str(celda).center(anchos[i] - 2)} |"
        print(fila_str)
    
    # Línea inferior
    print(linea)


def imprimir_informe(informe):
    print("\nInforme de compromiso de sesiones:")
    if not informe:
        print("No se registraron sesiones.")
        return
    
    headers = ["ID Cliente", "Clasificación"]
    imprimir_tabla(headers, informe)


if __name__ == "__main__":
    sesiones = leer_sesiones()
    informe = generar_informe(sesiones)
    imprimir_informe(informe)
