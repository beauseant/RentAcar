# RentAcar
Ejemplo de interfaz REST con el framework django

Este programa utiliza el framework sobre python django para crear una interfaz RES sobre una mini aplicación de alquiler de coches.

Se han seguido los pasos normales para crear una aplicación con dejango y posteriormente se han añadido las capacidades REST:

[Tutorial de REST sobre django] http://www.django-rest-framework.org/tutorial/

###Dependencias necesarias:

Se ha usado python 3 sobre anaconda, se necesita instalar:

    - sudo /usr/local/anaconda3/bin/pip install djangorestframework
    - sudo /usr/local/anaconda3/bin/pip install mysqlclient

##Ejecución:

    - /usr/local/anaconda3/bin/python manage.py runserver

###Ejemplos de comandos disponibles:
    - http://localhost:8000/rent/rest_car/1/  ver detalles del coche 1
    - http://localhost:8000/rent/rest_car/    ver todos los coches
    - http://localhost:8000/rent/rest_client  ver los clientes
    - http://localhost:8000/rent/rest_client/1/  ver un cliente concreto

### Hacer un put:

#### Desde un script de python:

```python
import requests
data={'car_model':'Jaguar Casi S','car_plate':'AWR456'}
r = requests.post("http://localhost:8000/rent/rest_car/", data=data, auth=('usuarioxxx','passwdusuarioxxx'))
```

#### Desde la línea de comandos:
```python
/usr/local/anaconda3/bin/http -a sblanco:1234qwerty POST http://127.0.0.1:8000/rent/rest_car/ car_model="Jaguar casi S" car_plate="3445AWS" car_date="2018-04-03T07:55:53Z"

```

### Añadir paginación a lo que devuelve:

En el settings:

REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 10
}



# Implementación sobre Docker:

En el directorio Docker se han grabado los ficheros necesarios para ejecutarlo sobre un docker:

    - docker build -t rentacar .
    - docker swarm init --advertise-addr 127.0.0.1
    - docker stack deploy -c rentacar.yml rentacar

    - Nos conectamos a: http://127.0.1.1:8000/admin/
    - Usuario admin contraseña 1234qwerty


### Comandos que pueden venir bien:
    - docker exec -it 0195d90f22f2 bash
    - docker inspect e8b5ee2b2797
    - docker swarm leave --force
    - docker rmi -f rentacar
    - docker ps
    








