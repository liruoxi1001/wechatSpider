# -*- coding: utf-8 -*-
import requests
import time
import random
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
              "openid2ticket_ohqJuwOiHcvpjR6eqdRhfdKhIsF8=1HqAUhwJd2Gx+rIt+hFI/5LDZbbGsmj1dDPmTb6x3Yc=; "
              "pgv_info=ssid=s2282489700; pgv_si=s1788276736; uuid=0c3d564822a44282b4d202e17818a534; "
              "rand_info=CAESIKainzTr1vv8NCxK4hm3zuq8fY+jx3PkQocQqoUniVW6; slave_bizuin=3229474268; "
              "data_bizuin=3228476038; bizuin=3229474268; "
              "data_ticket=zs9gIaZwpEXH7pRpqycvj00CJZACUKqSJxMj1xLbEJGs8rKhMDaeAGRWAx595IZG; "
              "slave_sid=ZERpM0F6NVZVM2o3TUF4X0pEdW5nN1dMMEdNeFhPbGFjeEVmUVlxTHRua0VGeE5zZGh5dlVhVnB1YjcxdGtlNmtIRjg1b3VnNUVCS3RZWG9KWXdfc01ndGxtWHI1R1hIQmU1Tk94NTBJWVBQWGtnRjltMXZBSjdPY1dOdzZyZks5QkVmSzhiZDJHbjZ0V0Ix; slave_user=gh_bf104cd2a246; xid=dfb1ebf0ac942cf29f8f89e822cbd1d0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/62.0.3202.62 "
                  "Safari/537.36",
}
data = {
    "token": "614974149",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "区块链100分",
    "fakeid": "MzUxMDE1NjQ1Ng==",
    "type": "9",
}

# 存放结果
app_msg_list = []
# 在不知道公众号有多少文章的情况下，使用while语句
# 也方便重新运行时设置页数
i = 0
while True:
    begin = i * 5
    data["begin"] = str(begin)
    # 随机暂停几秒，避免过快的请求导致过快地被查到
    time.sleep(random.randint(1, 10))
    resp = requests.get(url, headers=headers, params=data, verify=False)
    print('第' + str(i + 1) + '页爬取成功')
    # 微信流量控制, 退出
    if resp.json()['base_resp']['ret'] == 200013:
        print("frequencey control, stop at {}".format(str(begin)))
        break

    # 如果返回的内容中为空则结束
    if len(resp.json()['app_msg_list']) == 0:
        print("all ariticle parsed")
        break

    app_msg_list.append(resp.json())
    # 翻页
    i += 1

info_list = []
for msg in app_msg_list:
    if "app_msg_list" in msg:
        for item in msg["app_msg_list"]:
            info = '"{}","{}","{}","{}"'.format(str(item["aid"]), item['title'], item['link'], str(item['create_time']))
            info = info.replace('<em>', '')
            info = info.replace('</em>', '')
            info_list.append(info)
# save as csv
with open("wechatResult.csv", "w", encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['id', 'title', 'link', 'time'])
    file.writelines("\n".join(info_list))
