from tkinter import *

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

frame = Frame(root)
frame.pack()

Scrollbar  = Scrollbar(frame)
Scrollbar.pack(side='right', fill='y')

listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand= Scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack()

Scrollbar.config(command=listbox.yview)

root.mainloop()