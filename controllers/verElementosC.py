import utils.screenControlers as sc
from utils.corefiles import readJson
from app.config import AGREGARELEMENTO


def verElementos():
    while True:
        sc.limpiarPantalla()
        print("===========================================")
        print("        Ver Todos los Elementos")
        print("===========================================")
        print("¿Qué categoría deseas ver?")
        print("1. Ver Libros")
        print("2. Ver Películas")
        print("3. Ver Música")
        print("0. Regresar al Menú Principal")
        print("===========================================")
        opcion = input("Selecciona una opción : ").strip()

        tipos = {
            "1": ("libro", "Autor"),
            "2": ("película", "Director"),
            "3": ("música", "Artista")
        }

        if opcion == "0":
            break

        tipo_info = tipos.get(opcion)
        if not tipo_info:
            print("Opción inválida")
            sc.pausar_pantalla()
            continue

        tipoBuscado, etiqueta_autor = tipo_info
        coleccion = readJson(AGREGARELEMENTO)

        filtrados = [e for e in coleccion if e["tipo"].lower() == tipoBuscado]

        if not filtrados:
            print(f"No hay {tipoBuscado}s registrados")
            sc.pausar_pantalla()
            continue

        # Submenú por género
        generos = sorted(set(item["genero"] for item in filtrados))
        while True:
            sc.limpiarPantalla()
            print(f"===========================================")
            print(f"      Géneros disponibles de {tipoBuscado.capitalize()}s")
            print("===========================================")
            for i, genero in enumerate(generos, 1):
                print(f"{i}. {genero}")
            print("0. Regresar")
            print("===========================================")
            subopcion = input("Selecciona un género: ").strip()

            if subopcion == "0":
                break

            if not subopcion.isdigit() or int(subopcion) < 1 or int(subopcion) > len(generos):
                print("Opción inválida")
                sc.pausar_pantalla()
                continue

            generoSeleccionado = generos[int(subopcion)-1]
            seleccionados = [e for e in filtrados if e["genero"] == generoSeleccionado]

            sc.limpiarPantalla()
            print(f"\n{tipoBuscado.capitalize()}s del género '{generoSeleccionado}':\n")
            for i, item in enumerate(seleccionados, 1):
                print(f"{i}. Título: {item.get('titulo', 'Desconocido')}")
                print(f"   {etiqueta_autor}: {item.get('autor', 'Desconocido')}")
                print(f"   Género: {item.get('genero', 'Desconocido')}")
                print(f"   Valoración: {item.get('valoracion', 'Sin calificar')}")
                print("-----------------------------------")
            sc.pausar_pantalla()
