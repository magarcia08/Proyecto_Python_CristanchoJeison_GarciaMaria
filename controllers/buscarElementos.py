# controllers/buscarElementos.py

import utils.screenControlers as sc
from utils.corefiles import readJson
from app.config import AGREGARELEMENTO

def buscarElemento():
    while True:
        sc.limpiarPantalla()
        print("========================================")
        print("          Buscar un Elemento ")
        print("========================================")
        print("¿Cómo deseas buscar?")
        print("1. Buscar por Título")
        print("2. Buscar por Autor/Director/Artista")
        print("3. Buscar por Género")
        print("0. Regresar al menú principal")
        print("========================================")
        buscOpcion = input("Seleccione una opción: ").strip()

        match buscOpcion:
            case "1":
                buscarPor("titulo", "Título")
            case "2":
                buscarPor("autor", "Autor / Director / Artista")
            case "3":
                buscarPor("genero", "Género")
            case "0":
                break
            case _:
                print("Opción inválida.")
                sc.pausar_pantalla()

def buscarPor(clave, etiqueta):
    sc.limpiarPantalla()
    coleccion = readJson(AGREGARELEMENTO)

    if not coleccion:
        print("No hay elementos registrados.")
        sc.pausar_pantalla()
        return

    termino = input(f"Ingrese el {etiqueta} a buscar: ").strip().lower()
    encontrados = []

    for e in coleccion:
        tipo = e["tipo"].lower()
        autor_label = {
            "libro": "Autor",
            "película": "Director",
            "música": "Artista"
        }.get(tipo, "Autor")

        if termino in e[clave].lower():
            encontrados.append((e, autor_label))

    if not encontrados:
        print("\nNo se encontraron coincidencias.")
    else:
        print(f"\n Resultados encontrados:\n")
        for i, (item, etiqueta_autor) in enumerate(encontrados, 1):
            print(f"{i}. Título: {item['titulo']}")
            print(f"   {etiqueta_autor}: {item['autor']}")
            print(f"   Género: {item['genero']}")
            print(f"   Valoración: {item['valoracion']}\n")

    sc.pausar_pantalla()
