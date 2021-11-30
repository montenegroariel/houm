# Houmers Tracker

En Houm tenemos un gran equipo de Houmers que muestran las propiedades y solucionan todos los problemas que podrían ocurrir en ellas. Ellos son parte fundamental de nuestra operación y de la experiencia que tienen nuestros clientes. Es por esta razón que queremos incorporar ciertas métricas para monitorear cómo operan, mejorar la calidad de servicio y para asegurar la seguridad de nuestros Houmers.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

git clone https://github.com/montenegroariel/houm.git

cd houm

sudo docker-compose up

### Pre-requisitos 📋

_software y como instalarlas_

git

https://git-scm.com/downloads

docker

https://www.docker.com/get-started

docker-compose

https://docs.docker.com/compose/install/


### Instalación Ubuntu 20.04 🔧

```
sudo apt update
sudo apt-get install git docker docker-compose
```

## Ejecutando las pruebas ⚙️

El usuario se registra y una vez que se encuentra logeado puede enviar su ubicación. Al guardarse se relaciona con este usuario de forma automática.

Se puede importar en postman de manera local el archivo 
Houm.postman_local.json

## Test ⚙️

Correr el proyecto con docker-compose up

En la consola
```
sudo docker ps

CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS       PORTS                                                           NAMES
53ea132deb05   houm_web                 "/usr/src/app/entryp…"   30 hours ago   Up 2 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp                       houm_web_1
054ef247ff8f   postgres:12.0-alpine     "docker-entrypoint.s…"   30 hours ago   Up 2 hours   5432/tcp                                                        houm_db_1
41b7583f9021   portainer/portainer-ce   "/portainer"             5 weeks ago    Up 7 hours   8000/tcp, 9443/tcp, 0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   portainer

...
copiar el id del contenedor houm_web
...
docker exec -it <id_container> python manage.py test
...

Ejemplo:
...
docker exec -it 53ea132deb05 python manage.py test

```


Endpoints

Registro

http://0.0.0.0:8000/register/

Login

http://0.0.0.0:8000/login/

Guardar ubicación

http://0.0.0.0:8000/locations/

Obtener tiempo

http://0.0.0.0:8000/locations/time/<int:user>

Obtener velocidad y distancia filtrando por los registros con la velocidad superior a la variable.

http://0.0.0.0:8000/locations/velocity/<int:user>/<float:velocity>/



## Despliegue 📦

El proyecto se encuentra corriendo en https://houm.seostax.com

Para realizar pruebas en producción se puede importar el archivo 
Houm Seostax.postman_production.json

## Construido con 🛠️


* [Django](https://www.djangoproject.com/) - El framework web usado
* [Django Rest Framework](https://www.django-rest-framework.org/) - API Rest
* [Docker](https://www.docker.com/) - Containers
* [Postgresql](https://www.postgresql.org/) - Base de datos



## Expresiones de Gratitud 🎁

* Gracias por el template [Villanuevand](https://github.com/Villanuevand)
---
