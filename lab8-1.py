from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โดย จิรภัทร แก่นคำ")
messagebox.showinfo("Hello","สวัสดีครับ")
messagebox.showwarning("เตือน","ตั้งใจเรียนด้วย")
messagebox.showerror("ผิดพลาด","โปรแกรม error")
messagebox.askquestion("confirm","คุณต้องการลบ?")
messagebox.askokcancel("confirm","คุณต้องการลบ?")
messagebox.askyesno("confirm","คุณต้องการลบ?")
messagebox.askretrycancel("confirm","คุณต้องการลบ?")

main.mainloop()

