from msilib.schema import ComboBox
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

values = [str(i) + "일" for i in range(1, 32)]
ComboBox = ttk.Combobox(root, height=5, values=values)
ComboBox.pack()
ComboBox.set("카드 결제일") # 최초 목록 제목 설정

readonly_ComboBox = ttk.Combobox(root, height=10, values=values, state='readonly')
readonly_ComboBox.current(0)
readonly_ComboBox.pack() # 최초 목록 제목 설정

def btncmd():
    print(ttk.Combobox.get())
    
btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()