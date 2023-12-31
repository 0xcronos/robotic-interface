#!/bin/bash

source ../venv/bin/activate

. ./camera_streaming/conf.sh

if [[ -z $(ss -tulnp | grep 0.0.0.0:$PORT | grep libcamera-vid) ]]; then
	echo "[+] Starting streaming camera on port $PORT..."
	./camera_streaming/start_camera_stream.sh
	sleep 3
	echo "[+] Starting camera streaming on port $PORT...: Done"
else
	echo "[!] Camera streaming already running on port $PORT...: Done"
fi

echo "[+] Starting robotic interface..."
python3 main.py
