import requests

url = "https://www.yuque.com/hollis666/fo22bm/kawhdmf1bkcn1gxn"
response = requests.get(url)

if response.status_code == 200:
    retStr = response.text
else:
    print("Failed to retrieve the webpage.")