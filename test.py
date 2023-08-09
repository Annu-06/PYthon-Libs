from tkinter import*
from PIL import ImageTk , Image

window=Tk()
window.title("root")

img=ImageTk.PhotoImage(Image.open("bg1"))
label=Label(image=img)
label.pack()

window.mainloop()