empleados = {}
def agregar_empleado():
    nombre = input("ingrese el nombre del empleado: ").capitalize()
    if nombre in empleados:
        print("el empleado ya esta registrado.")
        return
    try:
        salario = float(input("ingrese el salario del empleado: "))
        if salario < 0:
            print("el salario no puede ser negativo.")
            return
        empleados[nombre] = salario
        print(f"empleado '{nombre}' agregado correctamente.")
    except ValueError:
        print("debe ingresar un valor numerico valido.")
def mostrar_empleados():
    if not empleados:
        print("no hay empleados registrados.")
        return
    print("\n lista de empleados:")
    for nombre, salario in empleados.items():
        print(f"- {nombre}: ${salario:.2f}")
def calcular_salarios():
    if not empleados:
        print("no hay empleados registrados.")
        return
    total = sum(empleados.values())
    promedio = total / len(empleados)
    print("\n resumen de salarios:")
    print(f"total de salarios: ${total:.2f}")
    print(f"promedio salarial: ${promedio:.2f}")
def menu():
    while True:
        print("\n registro de empleados ")
        print("1. agregar empleado")
        print("2. mostrar empleados")
        print("3. calcular total y promedio")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            calcular_salarios()
        elif opcion == "4":
            print("saliendo del sistema.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()