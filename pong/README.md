# pygame
vercion del clasico juego pong echo con python y pygame

## como iniciar el juego
 
 
 ## COMO CRERAR UN ENTORNO VIRTUAL

 para crear un entorno virtual con el nombre _env_ nesesito utilizar
 un modulo de python que se llama  "venv".

 """
# en windows 
python -m venv env

# en mac/linux
python3 -m venv env
 """

 evidentemente, podemos usar cualquier nombre 
 para ponerle al entorno virtual. de aqui en adelante, 
 utilizare _env_ como nombre de entorno, pero puedes usar el que quieras

 ## como ulitizar el entorno virtual
 cuando se cra un entorno virtual se prepara unos scripts
 con utilidades par activar el entorno y un enlace simbolico a la 
 vercion de python que se va a utilizar y su vercion correspondiente
  al gestr de paquetes "pip"

para activarlo es neesario activar el gestor de la siguiente manera

"""
# en windows
.\env\Scripts\activate

# en mac/linux
source ./env/bin/activate

"""

si el entorno se ha activado correctamente veremos en el promp 
del terminal el nombre de entorno activo enttre 
parectesis en este caso veremos (env)

## gestor de paquetes :pip

- instalar un paquete nuevo: *pip install <nombre_del_paquete>
- puedo dejar los paquetes instalados: "pip list"
- puedo listar paquetes en formaro de dependencias: "pip freeze"

## como desactivar el entorno virtual

con el entorno virtual acyivado
simplemente basta con ejecutar el siguiente comando

"""
deactivate
"""

## como eliminar un entorno virtual

basta com eliminar el directoria que se a creado al inicializar 
el entorni virtual. esto elimina el entorno y todas las dependencias 
instaladas en el
