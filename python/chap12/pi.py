def picalc():
    nom = denom = 1
    total = 1
    inc = 0
    while True:
        yield total*2
        inc +=1
        nom *= inc
        denom *= (2*inc +1)
        total += nom / denom
        
g = picalc()
for _ in range(20):
    print(next(g))

        