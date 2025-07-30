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
        print("1. Ver Todos los Libros")
        print("2. Ver Todas las Películas")
        print("3. Ver Toda la Música")
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
        print(f"🔎 Buscando tipo: {tipoBuscado}")

        filtrados = [e for e in coleccion if e["tipo"].lower() == tipoBuscado]

        if not filtrados:
            print(f"No hay {tipoBuscado}s registrados")
        else:
            print(f"\n Lista de {tipoBuscado.capitalize()}s:\n")
            for i, item in enumerate(filtrados, 1):
                print(f"{i}. Título: {item['titulo']}")
                print(f"   {etiqueta_autor}: {item['autor']}")
                print(f"   Género: {item['genero']}")
                print(f"   Valoración: {item['valoracion']}\n")
        sc.pausar_pantalla()
