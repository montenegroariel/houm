# Houmers Tracker

En Houm tenemos un gran equipo de Houmers que muestran las propiedades y solucionan todos los problemas que podrían ocurrir en ellas. Ellos son parte fundamental de nuestra operación y de la experiencia que tienen nuestros clientes. Es por esta razón que queremos incorporar ciertas métricas para monitorear cómo operan, mejorar la calidad de servicio y para asegurar la seguridad de nuestros Houmers.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

git clone https://github.com/montenegroariel/houm.git

cd houm

docker-compose up

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

Se puede importar en postman de manera local el archivo 
Houm.postman_local.json

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
