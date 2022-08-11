namelist = []
pricelist = []
def showBill():
    print("--- My Food ---")
    for number in range(len(namelist)):
        print(namelist[number],pricelist[number])

def showtotle():
    totle = 0
    for sum in range(len(pricelist)):
        totle = totle + pricelist[sum]
    print("ราคาทั้งหมด : ",totle)

while True:
    name = input("กรอกชื่อเมนู : ")
    if name.lower() == "exit":
        break
    else:
        price = int(input("ราคา : "))
        namelist.append(name)
        pricelist.append(price)

showBill()
showtotle()