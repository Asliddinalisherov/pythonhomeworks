password = input()
n=0
for i in password:
    if i != i.upper():
       n+=1

if len(password)<8:
    print("Password is too short.")
    if n == len(password):
        print("Password must contain an uppercase letter.")
else:
    if n == len(password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")