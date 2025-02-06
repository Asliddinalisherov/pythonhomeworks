
def istheredigit(str):
    for char in str:
        if char.isdigit():
            return True
    return False

str=input("Enter string: ")
print(istheredigit(str))

    