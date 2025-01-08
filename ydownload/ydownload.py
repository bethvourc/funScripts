from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube[link]

print("Title:", yt.title)

print("NegativeComment:",yt.negativecomment)

print("Likes:", yt.likes)

yd = yt.streams.get_highest_resolution()

yd.download('user/mackbook/Desktop')
