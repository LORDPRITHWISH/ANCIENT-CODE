from pytube import YouTube
from pytube import Playlist
from math import ceil
import sys
import threading
import os

loca='YouTube'

p = Playlist("https://youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb")


thr=4
print(f"Playlist Name : {p.title}\nChannel Name  : {p.owner}\nTotal Videos  : {p.length}\nTotal Views   : {p.views} ")
links = []
size = 0

if not os.path.exists(loca) :
    os.mkdir(loca)
    
loca=os.path.join(loca,p.title)
if not os.path.exists(loca) :
    os.mkdir(loca)


try:
    for url in p.video_urls:
        links.append(url)
except:
    print('Playlist link is not valid.')
    sys.exit(0)
size = ceil(len(links)/thr)
def split_link(links,size):
    for i in range(0,len(links),size):
        yield links[i:i+size]
link = list(split_link(links,size))

print("Downloading Started...\n")

def downloader(no,chunk):
    for i in chunk:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download(output_path=loca)
      print(f"threading {no} -->  " + filename.split('/')[-1] + ' Downloaded')

for i,n in enumerate(link) :
    t = threading.Thread(target=downloader,args=(i,n),name=f"thread {n}")
    t.start()

