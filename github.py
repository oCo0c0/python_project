import requests
from bs4 import BeautifulSoup

url = "https://github.com/redisson/redisson/wiki/1.-%E6%A6%82%E8%BF%B0"
response = requests.get(url)
soup = BeautifulSoup( response.text, 'html.parser')
# 选择id为"wiki-body"的div
wiki_body_div = soup.find('div', id='wiki-body')

# 在wiki-body的div中，选择class为"markdown-body"的div
markdown_body_div = wiki_body_div.find('div', class_='markdown-body')

# 提取所有p标签的内容
paragraphs = [p.get_text() for p in markdown_body_div.find_all('p')]
print(paragraphs)

result = ""
for paragraph in paragraphs:
    if paragraph != '':
        result += paragraph
print(result)