# eliminarElemento.py

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
        print("¿Cómo deseas eliminar?")
        print("1. Eliminar por Título")
        print("2. Eliminar por Identificador Único")
        print("3. Regresar al Menú Principal")
        print("===========================================")
        opcion = input("Selecciona una opción (1-3): ").strip()

        elementos = readJson(AGREGARELEMENTO)

        if opcion == "3":
            break

        if opcion not in ("1", "2"):
            print("⚠️ Opción inválida.")
            sc.pausar_pantalla()
            continue

        criterio = input("Ingrese el valor de búsqueda: ").strip().lower()

        if opcion == "1":
            filtrados = [e for e in elementos if e["titulo"].lower() == criterio]
        elif opcion == "2":
            filtrados = [e for e in elementos if str(e.get("id", "")).lower() == criterio]

        if not filtrados:
            print("⚠️ No se encontró ningún elemento con ese criterio.")
        else:
            for item in filtrados:
                print(f"\n¿Deseas eliminar el siguiente elemento?\nTítulo: {item['titulo']}")
                confirmar = input("Escribe 'S' para confirmar: ").strip().lower()
                if confirmar == "s":
                    elementos.remove(item)
                    writeJson(AGREGARELEMENTO, elementos)
                    print("✅ Elemento eliminado exitosamente.")
                else:
                    print("❌ Eliminación cancelada.")

        sc.pausar_pantalla()
