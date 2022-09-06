from pytube import Playlist, YouTube
import os
#descpription
print("mp3 files are downloaded as mp4!!!!")
mp3_mp4 = input("Do you want a mp3(audio only) file or mp4(video) file?( type in |mp3| or |mp4|): ")
video_or_playlist = input("Do you want to download a video or a playlist?( type in |video| or |playlist|): ")
#making a new file
newpath = r'C:\Program Files\george_program'
if not os.path.exists(newpath):
    os.makedirs(newpath)

def on_progress(stream,chunk,bytes_remaining):
    print(100 -  (bytes_remaining/stream.filesize * 100))
def on_complete(stream,filepath):
    print("download complete")
    print(filepath)
#downloading mp4
if mp3_mp4 == "mp4":
    if video_or_playlist == "video":
        url_video = input("Enter video url: ")
        yt = YouTube(url_video,on_complete_callback= on_complete,on_progress_callback= on_progress)
        yt.streams.get_highest_resolution().download(newpath)
    elif video_or_playlist == "playlist":
        url_playlist = input("Enter playlist url: ")
        playlist = Playlist(url_playlist)
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(newpath)
#downloading mp3
elif mp3_mp4 == "mp3":
    if video_or_playlist == "video":
        url_video = input("Enter video url: ")
        yt = YouTube(url_video,on_progress_callback= on_progress, on_complete_callback= on_complete)
        yt.streams.get_audio_only().download(newpath)
    elif video_or_playlist == "playlist":
        url_playlist = input("Enter playlist url: ")
        playlist = Playlist(url_playlist)
        for video in playlist.videos:
            video.streams.get_audio_only().download(newpath)

