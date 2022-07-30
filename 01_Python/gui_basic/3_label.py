from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("680x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    # photo2라는 변수가 함수의 실행이 종료된 이후
    # Garbage Collection(불필요한 메모리 공간해제)에 의해
    # 소멸되지 않게 전역변수로 선언해줘야한다.
    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()