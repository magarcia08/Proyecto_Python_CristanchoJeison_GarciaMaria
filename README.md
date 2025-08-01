# Proyecto: **Gestión de colección (Python + JSON)**

------

- #  Administrador de  Libros, Películas y Música
  
  Una aplicación de consola creada en Python que permite gestionar una colección personal de libros, películas o música. donde  se pueden agregar contenidos favoritos con opciones para agregar, buscar, editar, eliminar y guardar colecciones en archivos JSON.
  
  Este programa ayuda a:
  - Mantener un registro ordenado de elementos 
  - Consultar detalles rápidamente (autor, género, puntuación, etc.)
  - Buscar títulos por nombre, autor o género
  - Guardar múltiples versiones de colección
  - Cargar colecciones fácilmente
  
  ---
  
  ## 📂 Estructura del Proyecto
  
  Proyecto_phyron_CristanchoJeison_GarciaMaria/
  │
  ├── main.py # Menú principal y ejecución
  │
  ├── controllers/ # Funciones principales
  │ ├── agregarElemento.py
  │ ├── verElementos.py
  │ ├── buscarElemento.py
  │ ├── editarElemento.py
  │ ├── eliminarElemento.py
  │ └── gestorColecciones.py 
  │
  
  ├──utils/
  
  │├── corefiles.py
  
  │├── screenControles.py
  
  │
  
  ├──app/
  
  │├──config.py
  
  │
  
  ├── data/
  │ ├── coleccion.json # Archivo principal
  │ ├── *.json # Otras colecciones guardadas
  │
  └── README.md
  
  
  
  ---
  
  ##  Funcionalidades
  
  ### 1. Agregar Elemento
  Permite registrar un nuevo elemento a la colección indicando:
  - Tipo: Libro, Película o Música
  - Título
  - Autor / Director / Artista
  - Género
  - Valoración
  
  ---
  
  ### 2. Ver Elementos por Categoría
  Muestra solo los elementos de un tipo específico:
  - Ver solo Libros
  - Ver solo Películas
  - Ver solo Música
  
  ---
  
  ### 3. Buscar Elemento
  Permite buscar por:
  - Título
  - Autor / Artista
  - Género
  
  Filtra resultados según lo que se escriba.
  
  ---
  
  ###  4. Ver Colección Completa
  Muestra todos los elementos registrados sin filtros.
  
  ---
  
  ###  5. Guardar y Cargar Colecciones
  - Guarda la colección activa con un nombre personalizado (`mi_libros.json`, `pelis_top.json`, etc.)
  - Carga colecciones anteriores sin perder los datos actuales
  
  ---
  
  ###  Funcionalidades adicionales (opcional)
  -  Editar elementos existentes
  -  Eliminar elementos por título o ID
  -  Persistencia en JSON
  
  
  
  ---
  
  ## Para Iniciar
  
  1. Clona o descarga el repositorio.
  2. Ejecutar `main.py`
  3. Navegae por el menú interactivo para gestionar la colección.
  
  ```bash
  python main.py
  ```

