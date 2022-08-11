namelist = []
systemMenu = {"ไข่ดาว":10, "ปลา":30, "ข้าวเปล่า":15}
def showBill():
    totle = 0
    print("--- My Food ---")
    for number in range(len(namelist)):
        print(namelist[number][0], namelist[number][1])
        totle = totle + namelist[number][1]
    print("ราคาทั้งหมด : ",totle)
while True:
    name = input("กรอกชื่อเมนู : ")
    if name.lower() == "exit":
        break
    else:
        namelist.append([name,systemMenu[name]])
showBill()