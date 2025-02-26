from pytubefix import YouTube

def main():
    video_url = input("url: ")
    output_folder = "../"

    try:
        yt = YouTube(video_url)
        streams = yt.streams

        print("\n\nAudio streams")
        audio_streams = streams.filter(only_audio=True)
        for stream in streams:
            print(stream)

        print("\n\nvideo streams")
        video_streams = streams.filter(only_video=True)
        for stream in streams:
            print(stream)

    except Exception as e:
        print(f"Error: {e}")

