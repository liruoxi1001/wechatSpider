# -*- coding: utf-8 -*-
import requests
import time
import csv
import pandas as pd

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
    "Cookie": "appmsglist_action_3229474268=card; pgv_pvid=2216621600; pac_uid=0_5f081d73357b9; "
              "ua_id=dzp6ksAj5d0A6R7AAAAAAGhnwYBzvBgqoFz5s8Ry7qM=; pgv_pvi=2762249216; mm_lang=zh_CN; iip=0; "
              "ptui_loginuin=769489918; RK=IczleoICZb; "
              "ptcz=4a74ba8757b457d0e0fce1f3a8e5b51c7dcd5e818fd2ba77e0eaa6b9a6faf5da; "
              "openid2ticket_ohqJuwOiHcvpjR6eqdRhfdKhIsF8=1HqAUhwJd2Gx+rIt+hFI/5LDZbbGsmj1dDPmTb6x3Yc=; rewardsn=; "
              "wxtokenkey=777; pgv_si=s4511147008; uuid=074779bbc71d53546c3a98c187cef878; "
              "rand_info=CAESIESJ5E7MV0XrPYoCYyXAX1oPvnVEvY9vfDOrTQVvaeDN; slave_bizuin=3229474268; "
              "data_bizuin=3228476038; bizuin=3229474268; "
              "data_ticket=8vYbuvWBiNtLzRz3TB3qEY6y2LV7ydEb/mF2wvyYmxp8rrws2arymv3IEE8Uq0rD; "
              "slave_sid"
              "=MGRVX1FhX1hNa2gzOFhfc1phMXJXeFpxSTdDQWpHeElpdmt0a21UZDh1Y2UzV2RmcThXRks0OTlaUjJBeVJXclNpbzVJNnZyd0NZUm1SRkJ3UjFOek9SQkI2amIzTlYxeGlMSUVLeFJUVUg3Q3FGMTN5NjRRVTFPcUpOdlc4VzFjZmFCaWViN3ZnakNpMEF1; slave_user=gh_bf104cd2a246; xid=180ea26d69c4d41d2c4ce86fe576eea3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/62.0.3202.62 "
                  "Safari/537.36",
}
data = {
    "token": "460167267",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MzI3ODY4NTA0NA==",
    "type": "9",
}
content_list = []

# 爬取 i 页
for i in range(20):
    data["begin"] = i * 5
    time.sleep(3)
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data).json()
    # 返回了一个json，里面是每一页的数据
    for item in content_json["app_msg_list"]:
        # 提取每页文章的标题及对应的url
        items = [item["title"], item["link"]]
        content_list.append(items)
    print("第" + str(i + 1) + "页爬取成功")
name = ['title', 'link']
test = pd.DataFrame(columns=name, data=content_list)
test.to_csv("wechatResult.csv", mode='w', encoding='utf-8')
print("保存成功")
