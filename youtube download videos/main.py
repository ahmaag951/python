from pytube import YouTube
from pytube import Playlist

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)
####################################################

def Download(link):
    playlist = Playlist(link)
    print(f'Downloading Playlist: {playlist.title}')

    for video in playlist.videos:
        print(f'downloading {video.title}')
        # video.streams.first().download()
        youtubeObject = YouTube(video.watch_url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
Download(link)
