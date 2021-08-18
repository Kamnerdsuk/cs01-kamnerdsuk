def my_function(X) :
    for i in range(len(X)) :
        print(i)
        if (X[i] == 20) :
            X[i] = 200
    print(X)
Thislist = [5, 10, 15, 20, 25, 50, 20]
my_function(Thislist)