import os
from utils.corefiles import readJson, writeJson
from app.config import AGREGARELEMENTO
import utils.screenControlers as sc

def gestoresColeccion():
    while True:
        sc.limpiarPantalla()
        print("========================================")
        print("          Guardar y Cargar Colección ")
        print("========================================")
        print("¿Qué deseas hacer?")
        print("1. Guardar la Colección Actual")
        print("2. Cargar una Colección Guardada")
        print("0. Regresar al Menú Principal")
        print("========================================")
        buscOpcion = input("Seleccione una opción: ").strip()

        match buscOpcion:
            case "1":
                guardarColeccion()
            case "2":
                cargarColeccion()
            case "0":
                break
            case _:
                print("Opción inválida.")
                sc.pausar_pantalla()

def guardarColeccion():                                       #Guardar coleccion 
    print("\n= Guardar la Colección Actual ")
    nombre = input("Ingresa un nombre para guardar Coleccion: ").strip()
    if not nombre:
        print("Nombre inválido.")
        return

    coleccionPersonalizada = f"data/{nombre}.json"           # Aqui se pide que lo guarde en un archivo json de "nombre" que se pide en input


    try:
        coleccionActual = readJson(AGREGARELEMENTO)
        writeJson(coleccionPersonalizada, coleccionActual)
        print(f"Colección guardada como '{nombre}.json'")
    except Exception as e:
        print(f"Error al guardar: {e}")

    #    #necesito que al momento de guardar la coleccion, el otro principal quede vacio
    try:
        writeJson(AGREGARELEMENTO, [])  # Limpia la colección principal
        print("Colección principal vaciada.")
    except Exception as e:
        print(f"Error al vaciar la colección principal: {e}")
    input("Presione Enter para continuar...")  # Pausa para que el usuario vea el mensaje
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    print("Colección guardada y vaciada correctamente.")

    #para cargar una coleccion
def cargarColeccion():
    print("\n= Cargar una Colección ")
    nombre = input("Ingresa el nombre del archivo a cargar (sin .json): ").strip()
    if not nombre:
        print("Nombre inválido.")
        return
    coleccionPersonalizada = f"data/{nombre}.json"           
    try:
        coleccionCargada = readJson(coleccionPersonalizada)
        writeJson(AGREGARELEMENTO, coleccionCargada)
        print(f"Colección '{nombre}.json' cargada correctamente.")
    except FileNotFoundError:
        print(f"Archivo '{nombre}.json' no encontrado.")
    except Exception as e:
        print(f"Error al cargar la colección: {e}")

    input("Presione Enter para continuar...")  
    sc.limpiarPantalla()  
    print("Colección cargada correctamente.")