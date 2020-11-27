# -*- coding : utf-8 -*-
# @Time      : 2020/11/18 19:36
# @Author    : A WAYS AWAY
# @File      : 大众点评店铺.py
# @IDE       : PyCharm

import random
import requests
import xlwt

# 城市列表
list_city = [["上海", "fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0"],
             ["北京", "d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0"],
             ["广州", "e749e3e04032ee6b165fbea6fe2dafab71862f838d1255ea693b953b1d49c7c0"],
             ["深圳", "e049aa251858f43d095fc4c61d62a9ec71862f838d1255ea693b953b1d49c7c0"],
             ["天津", "2e5d0080237ff3c8f5b5d3f315c7c4a508e25c702ab1b810071e8e2c39502be1"],
             ["杭州", "91621282e559e9fc9c5b3e816cb1619c71862f838d1255ea693b953b1d49c7c0"],
             ["南京", "d6339a01dbd98141f8e684e1ad8af5c871862f838d1255ea693b953b1d49c7c0"],
             ["苏州", "536e0e568df850d1e6ba74b0cf72e19771862f838d1255ea693b953b1d49c7c0"],
             ["成都", "c950bc35ad04316c76e89bf2dc86bfe071862f838d1255ea693b953b1d49c7c0"],
             ["武汉", "d96a24c312ed7b96fcc0cedd6c08f68c08e25c702ab1b810071e8e2c39502be1"],
             ["重庆", "6229984ceb373efb8fd1beec7eb4dcfd71862f838d1255ea693b953b1d49c7c0"],
             ["西安", "ad66274c7f5f8d27ffd7f6b39ec447b608e25c702ab1b810071e8e2c39502be1"]]
# 请求头
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"]
head = {
    'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
}

# 抓取
if __name__ == '__main__':
    all_data = []
    city_name = []
    for city_list in list_city:
        city = city_list[0]
        url = city_list[1]
        base_url = "http://www.dianping.com/mylist/ajax/shoprank?rankId=" + url
        data_list = requests.get(base_url, headers=head).json()
        all_data.append(data_list)
        city_name.append([city] * len(data_list['shopBeans']))

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)

    # 设置表头
    ws.write(0, 0, label='店铺名称')
    ws.write(0, 1, label='店铺网址')
    ws.write(0, 2, label='人均消费')
    ws.write(0, 3, label='店铺星级')
    ws.write(0, 4, label='所属区域')
    ws.write(0, 5, label='食品类别')
    ws.write(0, 6, label='口味评分')
    ws.write(0, 7, label='环境评分')
    ws.write(0, 8, label='服务评分')
    ws.write(0, 9, label='城市')

    val = 1
    for datas in all_data:

        for data_item in datas['shopBeans']:
            for key, value in data_item.items():
                if (key == 'shopName'):
                    ws.write(val, 0, value)
                elif (key == 'shopId'):
                    ws.write(val, 1, "http://www.dianping.com/shop/" + value)
                elif (key == 'avgPrice'):
                    ws.write(val, 2, value)
                elif (key == 'shopPower'):
                    ws.write(val, 3, value)
                elif (key == 'mainRegionName'):
                    ws.write(val, 4, value)
                elif (key == 'mainCategoryName'):
                    ws.write(val, 5, value)
                elif (key == 'refinedScore1'):
                    ws.write(val, 6, value)
                elif (key == 'refinedScore2'):
                    ws.write(val, 7, value)
                elif (key == 'refinedScore3'):
                    ws.write(val, 8, value)
            print(u'......正在写入%s行' % val)
            val += 1
    flag = 1
    for names in city_name:
        for name in names:
            ws.write(flag, 9, name)
            flag +=1
    print(u'......保存成功!!!')
    wb.save(u'大众点评.xls')

    print('over!!!')
