import utils.screenControlers as sc
from utils.corefiles import readJson, writeJson
from app.config import AGREGARELEMENTO

def eliminarElemento():
    while True:
        sc.limpiarPantalla()
        print("Menú de Opciones - Eliminar un Elemento")
        print("===========================================")
        print("        Eliminar un Elemento")
        print("===========================================")

        elementos = readJson(AGREGARELEMENTO)
        if not elementos:
            print("No hay elementos registrados.")
            sc.pausar_pantalla()
            return

        print("Lista de elementos disponibles:\n")
        for i, item in enumerate(elementos, 1):
            print(f"{i}. Título: {item.get('titulo', 'Desconocido')} | Tipo: {item.get('tipo', 'N/A')} | Autor: {item.get('autor', 'N/A')} | Género: {item.get('genero', 'N/A')}")

        print("\n===========================================")
        print("¿Cómo deseas eliminar?")
        print("1. Eliminar por Título")
        print("2. Eliminar por Identificador Único")
        print("3. Regresar al Menú Principal")
        print("===========================================")
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "3":
            break

        if opcion == "1":
            criterio = input("Ingrese el Título exacto del elemento que desea eliminar: ").strip().lower()
            filtrados = [e for e in elementos if e.get("titulo", "").lower() == criterio]

            if not filtrados:
                print(" No se encontró ningún elemento con ese título.")
            else:
                for item in filtrados:
                    print(f"\n¿Deseas eliminar el siguiente elemento?\nTítulo: {item.get('titulo', 'Desconocido')}")
                    confirmar = input("Escribe 'S' para confirmar: ").strip().lower()
                    if confirmar == "s":
                        elementos.remove(item)
                        writeJson(AGREGARELEMENTO, elementos)
                        print(" Elemento eliminado exitosamente.")
                    else:
                        print("Eliminación cancelada.")

        elif opcion == "2":
            print("\n⚠️ Esta opción no está disponible porque los elementos no tienen campo 'id'.")
        else:
            print("Opción inválida.")

        sc.pausar_pantalla()
