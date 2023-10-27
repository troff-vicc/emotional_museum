from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('emotional_museum.db')
cur = conn.cursor()

text = open("Сервиз кофейный.html")
soup = BeautifulSoup(text, 'lxml')

outList = []

for i in range(1, 151):
    s = soup.find(id=f"gallery1_zg_slide-{i}")
    name = s.find_all("h1", {"class": "exhibit__title"})[0].text
    data1 = str(s.find_all("div", {"class": "exhibit__chars"})[0])
    data1 = data1[::-1].replace('>', '', 1)[::-1]
    data = data1[data1.rfind('>')+1:-5]
    description = s.find_all("div", {"class": "exhibit__description"})[0].text
    outList.append((i, name, data, description))

cur.executemany("INSERT INTO exhibits VALUES(?, ?, ?, ?)", outList)
conn.commit()