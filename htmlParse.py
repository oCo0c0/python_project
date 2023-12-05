import re
from bs4 import BeautifulSoup

# 使用 BeautifulSoup 解析 HTML
with open("parserFile.html", "r", encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

a_tags = soup.find_all("a", onclick=True)

onclick_contents = [tag["onclick"] for tag in a_tags]
print(onclick_contents)

first_fields = []
for item in onclick_contents:
    match = re.match(r"AskRestore\('([^']*)'", item)
    if match:
        first_field = match.group(1)
        first_fields.append(first_field)

print(first_fields)
