import random 

while True:
    
    print ("    💥JUEGO NUMERO SECRETO💥    ")
    opc = int(input("Ingrese una opcion:\n1 ➖ Iniciar juego: \n2 ➖ Terminar juego: \n : "))

    if opc == 1:

        def jugar():

            numero_secreto = random.randint(1, 500)
            adivinado = False
            intentos = 0
            max_intentos = 10

            print("¡Bienvenido al juego del número secreto!")
            print("Adivina el número del 1 al 500😉")
            print("🙌 ¡SUERTE! 🙌")

            while not adivinado:
                intento = int(input("- Ingresa un número: "))
                intentos += 1 

                if intentos >= 10: 
                    break

                if intento == numero_secreto:
                    print("🎉 ¡Felicidades! Adivinaste el número.😁")
                    adivinado = True
                elif intento < numero_secreto:
                    print("🔼 El número es mayor.🤣")
                else:
                    print("🔽 El número es menor.🤣")

            print(f"\nTotal de intentos: {intentos} 😎")

    if opc == 2:
        break

    jugar()