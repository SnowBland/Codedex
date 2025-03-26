import areaMethod as am


print("==================")
print("Area Calculator 📐")
print("==================")

shapeslist = ['Triangle','Rectangle','Square','Circle','Quit']

for i in range(len(shapeslist)):
    print(str(i+1)+") "+shapeslist[i])

choose = 0
while choose != 5:
    choose = int(input("Which shape: "))
    areaEquation = 0
    if choose == 1:
        height = int(input("Height:"))
        base = int(input("Base:"))
        areaEquation =  am.triangleArea(height,base)
    elif choose == 2:
        length = int(input("Length:"))
        width = int(input("Width:"))
        areaEquation = am.rectangleArea(length,width)
    elif choose == 3:
        side = int(input("Side:"))
        areaEquation = am.squareArea(side)
    elif choose == 4:
        radius = int(input("Radius:"))
        areaEquation = am.circleArea(radius)
    print(f"The area is {areaEquation}")
    




