sentence = input("String: ").split()
a=''
print(f"Starts with : {sentence[0]}")
for word in sentence:
    a=word
print(f"Ends with : {a}")