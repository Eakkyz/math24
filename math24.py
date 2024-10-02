#นำเข้าmodule
import tkinter as tk
import random

#สุ่มเลข
def randomnumber():
    randomlist = []
    for i in range(0,4):
        n = random.randint(1,13)
        randomlist.append(n)
    output.configure(text=randomlist)
#กำหนดขนาดจอ
window = tk.Tk()
window.title('Math 24')
window.minsize(width=400, height=400)

#ตั้งชื่อหัวข้อหน้าจอ
title = tk.Label(window, text='Math 24', font=('Arial',15), bg='#edb482')
title.pack()

#Random button
button = tk.Button(window, text='สุ่มเลข', font=('Arial',12),command=randomnumber,bg='#edb482')
button.pack()

#Show Rules
output = tk.Label(window, text='กติกาง่าย ๆ เอาตัวเลขทุกตัวมาคำนวณกันให้ได้ 24', font=('Arial',12))
output.pack()

window.mainloop()
