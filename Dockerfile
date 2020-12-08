# Carga la imagen de docker correspondiente a alpine con python
FROM python:3.7-alpine
# Establece el entorno de trabajo
WORKDIR /code
# Guarda las variables de entorno correspondientes a flask
## La direccion del fichero a ejecutar
ENV FLASK_APP=main.py
## La direccion donde se almacenara el servidor
ENV FLASK_RUN_HOST=0.0.0.0
# Se instalan los paquetes necesarios
RUN apk add --no-cache gcc musl-dev linux-headers
# Se copian e instalan las librerias de python necesarias para ejecutar la aplicacion de flask
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Se exponen los puertos de flask y de mango-express
EXPOSE 5000 8081
# Se copian los ficheros en el contenedor
COPY . .
# Se ejecuta la aplicacion flask
CMD ["flask", "run"]
