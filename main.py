import json, pprint
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'FB','TSLA']

news_tables = {}

for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    print(response)

    html = BeautifulSoup(response, 'html')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table

    break

amzn_data = news_tables['AMZN']
amzn_rows = amzn_data.findAll('tr')

# print(json.dumps(news_tables, indent=4))

for index, row in enumerate(amzn_rows):
    title = row.a.text
    timestamp = row.td.text
    print(timestamp + " " + title)