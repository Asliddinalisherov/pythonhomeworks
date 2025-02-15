try:
    with open("sample.txt", mode="r") as f:
        pass
except FileNotFoundError:
    with open("sample.txt", mode="w+") as f:
        print("Type a paragraph to create sample.txt. When you done just write -1 in new line")
        while True:
            i = input()
            if i == "-1":
                break
            f.write(i + "\n")

f = open("sample.txt", mode="r")
txt = f.read()
txt = txt.replace(",","")
txt = txt.replace("\n"," ")
txt = txt.upper()
text = txt.split(" ")
while True:
    if "" in text:
        text.remove("")
    else:
        break
num = []

g = open("word_count_report.txt", "w+") # new file for report opened
g.write("Word Count Report" + "\n")
g.write(f"Total words: {len(text)}\n")
g.write("Top 5 most common words:" + "\n")
print(f"Total words: {len(text)}")
print("Top 5 most common words:")
unique_text = list(set(text))

for i in unique_text:
    num.append(text.count(i))
mydict = dict()
for key,value in zip(unique_text,num):
    mydict.update({key:value})

count = 5
while count != 0:
    for key, val in mydict.items():
        if val == max(num):
            g.write(f"{key} - {val}\n")
            print(f"{key} - {val}")
            count = count - 1
            num.remove(max(num))
            mydict.update({key:0})
            break

g.close()
f.close()