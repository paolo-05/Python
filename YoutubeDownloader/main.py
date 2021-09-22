from pytube import YouTube

link = input("Enter the link: \n")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()