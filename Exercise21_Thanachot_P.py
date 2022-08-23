from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBox2.get()) / math.pow(float(textBox.get())/100,2)
    labellabelresult.configure(text=BMI)
    if BMI >= 30.0:
        labellabelresult2.configure(text="อ้วนมาก")
    elif BMI >= 25.0:
        labellabelresult2.configure(text="อ้วน")
    elif BMI >= 23.0:
        labellabelresult2.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6:
        labellabelresult2.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labellabelresult2.configure(text="ผอมเกินไป")

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

labeltext1 = Label(MainWindows,text="ผลลัพธ์")
labeltext1.grid(row=4,column=0)
labeltext2 = Label(MainWindows,text="ค่า BMI : ")
labeltext2.grid(row=4,column=0)
labellabelresult = Label(MainWindows,text="")
labellabelresult.grid(row=4,column=1)
labeltext3 = Label(MainWindows,text="คุณอยู่ในเกณฑ์ : ")
labeltext3.grid(row=5,column=0)
labellabelresult2 = Label(MainWindows,text="")
labellabelresult2.grid(row=5,column=1)

MainWindows.mainloop()