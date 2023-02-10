from tkinter import *

from matplotlib.pyplot import text

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode='extended', height=2)
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.pack()



def btncmd():
    #삭제
    #listbox.delete(0)

    #갯수 확인
    #print('리스트에는', listbox.size(), '개가 있어요')

    #항목 확인
    print('1번쨰부터 3번쨰까지의 항목 :', listbox.get(0, 2))
    
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()
root.mainloop()