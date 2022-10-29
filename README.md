# Quotes

## Description:
___
A simple program which allows users to subscribe to a telegram bot which sends them a quote at a fixed timing everyday. A user can only subscribe or unsubscribe to the telegram bot to start/stop receiving daily quotes. no other user functionalities will be implemented for now.

This project consists of 2 main parts. The backend portion will be an API which will be used to retrieve the quotes. The RPI portion will be handling the bot script and cronjobs.

## Project Links:
___
* [Draw.io System Architecture](https://drive.google.com/file/d/1jcrfMuCnpIpcjcFCqFA2UnMr-9suBF1B/view?usp=sharing "draw.io of system architecture")
    > open in diagrams.net to view
## Tech stack used:
___
Docker
> Containerization

Kubernetes
> Container management

Raspberry Pi 4b
> Linux server running on ubuntu server. Used to host the backend server and also to run cronjobs for the bot script.

FastAPI
> Backend framework for API

