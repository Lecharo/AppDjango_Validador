# AppDjango: Validador de CSV

## Descripción
Este proyecto es una aplicación Django que permite a los usuarios cargar archivos CSV y validar su estructura según criterios específicos.

## Requisitos técnicos
- Python 3.x
- Django 3.x (o la versión específica que estés usando)
- Otras dependencias (lista las bibliotecas adicionales si las hay)

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/Lecharo/AppDjango_Validador.git
   cd AppDjango
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```

## Ejecución

1. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

2. Abre un navegador y ve a `http://localhost:8000`

## Uso

1. Carga un archivo CSV utilizando el formulario en la página principal.
2. El sistema validará el archivo según los siguientes criterios:
   - El archivo debe tener exactamente 5 columnas.
   - Columna 1: Solo números enteros entre 3 y 10 caracteres.
   - Columna 2: Solo direcciones de correo electrónico válidas.
   - Columna 3: Solo valores "CC" o "TI".
   - Columna 4: Solo valores entre 200,000 y 1,500,000.
   - Columna 5: Cualquier valor es aceptado.
3. Los resultados de la validación se mostrarán en la página.

