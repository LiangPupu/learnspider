import requests
import time
import json
import csv

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'
parms = {
    'timestamp': int(time.time()*1000),
    'pageIndex': 1,
    'pageSize': 10,
    'language': 'zh-cn',
    'area': 'cn'
}
for i in range(100):
    parms['pageIndex']=i
    res = requests.get(url,params=parms)
    # dict1 = eval(res.text.replace('false', 'False'))
    dict1 = json.loads(res.text)
    items = dict1['Data']['Posts']
    filename = []
    for key,val in items[0].items():
        filename.append(key)
        # with open('tenxun.json', 'a', encoding='utf-8') as f:
        #     f.write(json.dumps(item, ensure_ascii=False))
        #     f.write('\n')
    with open('data2.csv', 'a', newline='', encoding='utf-8')as f:
        writer = csv.DictWriter(f, fieldnames=filename)
        writer.writeheader()
        for item in items:
            writer.writerow(item)