from tkinter import *
from tkinter import ttk
import secrets

def delete_text_insert(event):
    textbox.delete(0,"end")

def random(event):
    try:
        menulist = textbox.get()
        menu_to_listmenu = menulist.rsplit()
        menu_random = secrets.choice(menu_to_listmenu)
        label5.configure(text = menu_random, bg = "#45FF83")
        label_error.configure(text = "", bg = "#F1F1F1")
    except IndexError:
        label_error.configure(text = "กรุณาเขียนเมนู", bg = "#FF6C62")
        label5.configure(text = "", bg = "#F1F1F1")

main = Tk()
main.geometry("500x400")
main.option_add("*font", "Prompt 16")

label = Label(main, text = "กินอะไรดีน้าาา")
label.grid(row = 1 , column = 0, padx = 180)
label2 = Label(main, text = "เคยเป็นกันไหม? พอถึงเวลากินข้าวแล้ว ไม่รู้จะกินอะไรดี")
label2.config(font = ("Prompt 12"))
label2.grid(row = 2 , column = 0,)
label3 = Label(main, text = "เพราะงั้นก็ให้โปรแกรมเลือกให้สิ")
label3.config(font = ("Prompt 12"))
label3.grid(row = 3 , column = 0,)
label4 = Label(main, text = "ข้าขอเลือก")
label4.config(font = ("Prompt 12"))
label4.grid(row = 7, pady = 5)
label5 = Label(main, text = "")
label5.grid(row = 8)
label_error = Label(main,text = "")
label_error.config(font = ("Prompt 12"))
label_error.grid(row = 6)

textbox = Entry(main, width = 35, font = ('Prompt 12'))
textbox.insert(0,"กะเพราะหมู ข้าวผัดหมูสับ ไข่เจียว")
textbox.grid(row = 4, column = 0, pady = 20)
textbox.bind('<FocusIn>', delete_text_insert)

button = Button(main, text = "สุ่ม")
button.grid(row = 5)
button.bind('<Button-1>', random)
main.mainloop()
