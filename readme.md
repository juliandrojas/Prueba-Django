Comandos:
Instalar virtualenv: pip install virtualenv
Crear entorno virtual: virtualenv nombreEntorno
Activar entorno virtual (en Windows): \.nombreEntorno\Scripts\activate
Nota: Al activarse el entorno virtual, aparecerá entre paréntesis al lado izquierdo de la ubicación
Instalar django: pip install django
Prueba para saber si django está instalado: 
1. django-admin --version
2. python -m django --version
3. Método: django.get_version() (usado en el shell de Python)
Crear proyecto django: django-admin startproject nombreProjecto
Crear proyecto django en la misma carpeta raíz: django-admin startproject nombreProjecto . (mysite)
Ejecutar archivo manage.py: python manage.py runserver 
Nota: runserver es un comando
Ejecutar archivo manage.py en otro puerto: python manage.py runserver numeroPuerto
Lista de comandos de manage.py: python manage.py --help
Crear una aplicación dentro del proyecto: python manage.py startapp nombreAplicacion (myapp)
Mirar migraciones (cambios que se han hecho): python manage.py makemigrations (nombreModulo)
Aplicar migraciones: python manage.py migrate (nombreModulo) 
Nota: El nombre del módulo es opcional cuando se hacen y se aplican migraciones
