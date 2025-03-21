class punto:
    def __init__(self, coor_x, coor_y):
        self._coor_x = coor_x  # Atributo privado para la coordenada x
        self._coor_y = coor_y  # Atributo privado para la coordenada y

    # Métodos públicos para obtener y establecer las coordenadas
    def get_coor_x(self):
        return self._coor_x  # Devuelve la coordenada x

    def set_coor_x(self, coor_x):
        self._coor_x = coor_x  # Actualiza la coordenada x

    def get_coor_y(self):
        return self._coor_y  # Devuelve la coordenada y

    def set_coor_y(self, coor_y):
        self._coor_y = coor_y  # Actualiza la coordenada y

    # Método público para mostrar las coordenadas
    def mostrar_todo(self):
        print(f"El punto tiene coordenadas (x, y) = ({self._coor_x}, {self._coor_y})")

    # Método público para calcular la distancia al origen
    def calcular_distancia(self):
        return self._calcular_distancia_al_origen()  # Llama al método privado

    # Método público para calcular el ángulo con el eje X
    def calcular_angulo(self):
        return self._calcular_angulo_con_eje_x()  # Llama al método privado

    # Método público para calcular la distancia hasta otro punto
    def calcular_distancia_hasta(self, nueva_x, nueva_y):
        return self._calcular_distancia_hasta_punto(nueva_x, nueva_y)  # Llama al método privado

    # Métodos privados (internos)
    def _calcular_distancia_al_origen(self):
        # Calcula la distancia desde el punto actual hasta el origen (0, 0)
        return (self._coor_x**2 + self._coor_y**2) ** 0.5

    def _calcular_angulo_con_eje_x(self):
        # Calcula el ángulo que forma el punto con el eje X (en radianes)
        if self._coor_x == 0:  # Evitamos división por cero
            if self._coor_y > 0:
                return 1.5707963267948966  # 90° en radianes (π/2)
            elif self._coor_y < 0:
                return -1.5707963267948966  # -90° en radianes (-π/2)
            else:
                return 0  # El punto está en el origen
        return self._coor_y / self._coor_x  # Devolvemos la tangente como aproximación del ángulo

    def _calcular_distancia_hasta_punto(self, nueva_x, nueva_y):
        # Calcula la distancia desde el punto actual hasta otro punto (nueva_x, nueva_y)
        return ((nueva_x - self._coor_x)**2 + (nueva_y - self._coor_y)**2) ** 0.5

    # Método estático para convertir radianes a grados
    @staticmethod
    def radianes_a_grados(radianes):
        # Convierte radianes a grados usando la fórmula: grados = radianes * (180 / π)
        return radianes * (180 / 3.141592653589793)  # π ≈ 3.141592653589793