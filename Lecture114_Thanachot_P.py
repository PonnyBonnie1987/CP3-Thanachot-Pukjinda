from tkinter import *
from tkinter import ttk
from currency_converter import CurrencyConverter

currency_rate = CurrencyConverter()


def Click_convert(event):
    exchange_rate = currency_rate.convert(text_box_money.get(), text_box_from_currency.get(), text_box_to_currency.get())
    text_box_today_rate.configure(text = exchange_rate)

main = Tk()
main.title("โปรแกรมคำนวนอัตราแลกเปลี่ยน")
main.geometry("300x300")
main.option_add("*font", "Prompt 12")

label_from_currency = Label(main, text = "แปลงสกุลเงินจาก : ")
label_from_currency.grid(row = 0, column = 0)
currency = ['THB','USD','JPY']
text_box_from_currency = ttk.Combobox(main, values = currency, width= 7)
text_box_from_currency.bind("<<ComboboxSelected>>")
text_box_from_currency.grid(row = 0, column = 1, pady = 5)

label_to_currency = Label(main, text = "ไปสกุลเงิน : ")
label_to_currency.grid(row = 1, column = 0)
text_box_to_currency = ttk.Combobox(main, values = currency, width = 7)
text_box_to_currency.bind("<<ComboboxSelected>>")
text_box_to_currency.grid(row = 1, column= 1, pady = 5)

label_money = Label(main, text = "จำนวนเงิน : ",)
label_money.grid(row = 2)
text_box_money = Entry(main, width = 10)
text_box_money.grid(row = 2, column = 1)

convert_currency = Button(main, text = "แปลงค่าเงิน")
convert_currency.grid(row = 3, column = 0)
convert_currency.bind('<Button-1>', Click_convert)

label_today_rate = Label(main, text = "อัตราแลกเปลี่ยน : ")
label_today_rate.grid(row = 4, column = 0)
text_box_today_rate = Label(main, text = "")
text_box_today_rate.grid(row = 4, column = 1)

main.mainloop()