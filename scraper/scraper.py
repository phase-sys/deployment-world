from bs4 import BeautifulSoup
import csv

with open('pcso.htm') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

table = soup.table

csv_file = open('scrape.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['LOTTO GAME', 'COMBINATIONS', 'DRAW DATE', 'JACKPOT(₱)', 'WINNERS'])


for tr in table.find_all('tr'):
    data = []
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if data:
        print("Insert > ", data)
        csv_writer.writerow(data)

csv_file.close()