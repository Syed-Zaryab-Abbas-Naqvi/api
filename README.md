# Weather Dashboard Application

This is a weather dashboard application built with Flask. The application allows users to retrieve weather information based on a city name and includes additional features to add, retrieve, and delete custom tasks. The project is Dockerized for easy deployment and scalability.

## Project Overview

The main purpose of this application is to demonstrate a collaborative approach to building and deploying a web application using Docker. The application allows:
- Retrieving weather information for a specific city.
- Managing a simple to-do list with add, retrieve, and delete functionality.

## Features

- Enter a city name to get the current weather.
- Shows temperature and weather description.
  

## Files:
app.py file flask python code to develop.
index.html and weather.html for development of weather dashboard,  in templates folder.
Dockerfile and docker-compose.yml for dockerziation
requirements.txt file.

## Setup and Run the Application

## Table of Contents

1. Running the Application
2. Dockerization
3. Environment Variables
4. Testing the Application
5. Team Contributions

=> Running application:

-> Directory:
 cd C:\Users\Zergham\OneDrive\Desktop\weather-app

->Running with docker:
 docker build -t flask-weather-app .

 docker-compose up

 http://localhost:5000


=> Dockerization:

This project includes the following Docker files:

Dockerfile: Defines the base image, dependencies, and instructions to run the Flask application.
docker-compose.yml: Used for multi-container applications, including both front-end and back-end if needed.

=> Envoronment variables:

The application requires an API key for the weather API.
Registered on OpenWeatherMap to get an API key.

=> Testing the application:

Testing Features:

Add a new task by entering text in the input box and clicking "Add Task".
View the list of added tasks.
Delete a task by clicking the "Delete" button next to each task.

Docker Testing: Use the following command to view container logs:

docker-compose logs

=> Team contributions:

Ahmed Bilal Malik : Developed the Flask API and set up the initial project structure.
Muhammad Atif: Worked on front-end templates (index.html and weather.html) and added the to-do list features.
Syed Zaryab Abbas Naqvi: Created and tested the Dockerfile, as well as the docker-compose.yml, build & run application in docker and done Dockerization.
Muhammad Umar: Wrote the README documentation and assisted with final testing and troubleshooting.