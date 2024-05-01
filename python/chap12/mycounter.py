def MyCounter(start,step):
    x = start
    while True:
        yield x
        x += step
    
    
for x in MyCounter(1,2):
    print(x,end=" ")
    if x > 100:
        break