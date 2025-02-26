from pytubefix import YouTube

def main():
    video_url = input("url: ")
    output_folder = "../"
    itag = int(input("stream itag"))

    try:
        yt = YouTube(video_url)
        # stream = yt.streams.filter(res="1440p").first()
        stream = yt.streams.get_by_itag(itag)
        if stream:
            stream.download(output_folder)
        else:
            print(f"Invalid stream")
    except Exception as e:
        print(f"Error: {e}")
