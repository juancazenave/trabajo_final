# trabajo_final
Trabajo Final de cursada Python Coderhouse - crear un Blog
PASO 1: CLONAR Y LEVANTAR REPOSITORIO DE GITHUB
1. Dentro de Windows en nuestra maquina, creamos una carpeta, donde haremos la clonacion del proyecto
2. Dentro de esta carpeta abrimos GIT BASH, y ejecutamos el comando "git clone" + URL del Repositorio de GitHub
3. Una vez creado el Proyecto en esta carpeta, es decir, que el Proyecto se haya clonado correctamente, podemos cerrar GIT BASH

PASO 2: Utilizando el CMD (Command Prompt)
4. Desde dentro del Proyecto (es decir, nos movemos un paso mas adentro, y nos ubicamos dentro de la carpeta del Repositorio), abrimos el CMD. Al abrir el CMD nos deberia indicar que la ruta en la que esta ubicado el CMD es donde estamos parados ahora, es decir, dentro del Repositorio
5. Pasamos a instalar con el CMD, dentro del Repositorio (ahora Repositorio local), el Virtual Environment. Esto lo hacemos mediante el comando "pip install virtualenv"
6. Luego creamos nuestro entorno virtual. En este caso lo vamos a llamar "venv". Para eso ejecutamos el comando "virtualenv venv"
7. Luego activamos el Virtual Environment, con el comando "venv\Scripts\activate"
8. Instalamos todas las depedencias, tambien llamados "requirements", mediante el comando "pip install -r requirements.txt"
9. Instalamos django con el comando: "pip install django"

PASO 3: Desde VISUAL STUDIO CODE
10. Abrimos el VSC, y desde el VSC abrimos la carpeta del Repositorio Local. Al abrir la carpeta, desde la Terminal que se nos abra, deberiamos encontrarnos dentro del ambiente virtual (venv). Pero, si quizas no se diera esto, por las dudas, deberemos repetir los pasos 7 y 9, dentro de VSC, desde la Terminal.
11. Hacemos las migraciones correspondientes. Para eso ejecutamos primero: "python manage.py makemigrations". Luego ejecutamos el comando: "python manage.py migrate"
12. Luego, estamos en condiciones de correr el servidor, con el comando: "python manage.py runserver". Si no hay errores, la misma Terminal nos dara un URL, desde donde podemos acceder al sitio Web que se esta programando. "http://127.0.0.1:8000/". Hacemos click en el link, y nos llevara al sitio Web. Inicialmente, desde esta direccion "cruda" no veremos nada. Pero si a la direccion le agregamos la palabra "blog", nos llevara al sitio Web: "http://127.0.0.1:8000/blog". 
13. Tambien podemos crear un usuario con permisos de administrador, mediante el comando "python manage.py createsuperuser". Se pedira un nombre de usuario, email (opcional), y password. Para acceder como administrador, se debera acceder desde el sitio Web + "/admin", es decir, "http://127.0.0.1:8000/admin", y desde aqui se podra iniciar sesion con el usuario y password creados, y ver los registros en las bases de datos.

MI PROYECTO es un Blog de Posts en Ingles, de articulos de temas de interes general en ingles. Este blog tiene su propio registro y login de usuarios. Cada Post que quieran realizar, le pueden agregar un Titulo, una Introduccion, un Cuerpo de Desarrollo, y tambien agregar imagenes en cada Post. Estos Posts sera posible editarlos e incluso eliminarlos, si estan loggeados al sitio Web.
Tambien se incluye una seccion de actualizacion de datos de perfil y la posibilidad de subir una imagen de AVATAR, que se podra visualizar end la barra de navegacion cada vez que se inicie sesion.

LINK AL VIDEO EXPLICATIVO de mi BLOG: 
https://youtu.be/SqsZlGLNLTs

NOTA: al crear un usuario y password nuevos, la edicion del Avatar fallara! esto se debe a que hay un solo superuseresto lo hable con los chicos de CoderAsk y habria que hacer una re-edicion del usuario a traves de una clase usuario, como se indica en el video a continuacion: https://www.youtube.com/watch?v=lNxQkW1kjto
Por todo esto, indico que el USUARIO Y PASSWORD a utilizar son: 
SUPERUSER: juancazenave
PSW: coder48265
