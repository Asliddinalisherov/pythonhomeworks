import requests
from bs4 import BeautifulSoup
with open('weather.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
soup = BeautifulSoup(html_content, 'html.parser')
for_info = soup.find_all('tr')
mylist = [i.text.replace('\n', ' ').lstrip() for i in for_info]

highest_temp = 0
highest_temp_day = ''
temp_sum = 0
sunny_days = []
for i in range(len(mylist)):
    items = mylist[i]
    item = items.split()
    if item[2] == 'Sunny':
        sunny_days.append(item[0])
    htemp = item[1].split('°')[0]
    if htemp.isdigit():
        if int(htemp) > highest_temp:
            highest_temp = int(htemp)
            highest_temp_day = item[0]
    print(items)

print('The highest temperature is:', highest_temp, 'on', highest_temp_day)
print('Sunny days are: ')
for i in sunny_days:
    print(i)

    


