"""
Autores: Maria Alejandra Garcia y Jeison Cristanco
Fecha: 29 de julio de 2025
Descripción: Este es el archivo principal que ejecuta el programa de gestión de colección.
Este programa permite a los administradores añadir, ver, buscar, editar y eliminar elementos
de una colección de libros, películas y música.
El menú principal ofrece opciones para gestionar la colección de manera eficiente.

"""

import utils.screenControlers as sc
from controllers import agregarElemento, verElementos, buscarElementos, editarElemento,eliminarElemento, gestorColecciones

def menuAdministrador():                                      
    while True:                                                   # Menú Principal
        sc.limpiarPantalla()
        print("========================================")
        print("      Administrador de Colección ")
        print("========================================")
        print("1. Añadir un Nuevo Elemento")
        print("2. Ver Todos los Elementos")
        print("3. Buscar un Elemento")
        print("4. Editar un Elemento")
        print("5. Eliminar un Elemento")
        print("6. Ver Elementos por Categoría")
        print("7. Guardar y Cargar Colección")
        print("0. Salir")
        print("========================================")
        opcion = input("Elija una opción: ").strip()
        match opcion:
            
            case "1":                                                # Menú de Opciones - Añadir un Nuevo Elemento
                agregarElemento.agregarElemento()
            case "2":                                                # Menú de Opciones - Ver Todos los Elementos
                verElementos.verElementos()
            case "3":
                buscarElementos.buscarElemento()            # Menú de Opciones - Buscar un Elemento
            case "4":
                editarElemento.editarElemento()            # Menú de Opciones - Editar un Elemento
            case "5":                                                 # Menú de Opciones - Eliminar un Elemento
                eliminarElemento.eliminarElemento()        # Llama a la función para eliminar un elemento
            case "6":                                                  # Menú de Opciones - Ver Elementos por Categoría
                verElementos.verElementos()              # Llama a la función para ver elementos por categoría
            case "7":                                            #Menú de Opciones - Guardar y Cargar Colección
                gestorColecciones.gestoresColeccion()  # Llama a la función para guardar la colección
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opción inválida")

        sc.pausar_pantalla       #pausa

if __name__ == "__main__":
    menuAdministrador()