def cal():
    r = int(tb1.get())
    circle = (3.14)*r*r
    messagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์%.2f " % circle)
    result.set(circle)

from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย จิรภัทร แก่นคำ")

result = StringVar()

lb = Label(window,text="ยินดีต้อนรับเข้าสู่ python", font=("FreesiaUPC",24))
lb.place(x=50, y=10)

lb2 = Label(window,text="รับค่ารัศมี", font=("FreesiaUPC",18))
lb2.place(x=50, y=100)

lb3 = Label(window,text="ผลลัพธ์", font=("FreesiaUPC",18))
lb3.place(x=50, y=140)

tb1 = Entry()
tb1.place(x=210, y=90)

tb2 = Entry(window, textvariable=result)
tb2.place(x=210, y=150)

btn = Button(window, text="คำนวณ",font=("FreesiaUPC",20 ),command=cal)
btn.place(x=400, y=100)

window.mainloop()