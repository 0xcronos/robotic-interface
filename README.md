# Interfaz Robótica para Automatización de Reciclaje

El proyecto tiene como propósito el desarrollo de un sistema automatizado 
para la clasificación y detección de materiales reciclables como cartón, papel o plástico.

<div align="center">
  <img src="https://i.ibb.co/GP84JZz/20231213-000343.webp" alt="Diagrama de Componentes" width="987" height="865">
</div>

## Configuración Inicial

### Requisitos del Sistema
- python 3.10+
- pip

### Configuración del Entorno de Desarrollo

1. Paso 1: Instalar las dependencias del proyecto.
    ```bash
    cd robotic-interface/brain/
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Paso 2: Configurar el proyecto desde `config.yaml`
    ```bash
    # vim robotic-interface/brain/src/config.yaml
    conveyor_belt:
      serial_port: /dev/ttyUSB2
      baudrate: 9600
    braccio_arm:
      serial_port: /dev/ttyUSB1
      baudrate: 9600
    proximity_sensor:
      serial_port: /dev/ttyUSB0
      baudrate: 115200
    object_detector:
      weights_path: object_detector/best.pt
      source: tcp://127.0.0.1:8888
      device: cpu
      stream: true
      verbose: false
    ```
    Completa el archivo `config.yaml` con tus configuraciones.
   
4. Paso 3: Iniciar el programa.
    ```bash
    # Opción 1: Iniciar desde `runner.sh`.
        Utilizar esta opción si source = tcp://127.0.0.1:8888.

    cd robotic-interface/brain/src/
    ./runner.sh
    
    # Opción 2: Inicio manual
        Utilizar esta opción si source = 0 (config para cámaras USB)
        cd robotic-interface/brain/
        source venv/bin/activate
        cd src/
        python3 main.py
    ```

## Arquitectura Física

El componente principal de la interfaz robótica es el Raspberry pi 4 model b+, operando como el servidor 
en el cual se ejecuta este programa. El Raspberry pi es el encargado de controlar y orquestar el 
funcionamiento del brazo robótico, el detector de objetos, la banda transportadora y el sensor de proximidad.

![Diagrama de Componentes](https://i.ibb.co/0qhVxth/Arquitectura-general.png)

## Diagrama de Flujo General

![Diagrama de Flujo](https://i.ibb.co/2yFRsQz/diagrama-flujo.png)

## Diagrama de Clases UML

![Diagrama de Clases UML](https://i.ibb.co/42nkDrb/UML-robotic-interface.png)
