for i in range(2,100,1):
    a = True
    for j in range(2,i//2+1,1):
        if i % j == 0:
            a = False
            break
    if a:
        print(i)