import tkinter


import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("gosu GUI")
root.geometry("640x480") # 가로 * 세로

# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.')
# 기차 예매 시스템이라고 가정
def warn():
    msgbox.showinfo('경고', '해당 좌석은 매진되었습니다.')
def error():
    msgbox.showinfo('에러', '결제 내역에 오류가 발생했습니다.')
def okcancel():
    msgbox.askokcancel('확인 / 취소', '해당 좌석은 유아동반석입니다. 예매하시겠습니까?.')
def retrycancel():
    msgbox.askokcancel('재시도 / 취소', '일시적인 오류입니다. 다시 시도하시겠습니까?.')
def yesno():
    msgbox.askokcancel('예 / 아니요', '해당 좌석은 역방향입니다. 예매하겠습니까?.')

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()
Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니요').pack()

root.mainloop()