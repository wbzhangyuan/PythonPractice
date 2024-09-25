import json
# 爬取12306网站车票

import urllib.request
import requests
import urllib.response
import urllib.parse
# from prettytable import PrettyTable # 表格样式美化工具
import prettytable as pt

# url = 'https://kyfw.12306.cn/otn/leftTicket/query?'
# header = {
# 'accept':'*/*',
# 'accept-encoding':'gzip, deflate, br, zstd',
# 'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# 'cache-control':'no-cache',
# 'connection':'keep-alive',
# 'cookie':'_uab_collina=172543787795317440904626; JSESSIONID=E0F55A77D8B6BBA950FC123B555A8120; BIGipServerpool_passport=216269322.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u9042%u5B81%2CNIW; _jc_save_toStation=%u6210%u90FD%u4E1C%2CICW; _jc_save_wfdc_flag=dc; _jc_save_toDate=2024-09-10; BIGipServerpassport=803733770.50215.0000; _jc_save_fromDate=2024-09-10; BIGipServerotn=334496266.64545.0000',
# 'host':'kyfw.12306.cn',
# 'if-modified-since':'0',
# 'referer':'https://kyfw.12306.cn/otn/leftTicket/init',
# 'sec-ch-ua':'"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-ch-ua-platform':'"Windows"',
# 'sec-fetch-dest':'empty',
# 'sec-fetch-mode':'cors',
# 'sec-fetch-site':'same-origin',
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
# 'x-requested-with':'XMLHttpRequest',
# }

# data = {
#     'leftTicketDTO.train_date':'2024-09-10',
#     'leftTicketDTO.from_station':'NIW',
#     'leftTicketDTO.to_station':'ICW',
#     'purpose_codes':'ADULT'
# }

# new_data = urllib.parse.urlencode(data)
# request = urllib.request.Request(url=url+new_data, headers=header)
# response = urllib.request.urlopen(request)

f = open('city.json',encoding='utf-8');
json_city = json.loads(f.read())
# print(data_city)

from_city = input('请输入你想出发的城市\n')
to_city = input('请输入你想到达的城市\n')
query_date = input('请输入要查询的时间：格式(2022-11-09)')


url = f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={query_date}&leftTicketDTO.from_station={json_city[from_city]}&leftTicketDTO.to_station={json_city[to_city]}&purpose_codes=ADULT'
header = {
    # 用户信息，常用于检测是否登录账号（登录与否都有cookies）
    'cookie':'_uab_collina=172543787795317440904626; JSESSIONID=38A18500DAEED8810E856D2D83DE8AA8; guidesStatus=off; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u6210%u90FD%u4E1C%2CICW; BIGipServerotn=1961361674.24610.0000; BIGipServerpassport=837288202.50215.0000; highContrastMode=defaltMode; cursorStatus=off; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toStation=%u9042%u5B81%2CNIW; _jc_save_fromDate=2024-09-26; _jc_save_toDate=2024-09-26'
    # User-Agent 用户代理，表示浏览器/设备 基本身份信息
    ,'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

response = requests.get(url=url, headers=header)
# print(response)
json_data = response.json()
# print(json_data)

# text = response.text
# print(type(text))

# 提取js字段的值
result = json_data['data']['result']

# print(result)

# 实例化对象
tb = pt.PrettyTable()
# 设置字段名
tb.field_names = [
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等',
    '二等',
    '软卧',
    '硬卧',
    '硬座',
    '无座'
]
# 定义序号
page = 0
# print(json_data)
for i in result:
    index = i.split('|') # 字符串分隔会返回一个列表
    # 通过列表索引位置取值
    num = index[3] # 车次
    start_time = index[8] # 出发时间
    end_time = index[9]  # 达到时间
    use_time = index[10] # 耗时
    topGrade = index[32] # 特等座
    first_class = index[31]  # 一等
    second_class = index[30]  # 二等
    hard_sleeper = index[28]  # 硬卧
    hard_seat = index[29]  # 硬座
    no_seat = index[26]  # 无座
    soft_sleeper = index[23]  # 软卧
    dit = {
        '序号':'page',
        '车次':'num',
        '出发时间':'start_time',
        '到达时间':'end_time',
        '耗时':'use_time',
        '特等座':'topGrade',
        '一等':'first_class',
        '二等':'second_class',
        '软卧':'soft_sleeper',
        '硬卧':'hard_sleeper',
        '硬座':'hard_seat',
        '无座':'no_seat'
    }
    # print(dit)
    # 添加数据内容
    tb.add_row([
        page,
        num ,
        start_time ,
        end_time ,
        use_time ,
        topGrade ,
        first_class ,
        second_class ,
        soft_sleeper,
        hard_sleeper ,
        hard_seat ,
        no_seat ,
    ])
    page += 1

print(tb)


#
#
#     便携查询值所在的索引
#     page = 0
    # for j in index:
    #     print(j,page,sep='索引是：')
    #     page+=1
    # print(page)
# print(text)
# content = response.read().decode('utf-8')




'''搜索车票信息'''


'''自动预定车票'''












