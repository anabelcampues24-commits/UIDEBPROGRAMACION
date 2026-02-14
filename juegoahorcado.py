# INICIO

# Palabra secreta
palabra_secreta = "python"

# Lista para guardar letras ingresadas
letras_adivinadas = []

# Número máximo de intentos
intentos = 6

print("=================================")
print("   BIENVENIDO AL JUEGO DEL AHORCADO")
print("=================================")

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

    # DECISIÓN: ¿La palabra está completa?
    if "_" not in palabra_mostrada:
        print("\n ¡FELICIDADES, GANASTE!")
        break

    