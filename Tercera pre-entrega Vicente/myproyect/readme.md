# Django Web con MVT

Este es un ejemplo de una aplicación web Django usando el patrón MVT que gestiona libros, autores y categorías.

## Pasos para ejecutar el proyecto

1. Clonar este repositorio.
2. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Realizar las migraciones:
    ```bash
    python manage.py migrate
    ```
4. Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Funcionalidades

- **Añadir Autor**: `http://localhost:8000/app/add-author/`
- **Añadir Categoría**: `http://localhost:8000/app/add-category/`
- **Añadir Libro**: `http://localhost:8000/app/add-book/`
- **Buscar Libros**: `http://localhost:8000/app/search-books/`