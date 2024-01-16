import os
import requests
from tqdm import tqdm

print(f"欢迎！想必您流量非常多余，您想要将其挥霍掉。我们为您准备了大小足足为10GB的文件以便您更好地浪费您的流量。")
print(f"下面是一些注意事项：")
print(f"如果您想要浪费VPN流量，请务必打开“全局代理”，否则这10GB流量均不会对您的VPN剩余流量产生任何影响。")
print(f"挥霍流量的期间，会占用您一定的C盘空间（最高占用为10GB），请在挥霍流量前做好准备工作。")
input("如果您准备好了，就请按Enter开始挥霍流量...")


def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open(save_path, 'wb') as file, tqdm(
        desc="挥霍进度",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=block_size):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件 {file_path} 已删除。")
        input(f"流量浪费结束，本次共浪费10GB流量，请按Enter退出。")
    else:
        print(f"错误：文件 {file_path} 不存在，清理失败。")
        input(f"流量浪费结束，本次共浪费10GB流量，请按Enter退出。")


def main():
    url = "https://i0.hdslb.com/bfs/new_dyn/feb043c38fe2cf16502fe6cb4bfd7552401742377.png"
    download_folder = os.path.expanduser("~/Downloads")  # 获取当前用户的下载文件夹路径
    file_name = url.split("/")[-1]  # 从URL中获取文件名

    save_path = os.path.join(download_folder, file_name)

    download_file(url, save_path)
    print(f"成功下载文件：{save_path} ，开始清理刚刚占用的C盘空间...")

    # 删除文件
    delete_file(save_path)


if __name__ == "__main__":
    main()
