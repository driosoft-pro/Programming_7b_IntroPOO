class Car():
    def __init__(self, brand, model, color, engine_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
        
        
def main():
    carro_1 = Car("Renault", "Sandero", "Gris", "Gasolina")
    print(f"La marca del carro es: {carro_1.brand}")
    print(f"El modelo del carro es: {carro_1.model}")
    print(f"El color del carro es: {carro_1.color}")
    print(f"El tipo de motor del carro es: {carro_1.engine_type}")
    


if __name__ == "__main__":
    main()