## 👋 ¡Bienvenidos usuarios a mi proyecto! registro de empleados

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un sistema básico de gestión de empleados utilizando Python. El programa permite registrar empleados junto con su salario, almacenando la información en un diccionario para mantener una estructura organizada y eficiente.

Cada empleado se guarda como una clave dentro del diccionario, mientras que su salario se almacena como valor asociado. Esta estructura facilita la administración de los datos, permitiendo realizar cálculos automáticos como el total de salarios y el promedio salarial de todos los empleados registrados.

El sistema funciona mediante un menú interactivo en consola que permite agregar empleados, visualizar la lista completa y obtener un resumen financiero general en cualquier momento.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar información estructurada.
- Aplicar funciones para organizar el programa en módulos.
- Utilizar bucles para crear un menú interactivo.
- Realizar cálculos matemáticos sobre los datos almacenados.
- Validar la entrada de datos para evitar errores.
- Simular el funcionamiento básico de un sistema de gestión de personal.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Condicionales (`if`, `elif`, `else`)
- Bucles `while`
- Bucles `for`
- Operaciones matemáticas
- Uso de la función `sum()`
- Manejo de excepciones (`try` / `except`)
- Validación de datos

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `empleados` donde:
   - La clave representa el nombre del empleado.
   - El valor representa su salario.

2. El sistema muestra un menú con las siguientes opciones:
   - Agregar empleado.
   - Mostrar empleados.
   - Calcular total y promedio salarial.
   - Salir.

3. Cuando se agrega un empleado:
   - Se valida que el salario sea un número.
   - Se evita el registro de salarios negativos.
   - Se comprueba que el empleado no esté duplicado.

4. Al calcular el resumen salarial:
   - Se obtiene el total sumando todos los salarios.
   - Se calcula el promedio dividiendo el total entre el número de empleados.

5. El programa se ejecuta continuamente hasta que el usuario decide salir.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```