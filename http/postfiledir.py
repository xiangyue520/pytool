import os
import requests
import time

# 对某个文件夹下面的数据批量发送post请求json

def send_post_requests(folder_path, url,headers):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                data = file.read()

                # 发送POST请求
                response = requests.post(url, data=data, headers=headers)

                # 处理响应
                if response.status_code == 200:
                    print(f"Successfully sent data from {filename}")
                else:
                    print(f"Failed to send data from {filename}. Error: {response.text}")
                # 停滞2s,处理数据
                time.sleep(2)


headers = {
    "auth-code": "quickCEP",
    "quick-token": "token信息",
    "Content-Type": "application/json"
}
# 使用示例
send_post_requests("/tmp/b", "url", headers)
