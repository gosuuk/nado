from msilib.schema import ComboBox
import tkinter.ttk as ttk
from tkinter import *
import time
from click import progressbar

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

# #progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text='주문', command=btncmd)
# btn.pack()
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
    for i in range(101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update() # ui 업데이트
        print(p_var2.get())
btn = Button(root, text='시작', command=btncmd)
btn.pack()


root.mainloop()