import json
import requests
from bs4 import BeautifulSoup
from itertools import cycle

url = open("prettyhtml.html") #'http://mlr.cs.umass.edu/ml/datasets.html'
#response = requests.get(url)
#content = response.content
soup = BeautifulSoup(url, 'lxml')

# print(soup.title)
# print(soup.title.get_text())
# print(soup.body)
# print(response.status_code)

tables = soup.find_all('table', {'cellpadding': '5'})
# We are targeting the table with cellpadding attribute and the attribute value
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc

table = tables[0]
names = []
for td in table.find('tr').find_all('td'):
    # print(td.text)
    names.append(td.text.strip())
# print(names)

tables2 = soup.find_all('table', {'border': '1'})
table2 = tables2[0]
pretty_html = table2
td_tag = pretty_html.find_all('p', {'class', 'normal'})
# print(td_tag)

values = []
for td in td_tag:
    # print(td)
    values.append(td.text.strip())
# print(values)

results = list(zip(cycle(names), values))

result = []
dictionary = {}
for n, v in results:
    if len(dictionary.items()) < len(names):
        dictionary[n] = v

    if len(dictionary.items()) == len(names):
        result.append(dictionary)
        dictionary = {}


with open('web_datasets.json', 'w', encoding='windows-1252') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
