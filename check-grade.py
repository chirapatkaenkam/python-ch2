def Checkgrade():
    score = int(tb1.get())
    midterm = int(tb2.get())
    final = int(tb3.get())
    love = int(tb4.get())
    total = score+midterm+final+love
    answer.set(total)
    




from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมเช็คเกรด โดย จิรภัทร แก่นคำ")
answer=StringVar()

lb1 = Label(main , text="คะแนนเก็บ:",font=("Tahoma",16) )
lb1.place(x=10, y=30)
tb1 = Entry(main)
tb1.place(x=250, y=40)

lb2 = Label(main , text="คะแนนกลางภาค:",font=("Tahoma",16) )
lb2.place(x=10, y=90)
tb2 = Entry(main)
tb2.place(x=250, y=100)

lb3 = Label(main , text="คะแนนปลายภาค:",font=("Tahoma",16) )
lb3.place(x=10, y=150)
tb3 = Entry(main)
tb3.place(x=250, y=157)

lb4 = Label(main , text="คะแนนจิตพิสัย:",font=("Tahoma",16) )
lb4.place(x=10, y=210)
tb4 = Entry(main)
tb4.place(x=250, y=220)

lb5 = Label(main , text="คำตอบ:",font=("Tahoma",16) )
lb5.place(x=30, y=280)
tb5 = Entry(main)
tb5.place(x=250, y=300)

lb6 = Label(main ,  font=("Tahoma",16),textvariable=answer)
lb6.place(x = 281, y = 300)

btn = Button(main, text="คำนวณ", font=("Tahoma",16),command=Checkgrade)
btn.place(x=450,y=50)

main.mainloop()
