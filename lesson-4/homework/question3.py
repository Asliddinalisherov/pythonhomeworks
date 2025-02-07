txt = "abcabcdabcdeabcdefabcdefg"
vowels = 'aeiou'
result = ""
used = []
count = 0
i = 0

while i<len(txt):
    count += 1
    result = result + txt[i]
    # result.append[txt[i]]

    if count == 3:
        if txt[i] in vowels or txt[i] in used: #if char is vowel or used, dont count it
            count -= 1
            i+=1
            continue
        else:
            if i == len(txt)-1:
                i+=1
                continue
            result = result + "_"
            # result.append("_")
            used.append(txt[i])
            count = 0
    i+=1

print(result)
