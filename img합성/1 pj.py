from tkinter import *

root = Tk()
root.title("gosu GUI")
#root.geometry("640*480") # 가로 * 세로
root.geometry("640x480+100+300")

root.resizable(False, False) # X(너비), Y(높이) 값 변경 불까(창 크기 변경 불가)

root.mainloop()