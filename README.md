# 📌 Programación - Introducción a la POO

## 📖 Descripción
Este documento proporciona información sobre la **Programación Orientada a Objetos (POO)** en Python, incluyendo conceptos clave y el uso de la función `main()`.

## 📚 Contenido
1. **Función `main()` en Python**
   - Explicación de la estructura de `main()` en Python.
   - Uso de `if __name__ == "__main__"`.
   - Importancia de la función `main()` en la reutilización de código.

2. **Conceptos de Programación Orientada a Objetos (POO)**
   - Clases y Objetos.
   - Métodos y atributos.
   - Herencia, polimorfismo y encapsulamiento.

3. **Referencias y recursos**
   - Enlace a documentación externa sobre Python y POO.

## 🎯 Objetivo
El propósito de este material es brindar una comprensión sólida de la POO en Python y la correcta implementación de la función `main()`.

## Entorno virtual python

1. Clona este repositorio.
    ``` bash
    git clone https://github.com/driosoft-pro/Programming_7b_IntroPOO.git
    ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate "Linux"
   venv\Scripts\activate  	"Windows"

## Creacion de clase POO

## 📖 Descripción
Este proyecto contiene una implementación básica de Programación Orientada a Objetos (POO) en Python. Se define una clase `Car` con atributos que representan las características de un carro, y se instancia un objeto con datos de un modelo específico.

## 📂 Archivos
- **`poo.py`**: Contiene la definición de la clase `Car` y un programa principal para instanciar un objeto de esta clase.

## 🏗 Estructura del Código

### 🔹 Clase `Car`

La clase `Car` se define con los siguientes atributos:
- `brand`: Marca del carro.
- `model`: Modelo del carro.
- `color`: Color del carro.
- `engine_type`: Tipo de motor (Ejemplo: Gasolina, Eléctrico, Híbrido).

```python
class Car():
    def __init__(self, brand, model, color, engine_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
```

### 🔹 Creación de una Instancia

En la función `main()`, se crea un objeto `carro_1` de la clase `Car`, asignándole valores específicos.

```python
def main():
    carro_1 = Car("Renault", "Sandero", "Gris", "Gasolina")
    print(f"La marca del carro es: {carro_1.brand}")
    print(f"El modelo del carro es: {carro_1.model}")
    print(f"El color del carro es: {carro_1.color}")
    print(f"El tipo de motor del carro es: {carro_1.engine_type}")
```

## 🚀 Ejecución del Programa
Para ejecutar el programa, abre una terminal y corre el siguiente comando:

```sh
python poo.py
```

## 🔍 Resultado Esperado
Al ejecutar el programa, la salida en consola será:

```
La marca del carro es: Renault
El modelo del carro es: Sandero
El color del carro es: Gris
El tipo de motor del carro es: Gasolina
```

## 📝 Autor
**Estudiante** Deyton Riascos Ortiz

## 🔗 Referencias
- [Python Classes and Objects - W3Schools](https://www.w3schools.com/python/python_classes.asp)