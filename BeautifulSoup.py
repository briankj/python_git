import bs4,requests

res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1451201174&sr=8-1&keywords=automate+the+boring+stuff+with+python')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')

print(soup.select('#addToCart > a > h5 > div > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price'))




