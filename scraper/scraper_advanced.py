from bs4 import BeautifulSoup
import requests, csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w', newline='', encoding='utf-8')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_= 'youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except:
        yt_link = None

    print(yt_link)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()