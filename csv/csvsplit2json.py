import csv
import json
import math
import os

# 将某个csv按照1000一批写入一个新的文件夹下面

def csv_to_json_batch(csv_file, batch_size,out_put_dir):
    # 如果输出文件夹不存在,那么进行创建
    if not os.path.exists(out_put_dir):
        os.makedirs(out_put_dir)
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total_rows = sum(1 for row in reader)  # 计算总行数
        file.seek(0)  # 重新定位到文件开头
        
        batch_count = math.ceil(total_rows / batch_size)  # 计算批次数
        current_batch = 1
        
        for i in range(batch_count):
            data = []
            current_batch_size = min(batch_size, total_rows - (current_batch - 1) * batch_size)
            
            # 读取当前批次的数据
            for _ in range(current_batch_size):
                row = next(reader)
                data.append(row)
            
            # 写入JSON文件
            output_file = f'{out_put_dir}_{current_batch}.json'
            with open(output_file, 'w') as output:
                json.dump(data, output, indent=4)
            
            current_batch += 1

# 使用示例
csv_to_json_batch('/tmp/0710.csv', 1000,"/tmp/b/json")
