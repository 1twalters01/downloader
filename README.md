Thing to allow me to download yt videos easily.

1. Activate the virtual environment with "source .venv/bin/activate"
2. Get the desired itags for the video and audio by running "poetry run search"
3. Download the streams with "poetry run run"
4. ffmpeg -i video.mp4 -i audio.m4a -c:v copy -c:a aac -strict experimental output.mp4
