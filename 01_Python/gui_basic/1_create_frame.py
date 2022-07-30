from tkinter import *

root = Tk()
root.title("GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+100") # 가로 * 세로 + x 좌표 + y 좌표
root.resizable(False, False) # 너비, 높이 값 변경 불가
root.mainloop()