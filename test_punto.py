import punto as p  # Importa el módulo punto.py

def solicitar_numero(mensaje):
    # Función para solicitar un número válido al usuario
    while True:
        try:
            valor = float(input(mensaje))  # Intenta convertir la entrada a float
            return valor  # Si es válido, retorna el valor
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")

def formatear_coordenada(valor):
    # Función para formatear la coordenada (eliminar .0 si es un número entero)
    if valor == int(valor):  # Si no tiene parte decimal
        return int(valor)  # Retorna como entero
    return valor  # Retorna como float

def main():
    # Solicitar al usuario las coordenadas iniciales del punto
    print("=== Ingrese las coordenadas del punto inicial ===")
    coor_x = solicitar_numero("Ingrese la coordenada x: ")
    coor_y = solicitar_numero("Ingrese la coordenada y: ")

    # Crear un objeto de la clase Punto con las coordenadas ingresadas
    punto_1 = p.punto(coor_x, coor_y)

    # Mostrar las coordenadas actuales del punto
    print("\n=== Coordenadas del punto ===")
    x_formateado = formatear_coordenada(punto_1.get_coor_x())
    y_formateado = formatear_coordenada(punto_1.get_coor_y())
    print(f"El punto tiene coordenadas (x, y) = ({x_formateado}, {y_formateado})")

    # Calcular y mostrar la distancia al origen
    distancia = punto_1.calcular_distancia()
    print(f"\nDistancia al origen: {distancia:.2f}")

    # Calcular y mostrar el ángulo con el eje X (en grados y radianes)
    angulo_radianes = punto_1.calcular_angulo()
    angulo_grados = p.punto.radianes_a_grados(angulo_radianes)  # Llama al método estático
    print(f"Ángulo con el eje X: {angulo_grados:.2f}° ({angulo_radianes:.2f} radianes)")

    # Solicitar al usuario las coordenadas de otro punto para calcular la distancia
    print("\n=== Calcular distancia hasta otro punto ===")
    nueva_x = solicitar_numero("Ingrese la coordenada x del otro punto: ")
    nueva_y = solicitar_numero("Ingrese la coordenada y del otro punto: ")

    # Calcular y mostrar la distancia hasta el otro punto
    distancia_hasta = punto_1.calcular_distancia_hasta(nueva_x, nueva_y)
    nueva_x_formateado = formatear_coordenada(nueva_x)
    nueva_y_formateado = formatear_coordenada(nueva_y)
    print(f"Distancia hasta el punto ({nueva_x_formateado}, {nueva_y_formateado}): {distancia_hasta:.2f}")

if __name__ == "__main__":
    main()  # Ejecuta la función principal