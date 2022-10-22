import requests
from bs4 import BeautifulSoup

rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')
root = BeautifulSoup(rs.content, 'html.parser')

dictionary= {}

for tr in root.select('tr[onmouseover]'):
    td_list = [td.text.strip() for td in tr.select('td')]

    # Количество ячеек в таблице со словами -- 9
    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue

    en = td_list[1]

    # Русские слова могут быть перечислены через запятую 'ты, вы',
    # а нам достаточно одного слова
    # 'ты, вы' -> 'ты'
    ru = td_list[5].split(', ')[0]

    dictionary.update({en: ru})

print(len(dictionary), dictionary)
# 2000 [('a', 'неопределенный артикль'), ('abili... , ('zero', 'ноль')]