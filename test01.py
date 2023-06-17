# https://blog.csdn.net/python1639er/article/details/115386039
import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win)
canvas.pack()

r1 = canvas.create_rectangle(100, 30, 330, 180, fill="red", tag="one")
r2 = canvas.create_rectangle(150, 50, 200, 150, fill="green", tag=("two", "green"))
r3 = canvas.create_oval(250, 50, 300, 150, fill="green", tag=("three", "green"))

# canvas.delete(r1)
# canvas.delete(r2)
# canvas.delete(r3)
canvas.delete("green")

win.mainloop()
