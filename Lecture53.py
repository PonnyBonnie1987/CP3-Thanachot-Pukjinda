def Vat(total):
    result = total + (total * 7 / 100)
    return result

print(Vat(int(input("ราคา : "))))