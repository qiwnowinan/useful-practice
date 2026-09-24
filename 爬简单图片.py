import requests

URL = "https://img-s.msn.cn/tenant/amp/entityid/AA2aCn1e.img"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0"
}
params = {
    "w": "768",
    "h": "432",
    "m": "6",
    "x": "225",
    "y": "131",
    "s": "164",
    "d": "164",
}


def main():
    response = requests.get(URL, headers=headers, params=params, timeout=10)
    with open("./xx.png", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    main()
    print("下载完成")
