str=input("Enter string: ")
leng=len(str)
vowels="euioaAOUIE"
v=0
c=0
for char in str:
    if char in vowels:
        v+=1
    else:
        c+=1
print(f"count of vowels {v} \ncount of consenonants {c}")