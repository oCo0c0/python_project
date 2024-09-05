import requests
from bs4 import BeautifulSoup

url = "https://www.sbv.gov.vn/TyGia/faces/Aiber.jspx?_afrLoop=4578200756773891&_afrWindowMode=0&_adf.ctrl-state=s2ssddfsz_4"
headers = {
    "method": "POST",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6"
}
response = requests.get(url, headers = headers)

if response.status_code == 200:
    retStr = response.text
    # 越南银行数据解析操作
    soup = BeautifulSoup(retStr, "html.parser")
    tableElements = soup.find_all("table")
    tableElement = tableElements[4]
    tableChildrenElements = tableElement.findChildren()
    print(tableChildrenElements[0])
    print("----------------------------------------------------------------------------------------")
    print(tableChildrenElements[0].find_all("tr")[0])
    print("-------------------------------------------------------------------------------------------------")
    print(tableChildrenElements[0].find_all("tr")[2].find_all("td")[1])
    pullRate = tableChildrenElements[0].find_all("tr")[5].find_all("td")[2].find_all("span")[0].text.strip().replace(".", "")
    date = tableChildrenElements[0].find_all("tr")[2].find_all("td")[1].find_all("span")[1].text.strip().replace(".", "")

    print("Pull Rate:", pullRate)
    print("Date:", date)
else:
    print("Failed to retrieve the webpage.")
