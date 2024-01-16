import requests
import json


def get_titles(api_url):
    # 发送GET请求获取JSON数据
    response = requests.get(api_url)
    data = response.json()

    # 检查是否成功获取数据
    if data["success"]:
        # 提取并保存标题
        titles = [(entry["title"]["en"], entry["title"]["ja"])
                  for entry in data["value"]]

        # 输出带序号的英文和日文标题，按照JSON内的顺序
        for index, (en_title, ja_title) in enumerate(titles, 1):
            print(f"{index}. en-us: {en_title}, ja-jp: {ja_title}")
    else:
        print(f"请求失败: {api_url}")


# 处理免费歌曲
free_api_url = "https://webapi.lowiro.com/webapi/song/rank/free"
print("Free Songs:")
get_titles(free_api_url)

# 处理付费歌曲
paid_api_url = "https://webapi.lowiro.com/webapi/song/rank/paid"
print("\nPaid Songs:")
get_titles(paid_api_url)
