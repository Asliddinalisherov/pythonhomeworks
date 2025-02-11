def is_prime(n):
    isprime = True
    ran = round(n**(1/2))
    for i in range(2, ran+2, 1):
        if n % i == 0:
            isprime = False
            break
    return isprime

n = int(input())
if n == 1:
    print(False)
elif n == 2 or n == 3:
    print(True)
else:
    print(is_prime(n))
    