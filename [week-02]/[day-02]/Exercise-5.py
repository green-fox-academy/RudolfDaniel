def factorio(n):
    factorio = 1
    for i in range(1, n+1):
        factorio = factorio * i
    print(factorio)

factorio(5)