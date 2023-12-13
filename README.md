# Interfaz Robótica para Automatización de Reciclaje

El proyecto tiene como propósito el desarrollo de un sistema automatizado 
para la clasificación y detección de materiales reciclables como cartón, papel o plástico.

![Interfaz Robótica](https://i.ibb.co/GP84JZz/20231213-000343.webp)

## Configuración Inicial

### Requisitos del Sistema

- python 3.11+
- python3-full

### Configuración del Entorno de Desarrollo

1. Paso 1: Instala las dependencias del proyecto.
    ```bash
    npm install
    ```

2. Paso 2: Configura las variables de entorno necesarias.
    ```bash
    cp .env.example .env
    ```

    Completa el archivo `.env` con tus configuraciones.

3. Paso 3: Inicia el servidor de desarrollo.
    ```bash
    npm start
    ```

## Arquitectura Física

![Diagrama de Componentes](https://i.ibb.co/0qhVxth/Arquitectura-general.png)

El componente principal de la interfaz robótica es el Raspberry pi 4 model b+, operando como el servidor 
en el cual se ejecuta este programa. El Raspberry pi es el encargado de controlar y orquestar el 
funcionamiento del brazo robótico, el detector de objetos, la banda transportadora y el sensor de proximidad.

## Diagrama de Flujo

![Diagrama de Flujo](https://i.ibb.co/2yFRsQz/diagrama-flujo.png)

El funcionamiento general del sistema robótico es detallado en el diagrama de flujo general.

## Diagrama de Clases UML

![Diagrama de Clases UML](https://i.ibb.co/42nkDrb/UML-robotic-interface.png)
