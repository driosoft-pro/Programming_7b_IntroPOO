class pet():

    def __init__(self, name, species, age, color, sound):
        self.name = name  # Nombre de la mascota
        self.species = species  # Especie de la mascota
        self.age = age  # Edad de la mascota
        self.color = color  # Color de la mascota
        self.sound = sound  # Sonido característico de la mascota

def main():
    
    # Crear dos mascotas: una tortuga y un conejo
    pet_1 = Pet("Manchas", "Tortuga", 5, "Verde", "...")
    pet_2 = Pet("Bunny", "Conejo", 2, "Blanco", "¡Sniff sniff!")
    
    # Imprimir la información de la tortuga
    print(f"\n🐢 Mascota 1:")
    print(f"Nombre: {pet_1.name}")
    print(f"Especie: {pet_1.species}")
    print(f"Edad: {pet_1.age} años")
    print(f"Color: {pet_1.color}")
    print(f"Sonido: {pet_1.sound}")
    
    # Imprimir la información del conejo
    print(f"\n🐇 Mascota 2:")
    print(f"Nombre: {pet_2.name}")
    print(f"Especie: {pet_2.species}")
    print(f"Edad: {pet_2.age} años")
    print(f"Color: {pet_2.color}")
    print(f"Sonido: {pet_2.sound}")

if __name__ == "__main__":
    main()