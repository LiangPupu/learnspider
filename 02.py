import csv

# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['姓名', '年龄', '性别'])
#     writer.writerow(['张三', '3', '男'])
#     writer.writerows([['n','33','33'],['d','11','3'],['c','23','1']])

with open('data1.csv', 'w', newline='')as f:
    filename = ['name', 'age', 'gender']
    writer = csv.DictWriter(f, fieldnames=filename)
    writer.writeheader()
    writer.writerow({'name': 'cxk', 'gender': '男', 'age': 1})
