from calculadora import sumar, restar, multiplicar, dividir

def menu():
    print("=== Calculadora Simple ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        try:
            print("Resultado:", dividir(a, b))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Opción no válida")

    print()  # línea en blanco
