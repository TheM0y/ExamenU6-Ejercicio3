import json
import os
import time

# Moises Joaquin Negron Blanco

ARCHIVO = 'EMPLEADOS.json'

def cargar_empleados():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, 'r') as file:
        return json.load(file)

def guardar_empleados(lista):
    with open(ARCHIVO, 'w') as file:
        json.dump(lista, file, indent=4)

# Input con validación para evitar campos vacíos
def input_no_vacio(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        else:
            print("Este campo no puede estar vacío.")

def input_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Intente con un número entero positivo.")

def input_flotante_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Intente con un número positivo.")

def agregar_empleado():
    empleado = {
        "Nombre": input_no_vacio("Nombre: "),
        "Estado civil": input_no_vacio("Estado civil: "),
        "Antigüedad": input_entero_positivo("Antigüedad (años): "),
        "Categoría": input_no_vacio("Categoría: "),
        "Sueldo": input_flotante_positivo("Sueldo: ")
    }
    empleados = cargar_empleados()
    empleados.append(empleado)
    guardar_empleados(empleados)
    print("Empleado agregado correctamente.\n")

def eliminar_empleado():
    nombre = input_no_vacio("Nombre del empleado a eliminar: ")
    empleados = cargar_empleados()
    empleados_filtrados = [e for e in empleados if e['Nombre'].lower() != nombre.lower()]
    if len(empleados) == len(empleados_filtrados):
        print("No se encontró ningún empleado con ese nombre.")
    else:
        print("Empleado eliminado correctamente.")
    guardar_empleados(empleados_filtrados)
    print()

def mostrar_lista(etiqueta, lista):
    print(f"{etiqueta}: {[e['Nombre'] for e in lista]}")
    time.sleep(1)

def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = mezcla_directa(lista[:mid])
    derecha = mezcla_directa(lista[mid:])
    resultado = merge(izquierda, derecha, mostrar=True)
    mostrar_lista("Combinando", resultado)
    return resultado

def mezcla_equilibrada(lista):
    from collections import deque
    colas = deque([[empleado] for empleado in lista])
    paso = 1
    while len(colas) > 1:
        nueva_cola = []
        while len(colas) > 1:
            a = colas.popleft()
            b = colas.popleft()
            combinado = merge(a, b, mostrar=True)
            print(f"Paso {paso}: Combinando { [e['Nombre'] for e in a] } + { [e['Nombre'] for e in b] } → { [e['Nombre'] for e in combinado] }")
            time.sleep(1)
            nueva_cola.append(combinado)
            paso += 1
        if colas:
            nueva_cola.append(colas.popleft())
        colas = deque(nueva_cola)
    return colas[0] if colas else []

def merge(izq, der, mostrar=False):
    resultado = []
    i, j = 0, 0
    while i < len(izq) and j < len(der):
        if izq[i]['Nombre'].lower() <= der[j]['Nombre'].lower():
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    if mostrar:
        print(f"Mezclando → { [e['Nombre'] for e in resultado] }")
        time.sleep(1)
    return resultado

def consultar_empleados():
    empleados = cargar_empleados()
    if not empleados:
        print("No hay empleados registrados.\n")
        return

    while True:
        print("¿Qué método de ordenamiento desea usar?")
        print("a) Mezcla Directa")
        print("b) Mezcla Equilibrada")
        opcion = input("Opción (a/b): ").lower()
        if opcion in ('a', 'b'):
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    if opcion == 'a':
        print("Ejecutando Mezcla Directa con pasos...\n")
        empleados_ordenados = mezcla_directa(empleados)
    else:
        print("Ejecutando Mezcla Equilibrada con pasos...\n")
        empleados_ordenados = mezcla_equilibrada(empleados)

    print("\nEmpleados ordenados:")
    for e in empleados_ordenados:
        print(e)
    print()

def menu():
    print("Listado de empleados")
    while True:
        print("Menú de opciones")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Consultar archivo")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            eliminar_empleado()
        elif opcion == '3':
            consultar_empleados()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione entre 1 y 4.\n")

if __name__ == '__main__':
    menu()
