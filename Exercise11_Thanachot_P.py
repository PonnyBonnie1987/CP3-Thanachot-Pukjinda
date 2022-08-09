row = int(input("ความสูง : "))
for x in range(row):
    print(" "*(row - x), "*"*(x+(x+1)))
