import requests

def get_file_size(url):
    try:
        # 发送HEAD请求获取文件大小信息
        response = requests.head(url, allow_redirects=True)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 从头信息中获取Content-Length字段
            content_length = response.headers.get('Content-Length')
            
            # 将文件大小转换为适当的单位（如KB、MB、GB）
            size_in_bytes = float(content_length)
            size_in_kb = size_in_bytes / 1024
            size_in_mb = size_in_kb / 1024
            size_in_gb = size_in_mb / 1024

            # 返回文件大小信息
            return size_in_bytes, size_in_kb, size_in_mb, size_in_gb
        else:
            return "Error: Unable to fetch file information. Status code: {}".format(response.status_code)
    except Exception as e:
        return "Error: {}".format(str(e))

# 输入文件链接
file_url = input("请输入文件链接: ")

# 获取文件大小信息
file_size = get_file_size(file_url)

# 输出文件大小信息
print("文件大小: {} 字节, {} KB, {} MB, {} GB".format(file_size[0], file_size[1], file_size[2], file_size[3]))
