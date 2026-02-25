# INICIO

# Palabra secreta
palabra_secreta = "anabel"

# Lista para guardar letras ingresadas
letras_adivinadas = []

# Número máximo de intentos
intentos = 6

print("////////////////////////////////////")
print("   BIENVENIDO AL JUEGO DEL AHORCADO")
print("////////////////////////////////////")

# CICLO PRINCIPAL DEL JUEGO
while True:

    # PROCESO: Mostrar la palabra con guiones
    palabra_mostrada = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    print("\nPalabra:", palabra_mostrada)
    print("Intentos restantes:", intentos)

    # CONDICION: ¿La palabra está completa?
    if "_" not in palabra_mostrada:
        print("\n ¡FELICIDADES, GANASTE!")
        break

    # CONDICION: ¿Se acabaron los intentos?
    if intentos == 0:
        print("\n ¡PERDISTE!")
        print("La palabra secreta era:", palabra_secreta)
        break

    # ENTRADA: Ingresar una letra
    letra_ingresada = input("\nIngresa una letra: ").lower()

    # VALIDACIÓN: letra repetida
    if letra_ingresada in letras_adivinadas:
        print(" Ya ingresaste esa letra, intenta otra.")
        continue

    # Guardar la letra ingresada
    letras_adivinadas.append(letra_ingresada)

    # CONDICIO: ¿La letra está en la palabra?
    if letra_ingresada in palabra_secreta:
        print(" Letra correcta")
    else:
        print(" Letra incorrecta")
        intentos -= 1

# FIN DEL PROGRAMA
print("\nGracias por jugar ")