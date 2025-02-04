sentence = input("Sentence: ").split()
acr=""
for word in sentence:
    acr=acr+word[0]
print(f"acronym is {acr}")