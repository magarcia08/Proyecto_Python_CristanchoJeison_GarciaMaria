import json
import os


def readJson(ruta):                                   #  Leer datos desde un archivo JSON
    if not os.path.exists(ruta):
        return []                                     # Si el archivo no existe, se retorna una lista vacía
    with open(ruta, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []                                 # Si el archivo no existe, se retorna una lista vacía


def writeJson(ruta, data):                            # Escribir datos en un archivo JSON
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)