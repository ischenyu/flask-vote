import requests,json

# 上传文件的 URL
upload_url = 'http://127.0.0.1:5000/upload/John'

# 要上传的文件
files = {'file': open('1.jpg', 'rb')}

# 发送上传请求
response = requests.post(upload_url, files=files)

# 打印响应
print(response)
