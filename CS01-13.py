B = 0
while (True) :
    A = int(input("Enter your number : "))
    if (A == -1 ) :
        print("While Break!!!")
        break
    print(A+B)
    B = A + B
