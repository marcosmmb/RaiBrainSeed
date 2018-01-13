import tkinter as tk
import functions as fc
from functools import partial

def bt_click():
	phrase = inp.get()
	if phrase == "" or set(phrase) == {' '}:
		lb["text"] = "Insert a phrase first"
		lb["fg"] = "red"
		var.set("")
	elif fc.mainflow(phrase) != False :
		lb["text"] = "Your seed is:"
		lb["fg"] = "black"
		var.set(fc.mainflow(phrase))
	else:
		lb["text"] = "Your phrase has an invalid character"
		lb["fg"] = "red"
		var.set("")


window = tk.Tk()
window.title("Rai Brain Seed")
window.geometry("700x300+150+150")
window.wm_iconbitmap("icon.ico")

var = tk.StringVar()

inp = tk.Entry(window, width=70)
inp.pack(pady=30)

bt = tk.Button(window, width=20, text="Generate seed", command = bt_click)
bt.pack(pady=30)

lb = tk.Label(window, text="Click on \" Generate seed\" to check your custom seed")
lb.pack(pady=15)

show = tk.Entry(window, state='readonly', readonlybackground='white', fg='green', width=70)
show.config(textvariable=var, relief='flat')
show.pack()


window.mainloop()
