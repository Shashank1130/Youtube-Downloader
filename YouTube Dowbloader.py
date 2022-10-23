# YOUTUBE DOWNLOADER

from pytube import YouTube

link = input("Enter the url of the video , which you want to downlaod: \n")

video_details = YouTube(link)  # It stores all the details of a youtube link


print("\n****** Title ******")
title = video_details.title
print(title)


print("\n****** Thumbnail Image Url ******")
thumb_nail_url = video_details.thumbnail_url
print(thumb_nail_url)


print("\n****** Download Video&Audio Together ******")
pixels = video_details.streams  # streams.all will include the video , audio and all other format, but we can download every format individully.
                                # if we will use "video_details.streams.all()" :- it will give all the option og video download, means we can download only video, only audio , audio and video together

for i in list(enumerate(pixels)):
    print(i)
print('\n')

select_pixel = int(input("In what quality you wan tto download? Select from the above indexes! \n"))

print("Downloading...")
pixels[select_pixel].download()
print("Download successfully!")



print("\n\n****** Download Audio Only ******")

audio_quality = video_details.streams.filter(only_audio=True)  # inside the parenthesis of format(), what had written the audio only , it means we can download audio only

for i in list(enumerate(audio_quality)):
    print(i)
print('\n')

select_audio = int(input("Select the audio quality!\n"))

print("Downloading...")
audio_quality[select_audio].download()
print("Downloaded successfully!")





