import random
def jugar():
    
    numero_secreto = random.randint(1, 100)
    
    adivinado = False
    
    print("¡Bienvenido al juego del número secreto!")
    print("Adivina el número del 1 al 100")

    while not adivinado:

        intento = int(input("Ingresa un número: "))

        if intento == numero_secreto:
            print("🎉 ¡Felicidades! Adivinaste el número.")

            adivinado = True
            
        elif intento < numero_secreto:
            print("🔼 El número es mayor.")

        else:
            print("🔽 El número es menor.")

if __name__ == "__main__":
    jugar()