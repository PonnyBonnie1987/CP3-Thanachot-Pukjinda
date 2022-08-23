from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBox2.get()) / math.pow(float(textBox.get())/100,2)
    labelresult.configure(text=BMI)

MainWindows = Tk()

labelHeight = Label(MainWindows, text="ส่วนสูง (cm.)").grid(row=0, column=0)
textBox = Entry(MainWindows)
textBox.grid(row=0, column=1)

labelWeight = Label(MainWindows, text="น้ำหนัก (kg)").grid(row=1,column=0)
textBox2 = Entry(MainWindows)
textBox2.grid(row=1, column=1)

calculateButton = Button(MainWindows,text="คำนวณ")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>', leftClickButton)

labelresult = Label(MainWindows,text="ผลลัพธ์")
labelresult.grid(row=2,column=1)

MainWindows.mainloop()