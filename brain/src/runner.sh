#!/bin/bash

. ./socket_conf.sh

echo $PORT

if [[ -z $(ss -tulnp | grep 0.0.0.0:$PORT | grep libcamera-vid) ]]; then
	echo "[+] Starting streaming camera on port $PORT..."
	./scripts/start_camera_stream.sh
	sleep 3
	echo "[+] Starting streaming camera on port $PORT...: Done"
fi

echo "[+] Starting robotic interface"
python3 rpi-camera-integration-test.py
