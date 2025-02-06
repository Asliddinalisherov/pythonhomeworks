string1=input("Enter first string: ")
string2=input("Enter second string : ")
if (string2 in string1) or (string1 in string2):
    print(True)
else:
    print(False)