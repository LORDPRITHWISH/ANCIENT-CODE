import tkinter as tk
import pyperclip

link=''
def retrive():
	root = tk.Tk()
	root.geometry("1000x200")
	root.title(" YOUTUBE DOWNLOADER ")

	def Take_input():
		link = inp.get("1.0", "end-1c")
		print(link)
		root.destroy()

	def Paste():
		inp.delete("1.0", "end-1c")
		inp.insert(tk.END, pyperclip.paste())

		
	def paste_run():
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
retrive()