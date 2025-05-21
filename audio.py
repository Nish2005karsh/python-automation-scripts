from pytube import YouTube
url = input("YouTube URL: ")
yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
stream.download(filename="audio.mp3")
