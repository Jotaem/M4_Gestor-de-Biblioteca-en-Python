import os

class Libro:
    """
    Representa un libro físico con sus atributos básicos.
    """
    def __init__(self, titulo, autor, anio_publicacion, estado="disponible"):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion
        self._estado = estado

    # Getters
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_anio_publicacion(self):
        return self._anio_publicacion

    def get_estado(self):
        return self._estado

    # Setters
    def set_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "prestado"]:
            self._estado = nuevo_estado
        else:
            print("Error: Estado no válido.")
    
    def __str__(self):
        return f'Título: {self._titulo}, Autor: {self._autor}, Año: {self._anio_publicacion}, Estado: {self._estado}'

class LibroDigital(Libro):
    """
    Representa un libro digital, que hereda de Libro y añade un formato.
    """
    def __init__(self, titulo, autor, anio_publicacion, formato, estado="disponible"):
        super().__init__(titulo, autor, anio_publicacion, estado)
        self._formato = formato
    
    # Getter y Setter para el nuevo atributo
    def get_formato(self):
        return self._formato
    
    def set_formato(self, nuevo_formato):
        self._formato = nuevo_formato

    # Polimorfismo: Sobrescritura del método __str__
    def __str__(self):
        info_base = super().__str__()
        return f'{info_base}, Formato: {self._formato}'

class Biblioteca:
    """
    Gestiona una colección de libros, permitiendo operaciones y persistencia de datos.
    """
    def __init__(self, archivo="stock_libros.txt"):
        self._libros = []
        self._archivo = archivo
        self.cargar_libros()

    def agregar_libro(self, libro):
        # Evitar duplicados por título
        if not self.buscar_libro(libro.get_titulo()):
            self._libros.append(libro)
            print(f'✅ Libro "{libro.get_titulo()}" agregado correctamente.')
        else:
            print(f'⚠️  El libro "{libro.get_titulo()}" ya existe en la biblioteca.')

    def eliminar_libro(self, titulo):
        libro_a_eliminar = self.buscar_libro(titulo)
        try:
            if not libro_a_eliminar:
                raise ValueError(f'Error: El libro "{titulo}" no se encontró en la biblioteca.')
            self._libros.remove(libro_a_eliminar)
            print(f'🗑️  Libro "{titulo}" eliminado correctamente.')
        except ValueError as e:
            print(f"Error al eliminar: {e}")

    def buscar_libro(self, titulo):
        for libro in self._libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    def listar_libros(self):
        if not self._libros:
            print("ℹ️  La biblioteca está vacía.")
            return
        
        print("\n--- Listado de Libros ---")
        for libro in self._libros:
            print(f"- {libro}")
        print("-------------------------\n")


    def marcar_libro_prestado(self, titulo):
        libro = self.buscar_libro(titulo)
        try:
            if not libro:
                raise ValueError(f'El libro "{titulo}" no existe.')
            if libro.get_estado() == "prestado":
                raise Exception(f'El libro "{titulo}" ya se encuentra prestado.')
            
            libro.set_estado("prestado")
            print(f'📖 El libro "{titulo}" ha sido marcado como prestado.')
        except (ValueError, Exception) as e:
            print(f"Error: {e}")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        try:
            if not libro:
                raise ValueError(f'El libro "{titulo}" no existe.')
            if libro.get_estado() == "disponible":
                raise Exception(f'El libro "{titulo}" ya estaba disponible.')

            libro.set_estado("disponible")
            print(f'📚 El libro "{titulo}" ha sido devuelto.')
        except (ValueError, Exception) as e:
            print(f"Error: {e}")

    def cargar_libros(self):
        try:
            with open(self._archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    # Distinguir entre Libro y LibroDigital por la cantidad de campos
                    if len(datos) == 5 and datos[4] in ["PDF", "ePub"]: # Es LibroDigital
                        titulo, autor, anio, estado, formato = datos
                        libro = LibroDigital(titulo, autor, int(anio), formato, estado)
                    elif len(datos) == 4: # Es Libro físico
                        titulo, autor, anio, estado = datos
                        libro = Libro(titulo, autor, int(anio), estado)
                    else:
                        continue # Ignorar líneas mal formateadas
                    self._libros.append(libro)
            print("🚀 Libros cargados desde el archivo.")
        except FileNotFoundError:
            print("ℹ️  Archivo 'stock_libros.txt' no encontrado. Se creará uno nuevo al salir.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_libros(self):
        try:
            with open(self._archivo, 'w', encoding='utf-8') as f:
                for libro in self._libros:
                    base_info = f"{libro.get_titulo()},{libro.get_autor()},{libro.get_anio_publicacion()},{libro.get_estado()}"
                    # Si es una instancia de LibroDigital, añadir el formato
                    if isinstance(libro, LibroDigital):
                        f.write(f"{base_info},{libro.get_formato()}\n")
                    else:
                        f.write(f"{base_info}\n")
            print("💾 Cambios guardados en 'stock_libros.txt'.")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")


def mostrar_menu():
    print("\n--- Gestor de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Ver todos los libros")
    print("4. Buscar libro")
    print("5. Marcar libro como prestado")
    print("6. Devolver libro")
    print("7. Salir")
    return input("Elige una opción: ")

def main():
    mi_biblioteca = Biblioteca()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año de publicación: ")
            es_digital = input("¿Es un libro digital? (s/n): ").lower()
            if es_digital == 's':
                formato = input("Formato (PDF, ePub, etc.): ")
                nuevo_libro = LibroDigital(titulo, autor, int(anio), formato)
            else:
                nuevo_libro = Libro(titulo, autor, int(anio))
            mi_biblioteca.agregar_libro(nuevo_libro)

        elif opcion == '2':
            titulo = input("Introduce el título del libro a eliminar: ")
            mi_biblioteca.eliminar_libro(titulo)

        elif opcion == '3':
            mi_biblioteca.listar_libros()

        elif opcion == '4':
            titulo = input("Introduce el título del libro a buscar: ")
            libro = mi_biblioteca.buscar_libro(titulo)
            if libro:
                print(f"🔍 Libro encontrado: {libro}")
            else:
                print(f'⚠️  El libro "{titulo}" no se encontró.')

        elif opcion == '5':
            titulo = input("Introduce el título del libro a prestar: ")
            mi_biblioteca.marcar_libro_prestado(titulo)
            
        elif opcion == '6':
            titulo = input("Introduce el título del libro a devolver: ")
            mi_biblioteca.devolver_libro(titulo)

        elif opcion == '7':
            mi_biblioteca.guardar_libros()
            print("👋 ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()