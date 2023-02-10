from tkinter import *

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

frame_burger = Frame(root, relief='solid', bd=1)
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

Frame_drink = LabelFrame(root, text='음료')
Frame_drink.pack(side='right', fill='both', expand=True)
Button(Frame_drink, text='콜라').pack()
Button(Frame_drink, text='사이다').pack()

root.mainloop()