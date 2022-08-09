def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        ShowMenu()
    else:
        return "Username หรือ Password ผิด"

def ShowMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("ราคารวมภาษีแล้ว : ",privat(int(input("ราคาสินค้า : "))))
    elif userSelected == 2:
        print("ราคาทั้งหมด : ",price())
    else:
        print("กรุณากรอกตัวเลข 1 - 2")

def privat(total):
    result = total + (total * 7 / 100)
    return result

def price():
    price1 = int(input("ราคาสินค้าชิ้นที่ 1 : "))
    price2 = int(input("ราคาสิ้นค้าชิ้นที่ 2 : "))
    sum = price1 + price2
    return sum

login()