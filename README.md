# Gestor de Biblioteca en Python

## Descripción

Este es un sistema simple de gestión de bibliotecas desarrollado en Python, como parte de la evaluación del Módulo 4 del Bootcamp Full Stack. El programa utiliza Programación Orientada a Objetos para modelar libros y una biblioteca, maneja la persistencia de datos a través de un archivo de texto y ofrece una interfaz de consola para interactuar con el sistema.

## Características

* **Clases:** `Libro`, `LibroDigital` (herencia) y `Biblioteca`.
* **Funcionalidades:** Agregar, eliminar, listar, buscar, prestar y devolver libros.
* **Persistencia de Datos:** Los datos se guardan en `biblioteca.txt` al cerrar el programa y se cargan al iniciar.
* **Manejo de Errores:** Utiliza excepciones para gestionar operaciones inválidas (ej. eliminar un libro que no existe).
* **Polimorfismo:** La clase `LibroDigital` sobrescribe métodos de la clase `Libro`.

## Cómo Ejecutar el Programa

1.  **Requisitos:**
    * Tener Python 3 instalado en tu sistema.

2.  **Archivos del Proyecto:**
    * `gestor_biblioteca.py`: El código fuente principal.
    * `stock_libros.txt`: Puedes crear este archivo en el mismo directorio para empezar con una lista de libros precargada. Si no existe, el programa lo creará al guardar.

3.  **Ejecución:**
    * Abre una terminal o línea de comandos.
    * Navega hasta el directorio donde guardaste el archivo `gestor_biblioteca.py`.
    * Ejecuta el siguiente comando:
        ```bash
        python gestor_biblioteca.py
        ```
    * Sigue las instrucciones del menú que aparecerá en la consola para gestionar la biblioteca.