import csv
import json
# 将某个csv转换成json

csv_file = '/tmp/20230711.csv'
json_file = '/tmp/20230711.json'

data = []

# 读取 CSV 文件
with open(csv_file, 'r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# 将数据写入 JSON 文件
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)
