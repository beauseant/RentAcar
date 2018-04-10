# Use an official Python runtime as a parent image
#FROM python:2.7-slim

FROM continuumio/anaconda3

# Set the working directory to /app
WORKDIR /data

# Copy the current directory contents into the container at /app
ADD app /data/

# Install any needed packages specified in requirements.txt
RUN apt-get install -y libmariadbclient-dev
RUN apt-get install -y gcc
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 8000
EXPOSE 8001

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD python manage.py runserver 0.0.0.0:8000

