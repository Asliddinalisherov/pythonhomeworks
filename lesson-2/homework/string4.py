def isPalendrome(str):
    reversedstr=str[::-1]
    if reversedstr==str:
        print(True)
    else:
        print(False)
str=input("Enter string : ")
isPalendrome(str)

