from pytube import YouTube
from pytube import Playlist
from math import ceil
import sys
# import multiprocessing
import threading
import os
import tkinter as tk
import pyperclip

playlist = ''
loca='YouTube'
# link="https://youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb"
# link="https://youtube.com/playlist?list=PLlrATfBNZ98dC-V-N3m0Go4deliWHPFwT&si=d2k-n_p_Qq2-RZ2U"
link="https://youtube.com/playlist?list=PLU2nPsAdxKWQw1qBS9YdFi9hUMazppjV7&si=s_krxyLn4KwvV2yf"


def retrive():
	global link
	root = tk.Tk()
	root.geometry("1000x200")
	root.title(" YOUTUBE DOWNLOADER ")

	def Take_input():
		global link
		link = inp.get("1.0", "end-1c")
		print(link)
		root.destroy()

	def Paste():

		inp.delete("1.0", "end-1c")
		inp.insert(tk.END, pyperclip.paste())


	def paste_run():
		global link
		link = pyperclip.paste()
		print(link)
		root.destroy()


	win=tk.Frame(root,bg="black")
	opt=tk.Frame(win,bg="black")


	l = tk.Label(win,text = "Enter the link of the playlist : ",font=('Arial Black',10),padx=12,pady=5)

	inp = tk.Text(win, height = 1,
					width = 45,
					bg = "light yellow",font=('Arial Black',15),
					padx=5,pady=10)

	run = tk.Button(opt, height = 2,
					anchor='center',
					text ="	RUN  ",
					command = lambda:Take_input(),padx=10)
	paste = tk.Button(opt, height = 2,
					anchor='center',
					text ="	PASTE  ",
					command = lambda:Paste(),padx=10)
	clip = tk.Button(opt, height = 2,
					anchor='center',
					text ="	CLIPBOARD  ",
					command = lambda:paste_run(),padx=10)
	win.pack(fill="both")
	l.pack(side="top")
	inp.pack(side="top",pady=20)
	opt.pack(side="bottom",pady=20)
	run.pack(side="left",padx=10)
	paste.pack(side="left",padx=10)
	clip.pack(side="left",padx=10)
	# Output.pack()

	tk.mainloop()




def process():

	def dirmk(nam):
		if not os.path.exists(nam) :
			os.mkdir(nam)

	global playlist,loca
	# thr=multiprocessing.cpu_count()
	
	
	thr=2

	
	print(f"Playlist Name : {playlist.title}\nChannel Name  : {playlist.owner}\nTotal Videos  : {playlist.length}\nTotal Views   : {playlist.views} ")
	links = []
	size = 0

	dirmk(loca)

	loca=os.path.join(loca,playlist.title)
	dirmk(loca)

	try:
		for url in playlist.video_urls:
			links.append(url)
	except:
		print('Playlist link is not valid.')
		retrive()
		playlist = Playlist(link)
		process()
		# sys.exit(0)
	size = ceil(len(links)/thr)
	def split_link(links,size):
		for i in range(0,len(links),size):
			yield links[i:i+size]
	playlist = list(split_link(links,size))

	print("Downloading Started...\n")

	def downloader(no,chunk):
		for i in chunk:
			yt = YouTube(i)
			ys = yt.streams.get_highest_resolution()
			# ys = yt.streams.get_by_resolution()
			filename = ys.download(output_path=loca)
			print(f"threading {no} -->  " + filename.split('/')[-1] + ' Downloaded')

	for i,n in enumerate(playlist) :
		# t = multiprocessing.Process(target=downloader,args=(i,n),name=f"thread {n}")
		t = threading.Thread(target=downloader,args=(i,n),name=f"thread {n}")
		t.start()


# if __name__ == '__main__':
# retrive()
playlist = Playlist(link)
process()