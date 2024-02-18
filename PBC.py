import io
import requests
from lxml import etree


def get_exchange_rate():
    url = "http://wzdt.pbc.gov.cn:8080/flex-xml/flex_xml_23.xml"
    response = requests.get(url)
    data = response.content

    # 解析XML数据
    tree = etree.parse(io.BytesIO(data))
    root = tree.getroot()
    print(root)

    exchange_rate = []
    for temp in root.iter('Temp'):
        date = temp.find('date').text
        hlvalue = temp.find('hlvalue').text
        print("汇率日期:" + date, "汇率:" + hlvalue)
        exchange_rate.append((date, hlvalue))

    return exchange_rate

exchange_rate = get_exchange_rate()

print(exchange_rate)
