class rectangulo:
    # Método constructor para inicializar los atributos de la clase
    def __init__(self, base, altura):
        self.base = base  # Asigna la base del rectángulo
        self.altura = altura  # Asigna la altura del rectángulo

    # Método para mostrar las características del rectángulo
    def mostrar_todo(self):
        print(f"Rectángulo: Base = {self.base} cm, Altura = {self.altura} cm")

    # Método para calcular el área del rectángulo
    def calcular_area(self):
        return self.base * self.altura  # Área = base * altura

    # Método para calcular el perímetro del rectángulo
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)  # Perímetro = 2 * (base + altura)


# Programa principal
if __name__ == "__main__":
    # Crear tres objetos de la clase Rectangulo con diferentes características
    rectangulo1 = rectangulo(5, 10)  # Rectángulo con base 5 cm y altura 10 cm
    rectangulo2 = rectangulo(8, 4)  # Rectángulo con base 8 cm y altura 4 cm
    rectangulo3 = rectangulo(12, 6)  # Rectángulo con base 12 cm y altura 6 cm

    # Mostrar las características de cada rectángulo
    print("=== Características de los Rectángulos ===")
    rectangulo1.mostrar_todo()  # Mostrar características del primer rectángulo
    rectangulo2.mostrar_todo()  # Mostrar características del segundo rectángulo
    rectangulo3.mostrar_todo()  # Mostrar características del tercer rectángulo

    # Mostrar el área y el perímetro de cada rectángulo
    print("\n=== Área y Perímetro de los Rectángulos ===")
    print(f"Rectángulo 1: Área = {rectangulo1.calcular_area()} cm², Perímetro = {rectangulo1.calcular_perimetro()} cm")
    print(f"Rectángulo 2: Área = {rectangulo2.calcular_area()} cm², Perímetro = {rectangulo2.calcular_perimetro()} cm")
    print(f"Rectángulo 3: Área = {rectangulo3.calcular_area()} cm², Perímetro = {rectangulo3.calcular_perimetro()} cm")