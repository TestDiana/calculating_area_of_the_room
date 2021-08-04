type_room = str(input())
if type_room == "треугольник":
    A = int(input())
    B = int(input())
    C = int(input())
    P = (A + B + C) / 2
    S = (P * (P - A) * (P - B) * (P - C)) ** 0.5  # площадь треугольника
    print(S)
elif type_room == "прямоугольник":
    A = int(input())
    B = int(input())
    S1 = A * B  # площадь прямоугольника
    print (S1)
elif type_room == "круг":
    r = int(input())
    S2 = 3.14 * r ** 2  # площадь круга
    print(S2)




