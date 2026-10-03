"""FocusFlow - Módulo de seguimiento de hábitos (menú de consola)."""
from tabulate import tabulate

from focusflow.modelo.habito import Habito, FRECUENCIAS_VALIDAS
from focusflow.persistencia.habito_dao import HabitoDAO

ENCABEZADOS = ["ID", "Nombre", "Descripción", "Frecuencia",
               "Meta", "Racha", "Creado"]


def solicitar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío.")


def solicitar_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


def solicitar_frecuencia():
    opciones = "/".join(FRECUENCIAS_VALIDAS)
    while True:
        frecuencia = input(f"Frecuencia ({opciones}): ").strip().capitalize()
        if frecuencia in FRECUENCIAS_VALIDAS:
            return frecuencia
        print(f"Frecuencia no válida. Elige: {opciones}.")


def mostrar_habitos(habitos):
    if habitos:
        print(tabulate([h.a_fila_tabla() for h in habitos],
                       headers=ENCABEZADOS, tablefmt="grid"))
    else:
        print("No hay hábitos para mostrar.")


def solicitar_datos_habito():
    nombre = solicitar_texto("Nombre del hábito: ")
    descripcion = solicitar_texto("Descripción: ")
    frecuencia = solicitar_frecuencia()
    meta_veces = solicitar_entero("Meta de veces por periodo: ", minimo=1)
    racha = solicitar_entero("Racha actual (días/periodos): ", minimo=0)
    return nombre, descripcion, frecuencia, meta_veces, racha


def insertar(dao):
    print("=== Registrar hábito ===")
    nombre, descripcion, frecuencia, meta, racha = solicitar_datos_habito()
    habito = Habito(nombre, descripcion, frecuencia, meta, racha)
    if dao.insertar_habito(habito) > 0:
        print("Hábito registrado correctamente.")
    else:
        print("No se pudo registrar el hábito.")


def consultar(dao):
    print("=== Consultar hábitos ===")
    print("  1) Ver todos")
    print("  2) Buscar por ID")
    print("  3) Buscar por nombre")
    opcion = solicitar_entero("Selecciona: ", minimo=1)
    if opcion == 1:
        mostrar_habitos(dao.obtener_todos_los_habitos())
    elif opcion == 2:
        habito = dao.buscar_habito_por_id(solicitar_entero("ID: ", minimo=1))
        mostrar_habitos([habito] if habito else [])
    elif opcion == 3:
        mostrar_habitos(dao.buscar_habitos_por_nombre(
            solicitar_texto("Texto a buscar: ")))
    else:
        print("Opción no válida.")


def modificar(dao):
    print("=== Modificar hábito ===")
    habito = dao.buscar_habito_por_id(solicitar_entero("ID del hábito: ", minimo=1))
    if habito is None:
        print("El hábito no existe.")
        return
    print("Hábito actual:")
    mostrar_habitos([habito])
    (habito.nombre, habito.descripcion, habito.frecuencia,
     habito.meta_veces, habito.racha_actual) = solicitar_datos_habito()
    if dao.actualizar_habito(habito) > 0:
        print("Hábito modificado correctamente.")
    else:
        print("No se realizaron cambios.")


def eliminar(dao):
    print("=== Eliminar hábito ===")
    id_habito = solicitar_entero("ID del hábito a eliminar: ", minimo=1)
    if dao.eliminar_habito_por_id(id_habito) > 0:
        print("Hábito eliminado correctamente.")
    else:
        print("El hábito no existe.")


def mostrar_menu():
    dao = HabitoDAO()
    opcion = 0
    try:
        while opcion != 5:
            print("\n==============================")
            print("  FOCUSFLOW - SEGUIMIENTO DE HÁBITOS")
            print("==============================")
            print("  1) Registrar hábito")
            print("  2) Consultar hábitos")
            print("  3) Modificar hábito")
            print("  4) Eliminar hábito")
            print("  5) Salir")
            print("==============================")
            try:
                opcion = int(input("Selecciona una opción: "))
                print()
                acciones = {1: insertar, 2: consultar, 3: modificar, 4: eliminar}
                if opcion in acciones:
                    acciones[opcion](dao)
                elif opcion == 5:
                    print("Saliendo del sistema...")
                else:
                    print("Opción no válida. Intenta nuevamente.")
            except ValueError:
                print("Opción inválida. Ingresa un número entre 1 y 5.")
    finally:
        dao.cerrar()


if __name__ == "__main__":
    mostrar_menu()
