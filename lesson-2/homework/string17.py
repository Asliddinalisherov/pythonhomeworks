str = input("string: ")
vowels = "euioaEUIOA"

for char in str:
    if char in vowels:
        str = str.replace(char,'*')
        print(char)
print(str)