User = input("กรอก Username : ")
Pass = input("กรอก Password : ")
if User == "admin" and Pass == "1234":
    print("ยินดีต้อนรับสู่ SaToRu Shop")
    print("")
    print("---------------------")
    print("1. ชานม           ราคา    20 บาท")
    print("2. ชาไทย          ราคา    20 บาท")
    print("3. ชานมไข่มุก     ราคา    30 บาท")
    print("4. ช็อกโกแลต    ราคา    40 บาท")
    print("5. โกโก้            ราคา    50 บาท")
    print("---------------------")
    print("")
    num = int(input("กรุณาเลือกหมายเลข : "))
    if num == 1:
        numglass = int(input("กี่แก้วดี : "))
        totle = 20 * numglass
        print("คุณลูกค้าสั่ง ชานม", num, "แก้ว ทั้งหมดราคา",totle, "บาทคราบบ")
    elif num == 2:
        numglass = int(input("กี่แก้วดี : "))
        totle = 20 * numglass
        print("คุณลูกค้าสั่ง ชาไทย", num, "แก้ว ทั้งหมดราคา", totle, "บาทคราบบ")
    elif num == 3:
        numglass = int(input("กี่แก้วดี : "))
        totle = 30 * numglass
        print("คุณลูกค้าสั่ง ชานมไข่มุก", num, "แก้ว ทั้งหมดราคา", totle, "บาทคราบบ")
    elif num == 4:
        numglass = int(input("กี่แก้วดี : "))
        totle = 40 * numglass
        print("คุณลูกค้าสั่ง ช็อกโกแลต", num, "แก้ว ทั้งหมดราคา", totle, "บาทคราบบ")
    elif num == 5:
        numglass = int(input("กี่แก้วดี : "))
        totle = 50 * numglass
        print("คุณลูกค้าสั่ง โกโก้", num, "แก้ว ทั้งหมดราคา", totle, "บาทคราบบ")
    else:
        print("กรุณาเลือก 1 - 5 นะคราบบ")
else:
    print("Username หรือ Password ผิด กรุณาตรวจสอบใหม่อีกครั้ง")
