X = int(input())
Y = int(input())


if (X + Y) % 2 == 0:
    if X >= 0 and Y >= 0:
        if X > Y:
            razn = (X - Y) / 2
            X -= int(razn)
            print("1")
            print(X, X, "H")
        elif Y > X:
            razn = (Y - X) / 2
            Y -= int(razn)
            print("1")
            print(Y, Y, "V")
        else:
            print(0)
    elif X >= 0 and Y <= 0:
        if X > abs(Y):
            razn = (X - Y) / 2
            X -= int(razn)
            print("1")
            print(X, X, "H")
        else:
            razn = (abs(Y) - X) / 2 + 1
            Y += int(razn)
            X += int(razn)
            print("2")
            print(X, Y, "V")
            razn = (X - Y) / 2
            X -= int(razn)
            print(X, X, "H")
    elif X <=0 and Y >= 0:
        if Y > abs(X):
            razn = (Y - X) / 2
            Y -= int(razn)
            print("1")
            print(Y, Y, "V")
        elif abs(X)>Y or abs(X)==abs(Y):
            razn = (abs(X)-Y) / 2 + 1
            Y += int(razn)
            X += int(razn)
            print("2")
            print(X, Y, "H")
            razn = (X - Y) / 2
            X -= int(razn)
            print(X, X, "V")
    elif X < 0 and Y < 0:
        if abs(X) > abs(Y) :
            razn = (abs(X) - Y) / 2 + 1
            Y += int(razn)
            X += int(razn)
            print("2")
            print(X, Y, "H")
            razn = (X - Y) / 2
            X -= int(razn)
            print(X, X, "V")
        elif abs(X) > abs(Y):
            razn = (abs(Y) - X) / 2 + 1
            Y += int(razn)
            X += int(razn)
            print("2")
            print(X, Y, "V")
            razn = (X - Y) / 2
            X -= int(razn)
            print(X, X, "H")
        elif abs(X) == abs(Y):
            razn = (abs(X) - Y) / 2 + 1
            print("3")
            print(X-1,Y+1,"V")
            Y += int(razn)
            X += int(razn)

            print(2, 0, "H")
            razn = (X - Y) / 2
            X -= int(razn)
            print(X, X, "V")

else:
    print("-1")






