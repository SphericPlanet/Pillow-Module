from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open("imb.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label12 = Label(root, text="This is how you add Image in Tkinter Window")

root.mainloop()
