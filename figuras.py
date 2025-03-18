class figura_tridimensional:
    # Método constructor para inicializar los atributos de la clase
    def __init__(self, lado, material, densidad):
        self.lado = lado  # Asigna el lado del cubo
        self.material = material  # Asigna el material del cubo
        self.densidad = densidad  # Asigna la densidad del material (en kg/m³)

    # Método para mostrar las características del cubo
    def mostrar_todo(self):
        print(f"Cubo: Lado = {self.lado} cm, Material = {self.material}, Densidad = {self.densidad} kg/m³")

    # Método para calcular el área superficial del cubo
    def calcular_area(self):
        return 6 * (self.lado ** 2)  # Área superficial = 6 * lado²

    # Método para calcular el volumen del cubo
    def calcular_volumen(self):
        return self.lado ** 3  # Volumen = lado³

    # Método para calcular el peso del cubo
    def calcular_peso(self):
        volumen_m3 = self.calcular_volumen() / 1_000_000  # Convertir volumen a m³ (1 m³ = 1,000,000 cm³)
        return volumen_m3 * self.densidad  # Peso = Volumen (m³) * Densidad (kg/m³)


# Programa principal
if __name__ == "__main__":
    # Crear dos objetos de la clase figura_tridimensional con diferentes características
    cubo1 = figura_tridimensional(10, "Acero", 7850)  # Cubo de acero con lado 10 cm
    cubo2 = figura_tridimensional(15, "Aluminio", 2700)  # Cubo de aluminio con lado 15 cm

    # Mostrar las características de cada cubo
    print("=== Características de los Cubos ===")
    cubo1.mostrar_todo()  # Mostrar características del primer cubo
    cubo2.mostrar_todo()  # Mostrar características del segundo cubo

    # Mostrar el área, volumen y peso de cada cubo
    print("\n=== Área, Volumen y Peso de los Cubos ===")
    print(f"Cubo 1: Área = {cubo1.calcular_area()} cm², Volumen = {cubo1.calcular_volumen()} cm³, Peso = {cubo1.calcular_peso():.2f} kg")
    print(f"Cubo 2: Área = {cubo2.calcular_area()} cm², Volumen = {cubo2.calcular_volumen()} cm³, Peso = {cubo2.calcular_peso():.2f} kg")