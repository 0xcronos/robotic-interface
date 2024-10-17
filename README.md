# Interfaz Robótica para Automatización de Reciclaje

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]

El presente proyecto tiene como propósito el desarrollo de un sistema automatizado para la clasificación 
y detección de materiales reciclables utilizando una red neuronal convolucional y la programación de un 
brazo robótico para la manipulación y colocación de los materiales en diferentes contenedores. 
El objetivo principal del proyecto es la clasificación de los materiales en diferentes categorías, 
como cartón, papel o plástico. 

El sistema se implementará en una banda transportadora, donde los materiales reciclables serán transportados
para su posterior clasificación. La red neuronal convolucional será entrenada con imágenes de diferentes 
materiales para que pueda identificar y clasificar los materiales con precisión. El brazo robótico, por su parte,
estará equipado con actuadores y un sistema de visión para detectar y agarrar los materiales de manera segura y precisa.

Una vez que los materiales sean clasificados, el brazo robótico los colocará en diferentes contenedores, cada uno 
destinado para un tipo específico de material reciclable. La implementación de este sistema automatizado tiene como
objetivo reducir la cantidad de residuos que terminan en los vertederos, promoviendo así la gestión sostenible de los
residuos y la conservación del medio ambiente.


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
    # Utilizar esta opción si source = tcp://127.0.0.1:8888.

    cd robotic-interface/brain/src/
    ./runner.sh
    
    # Opción 2: Inicio manual
    # Utilizar esta opción si source = 0 (config para cámaras USB)

    cd robotic-interface/brain/
    source venv/bin/activate
    cd src/
    python3 main.py
    ```
    
[contributors-shield]: https://img.shields.io/github/contributors/0xCronos/robotic-interface.svg?style=for-the-badge
[contributors-url]: https://github.com/0xCronos/robotic-interface/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/0xCronos/robotic-interface.svg?style=for-the-badge
[forks-url]: https://github.com/0xCronos/robotic-interface/network/members
[stars-shield]: https://img.shields.io/github/stars/0xCronos/robotic-interface.svg?style=for-the-badge
[stars-url]: https://github.com/0xCronos/robotic-interface/stargazers
