# wechatSpider
spider for wechat common account

爬取指定公众号的历史文章标题


如果要爬取其他公众号，需要利用浏览器检查模式查看Headers，修改相应的cookie和data字段里的fakeid和token

cookie用的是我的个人公众号的，不可以频繁调取，不然存在封号封ip的风险

-----------9月25日更新------------

增加了frequency control，尽量避免微信公众号的流量控制导致爬虫无法使用

如果调取过于频繁，则仍然会被微信流量控制，这时候过半个小时重新登录微信公众号，重新修改cookie，token等字段即可
