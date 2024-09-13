# Lista de cursos disponibles
cursos_disponibles = [
    {"id": 1, "nombre": "Matemáticas I", "descripcion": "Curso introductorio de matemáticas."},
    {"id": 2, "nombre": "Historia del Arte", "descripcion": "Estudio de la evolución del arte a través de los siglos."},
    {"id": 3, "nombre": "Programación en Python", "descripcion": "Curso de introducción a la programación en Python."}
]

# Diccionario para almacenar la matrícula de los estudiantes
matricula_estudiantes = {}

# Función para mostrar cursos disponibles
def mostrar_cursos():
    print("\nCursos Disponibles:")
    for curso in cursos_disponibles:
        print(f"ID: {curso['id']}, Nombre: {curso['nombre']}, Descripción: {curso['descripcion']}")

# Función para matricularse en un curso
def matricularse():
    estudiante = input("Introduce tu nombre: ").strip()
    if estudiante not in matricula_estudiantes:
        matricula_estudiantes[estudiante] = []

    mostrar_cursos()
    
    try:
        id_curso = int(input("Introduce el ID del curso en el que deseas matricularte: "))
        curso_encontrado = next((c for c in cursos_disponibles if c["id"] == id_curso), None)
        
        if curso_encontrado:
            if curso_encontrado["nombre"] in matricula_estudiantes[estudiante]:
                print("Ya estás matriculado en este curso.")
            else:
                matricula_estudiantes[estudiante].append(curso_encontrado["nombre"])
                print(f"Te has matriculado en: {curso_encontrado['nombre']}")
        else:
            print("ID de curso no válido.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Función para mostrar los cursos en los que un estudiante está matriculado
def mostrar_matricula():
    estudiante = input("Introduce tu nombre: ").strip()
    if estudiante in matricula_estudiantes:
        cursos = matricula_estudiantes[estudiante]
        if cursos:
            print(f"\nCursos en los que estás matriculado, {estudiante}:")
            for curso in cursos:
                print(f"- {curso}")
        else:
            print("No estás matriculado en ningún curso.")
    else:
        print("No se encontró tu nombre en el sistema.")

# Función principal para ejecutar el programa
def main():
    while True:
        print("\nMenú:")
        print("1. Mostrar Cursos Disponibles")
        print("2. Matricularse en un Curso")
        print("3. Mostrar Cursos Matriculados")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")
        
        if opcion == "1":
            mostrar_cursos()
        elif opcion == "2":
            matricularse()
        elif opcion == "3":
            mostrar_matricula()
        elif opcion == "4":
            print("Gracias por usar el sistema de matriculación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
