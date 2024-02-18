import requests
from bs4 import BeautifulSoup

url = "https://github.com/redisson/redisson/wiki/2.-%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95"
response = requests.get(url)
soup = BeautifulSoup( response.text, 'html.parser')
# 选择id为"wiki-body"的div
wiki_body_div = soup.find('div', id='wiki-body')

# 在wiki-body的div中，选择class为"markdown-body"的div
markdown_body_div = wiki_body_div.find('div', class_='markdown-body')

# 提取所有p标签的内容
#paragraphs = [p.get_text() for p in markdown_body_div.find_all('p')]
#print(paragraphs)

paragraphs = []

for child in markdown_body_div.children:
    if child.name == 'p':
        # 解析p标签的内容
        text = child.get_text()
        # 将解析后的内容添加到data列表中
        paragraphs.append(text + '\n')
    elif child.name == 'div':
        # 在div标签内部查找pre标签
        pre_tags = child.find_all('pre')
        for pre in pre_tags:
            # 解析pre标签的内容
            text = pre.get_text()
            # 将解析后的内容添加到data列表中
            paragraphs.append(text + '\n')
    elif child.name == 'h3':
        # 解析h3标签的内容
        text = child.get_text()
        # 将解析后的内容添加到data列表中
        paragraphs.append(text + '\n')

print(paragraphs)

result = ""
for paragraph in paragraphs:
    if paragraph != '':
        result += paragraph
print(result)
