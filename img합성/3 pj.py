from cProfile import label
from tkinter import *

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file='C:\\Users\\user\\Desktop\\project\\pj.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    label.config(text='또 만나요')

    global photo2
    photo2 = PhotoImage(file='C:\\Users\\user\\Desktop\\project\\pj2.png')
    label2.config(image=photo2)

btn = Button(root, text='클릭', command=change)
btn.pack()
root.mainloop()