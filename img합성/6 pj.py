from tkinter import *

from matplotlib.pyplot import text

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

chkvar = IntVar()
chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar)
chkbox.select()
chkbox.pack()

chkbox2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일동안 보지 않기', variable=chkbox2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()
root.mainloop()