import requests
from lxml import etree
import pytesseract
from PIL import Image


def load_code():
    url = 'https://so.gushiwen.org/user/login.aspx?from='
    s = requests.Session()
    r = s.get(url)
    html = etree.HTML(r.text)
    VIEWSTATE = html.xpath('//input[contains(@id, "__VIEWSTATE")]/@value')[0]
    VIEWSTATEGENERATOR = html.xpath('//input[contains(@id, "__VIEWSTATEGENERATOR")]/@value')[0]
    code_url = "https://so.gushiwen.org" + html.xpath("//div[contains(@class, 'mainreg2')]//img[contains(@id, imgCode)]/@src")[0]

    # print(VIEWSTATE, VIEWSTATEGENERATOR, code_url)

    code_content = s.get(code_url).content
    with open('./img/code.png', 'wb') as f:
        f.write(code_content)
    login(VIEWSTATE, VIEWSTATEGENERATOR, s)

def login(VIEWSTATE, VIEWSTATEGENERATOR,s):
    code = code_text()
    print(code)
    data = {
        '__VIEWSTAT': VIEWSTATE,
        '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        'email': '1094122757@qq.com',
        'pwd': '123456',
        'code': code,
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'denglu': '登录'

    }
    url = 'https://so.gushiwen.org/user/login.aspx?from https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx='
    r = s.post(url, data=data)

    print(r.text)

def code_text():
    image = Image.open('./img/code.png')
    lim = image.convert('L')
    xx = 140
    table = []
    for i in range(256):
        if i < xx:
            table.append(0)
        else:
            table.append(1)
    bim = lim.point(table, '1')
    bim.save('./img/code1.jpg')
    image1 = Image.open('./img/code1.jpg')

    text = pytesseract.image_to_string(image1)
    # print(text)
    return text


if __name__ == '__main__':
    load_code()
    # code_text()