def triangle():
    b = int(base.get())    
    h = int(high.get())
    a = 1/2*b*h
    messagebox.showinfo("พื้นที่สามเหลี่ยม","คำตอบ %.2f" % a)
    area.set(a)
    
from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย จิรภัทร แก่นคำ")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main , text="รับค่าฐาน:",font=("Tahoma",20) )
lb1.place(x=20, y=20)
tb1 = Entry(main, textvariable=base)
tb1.place(x=200, y=25, width=200, height=30)

lb2 = Label(main , text="รับค่าสูง:",font=("Tahoma",20) )
lb2.place(x=20, y=80)
tb2 = Entry(main, textvariable=high)
tb2.place(x=200, y=85, width=200, height=30)

btn = Button(main , text="คำนวณ:",font=("Tahoma",20), command = triangle)
btn.place(x=200, y=150)

lb3 = Label(main , text="คำตอบ:",font=("Tahoma",20) )
lb3.place(x=20, y=250)

lb4 = Label(main , bg="#556699",fg="#FFFFFF", font=("Tahoma",20), textvariable=area)
lb4.place(x=200, y=250)

main.mainloop()

