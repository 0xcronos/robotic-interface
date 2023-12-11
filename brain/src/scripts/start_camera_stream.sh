#!/bin/bash

# -n: automatic photo taking
# -t: duration of the streaming (0 for infinite)
# --width: width of the photo, should match the images' width of the dataset.
# --height: height of the photo, should match the images' height of the dataset.
# --framerate: amount of frames per second.
# --inline: stil figuring out what the hell is this for jijiji.
# --listen: stream the content to a tcp socket.
# & disown: run job in background and remove it from the job list of the current shell.
libcamera-vid -n -t 0 \
	--width 480 --height 640 \
	--framerate 30 --inline \
	--listen -o tcp://127.0.0.1:$PORT & disown
