from pytube import YouTube
from datetime import timedelta
from pathlib import Path
import time
import os

while True:
    path = str(Path.home() / "Downloads")
    url = input('URL: ')
    try:
        video = YouTube(url)

    except:
        print(f'{url} is unavailable or not a YouTube URL.')
        print("")

    else:
        while True:
            type = str.lower(input('Audio/Video?: '))
            if type == 'audio' or type == 'video':  
                break
        print("\nProcessing...\n")
        if type == 'audio':
            result = video.streams.filter(only_audio=True).first()
            start_time = time.monotonic()
            print(f'You are about to download "{video.title}" {type}..')
            result = result.download(path)
            base, ext = os.path.splitext(result)
            new_file = base + '.mp3'
            os.rename(result, new_file)
            end_time = time.monotonic()
            print(f'\nDone downloading! Elapsed time: {timedelta(seconds=end_time - start_time)} seconds \n')

        else:
            resolution = set([str(res).split(" ")[3][5:-1] for res in video.streams.filter(file_extension="mp4",progressive=True).order_by('resolution')])
            print('Available resolution:', end=" ")
            for reso in resolution:
                print(reso, end=" ")
            print("")

            while True:
                choose_resolution = input('Choose resolution: ')
                if choose_resolution in resolution:
                    break

            result = video.streams.filter(file_extension="mp4",progressive=True, res=choose_resolution).first()
            start_time = time.monotonic()
            print(f'\nYou are about to download "{video.title}" {type}..')
            result.download(path)
            end_time = time.monotonic()
            print(f'\nDownloaded! Elapsed time: {timedelta(seconds=end_time - start_time)} seconds\n')
        
        while True:
            end = input('Exit the program?(y/n): ')
            if end == 'y' or end == 'n':
                break
            break
        print("\n"*40)
        if end == 'y':
            exit()