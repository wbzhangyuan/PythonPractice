"""
[课程内容]: Python实现12306查票以及自动购票

[授课老师]: 青灯教育-自游  [上课时间]: 20:05

[环境使用]:
    Python 3.8
    Pycharm

    谷歌浏览器
    谷歌驱动

[模块使用]:
    requests   ---> pip install requests  数据请求模块
    prettytable ---> pip install prettytable 打印好看一些
    selenium  ---> pip install selenium==3.141.0  模拟人的行为去操作浏览器
    json ---> 内置模块 不需要安装

课前素材:
    city.json文件  去找木子老师微信领取

---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找木子老师领取录播, 然后再写代码
    3. 不要早退, 课后签到领取福利代码以及课程录播
---------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

        - 失败三: cmd里面显示已经安装过了, 或者安装成功了, 但是在pycharm里面还是无法导入
            解决方法: 可能安装了多个python版本 (anaconda 或者 python 安装一个即可) 卸载一个就好
                    或者你pycharm里面python解释器没有设置好
---------------------------------------------------------------------------------------------------
如何配置pycharm里面的python解释器?
    1. 选择file(文件) >>> setting(设置) >>> Project(项目) >>> python interpreter(python解释器)
    2. 点击齿轮, 选择add
    3. 添加python安装路径
---------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1. 选择file(文件) >>> setting(设置) >>> Plugins(插件)
    2. 点击 Marketplace  输入想要安装的插件名字 比如:翻译插件 输入 translation / 汉化插件 输入 Chinese
    3. 选择相应的插件点击 install(安装) 即可
    4. 安装成功之后 是会弹出 重启pycharm的选项 点击确定, 重启即可生效
---------------------------------------------------------------------------------------------------

本节课内容:
    - 查票
    - 购票
都是爬虫相关知识点可以实现

零基础同学 0
有基础同学 1 ---> 自己写过爬虫程序

听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找木子老师领取录播, 然后再写代码
    3. 不要早退, 课后签到领取福利代码以及课程录播

查票: 先获取车次信息

爬虫基本思路:

一. 数据来源分析
    - 获取车次信息
        通过浏览器抓包分析, 这些车次信息, 在那个url里面
    抓包分析 ---> 开发者工具进行抓包 了解 1 不了解 0  <学python爬虫必备>
        1. 打开开发者工具: F12 或者 鼠标右键点击检查 选择 network
        2. 点击网页查询按钮 --> 会直接返回查询数据结果

只需要请求 https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-11-09&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
就可以得到相关车次信息数据内容

二. 代码实现过程
    1. 发送请求, 模拟浏览器对url地址发送请求
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取我们想要车次信息

    4. 查询功能实现, 根据输入不同城市,以及时间点 获取不同车次

实现购票程序


介绍一个非常优质的课程学习内容

从零基础入门到项目实战, 直接面向就业工作课程内容
    爬虫工程师
    数据分析师
    开发工程师

想要学习python就业工作 ---> 1

我想要找工作, 难道学你这个课程, 按照这个学习路线图去学习就可以了吗?

课程内容知识点, 所教授的内容, 都是符合各大企业招聘需求, 薪资8-15K左右
    爬虫工程师
    数据分析师
    开发工程师

掌握课程内容 80% 左右知识点, 就可以找到相关工作
    - 你真的掌握我们课程内容 80% 左右知识点, 来青灯面试, 我可以给内推进来 8-15K 左右

想要学习python接外包/副业 ---> 2
    - 淘宝 闲鱼
    - 外包群 qq群 微信群
    - 外包平台

如果你是VIP学员, 我们付费学员
    - 就业指导
    - 外包指导
        专属外包接单群
        外包问题解答辅导
        提供相应的外包渠道

跟着老师系统学习
    接外包: 1-3个月
    工作: 3-7个月

加清风老师微信: pythonmiss
    - 可以免费领取学习路线图
    - 可以根据自己情况, 来定制选择你想要学习内容
    - 可以享有双十一优惠

就业 月薪过万,  接外包, 一个月大几千  ---> 前提学会掌握

担心我自己学不会, 掌握不了, 因为是零基础小白

    只要你想要跟着老师学习 <无论是你什么学历, 英语怎么样, 数学怎么样 都不重要, 重要你在学习>
        - 按时听课: 坚持
        - 按时完成作业: 多写多练多敲
        - 认真学习: 不懂多问

    老师可以保证你学会掌握

只要想要学习, 可以直接让你从入门到入土

从报名开始:
    - 学费保障
    - 合同
    - 发票
学习过程中:
    老师远程教安装软件环境
    - 老师监督听课
    - 直播 + 录播资料 + 解答辅导 + 作业考核
    - 免费重修
学完之后:
    - 外包指导
    - 就业指导

加清风老师微信: pythonmiss
    预定 300 学费, 享有双十一优惠名额
    - 课程学费, 直接减免 2000
        原价课程 8880 - 2000 = 6880
    - 额外赠送两门精品课程
        1. 价值1680元自动化办公课程
        2. 价值2680元人工智能课程
    - 参与腾讯课堂抽奖活动
        最高可以获取 iPhone 14
    - 申请12期分期免息学习 0利息0手续费
        月付 ---> 6880 / 12 = 573 学费
    573 相当于 一个月接 1-2 个简单外包  ---> 10分钟左右可以实现外包

    第一期学费 12月7号支付 573 学费
    第二期学费 1月7号支付 573 学费
        已经学了两个月 ---> 接外包
    课程资料你报名之后, 都是有的 --->    签订合约, 月付
    青灯教育和支付宝平台一起弄 --->      签订合约, 月付


1. 学了之后, 接外包 1-3月 ---> 月收 1-3K左右
2. 学了之后, 就业工作 3-7月  薪资8-15K左右

如果你是学习爬虫
    采集数据, 自动化脚本, 抢购, 批量注册登陆脚本....
数据分析:
    可视化数据, 数据处理, Excel数据, 自动化办公脚本
全栈开发:
    网站开发, 后台系统开发, 网站程序, 论坛网站
高级开发
    linux 网络编程 服务器 MySQL 软件界面开发

接简单外包 最起码 核心编程 + 爬虫课程 ---> 可以简单爬虫<保存到表格/自动化脚本>

学的东西越多, 你接外包类目就越多

学的东西越多, 从事岗位也就越多, 薪资相当而言就越高

客户, 不仅仅只是一次发布外包, 做的好, 以后有需求, 他同样会找你

因为我们教学质量和教学服务, 我们很多VIP学员 还会介绍学员来报名

工作中, 你比较努力, 用心, 等你之后跳槽的话, 你部门大佬, 会给你推荐好公司

问题不多, 说明你没学, 没听, 没看, 没写


"""
# 导入数据请求模块
import requests
# 导入 prettytable  as 重命名  prettytable 重命名为 pt
import prettytable as pt
# 导入json模块
import json
# 导入selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 导入账号密码
from password import Password, account
# 导入time模块
import time
"""
模拟人的行为去操作浏览器
    1. 打开浏览器
    2. 输入12306登陆网址
    3. 输入账号密码, 点击登陆
    4. 选择城市以及时间, 点击查询
    5. 选择车次 点击预订
    6. 选择乘车人, 提交订单
    7. 选择座位, 点击购买
"""
# 1. 打开浏览器
driver = webdriver.Chrome()
# 2. 输入12306登陆网址
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
try:
    # 3. 输入账号密码, 点击登陆
    # 输入账号
    driver.find_element_by_css_selector('#J-userName').send_keys(account)
    # 输入密码
    driver.find_element_by_css_selector('#J-password').send_keys(Password)
    # 点击确定
    driver.find_element_by_css_selector('#J-login').click()
    # 3.1 点击弹窗
    driver.implicitly_wait(10)  # 延时等待 为了让网页元素加载
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()
    # 3.2 点击车票预定
    driver.find_element_by_css_selector('#link_for_ticket').click()
    # 4. 选择城市以及时间, 点击查询
    driver.find_element_by_css_selector('#fromStationText').click() # 点击输入框
    driver.find_element_by_css_selector('#fromStationText').clear() # 清空输入框
    driver.find_element_by_css_selector('#fromStationText').send_keys('长沙') # 输入内容
    driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER) # 回车按钮
    # 输入到达的城市
    driver.find_element_by_css_selector('#toStationText').click() # 点击输入框
    driver.find_element_by_css_selector('#toStationText').clear() # 清空输入框
    driver.find_element_by_css_selector('#toStationText').send_keys('上海') # 输入内容
    driver.find_element_by_css_selector('#toStationText').send_keys(Keys.ENTER) # 回车按钮
    # 输入时间
    driver.find_element_by_css_selector('#train_date').click() # 点击输入框
    driver.find_element_by_css_selector('#train_date').clear() # 清空输入框
    driver.find_element_by_css_selector('#train_date').send_keys('2022-11-09') # 输入内容
    # 点击查询按钮
    driver.find_element_by_css_selector('#query_ticket').click()
    # 点击预定
    driver.find_element_by_css_selector('#queryLeftTable tr:nth-child(1) .btn72').click()
    # 选择乘车人
    driver.find_element_by_css_selector('#normalPassenger_1').click()
    # 点击提交提单
    driver.find_element_by_css_selector('#submitOrder_id').click()
    # 选择座位
    # driver.find_element_by_css_selector('#erdeng1 > ul:nth-child(4) > li:nth-child(2)').click()
    # 点击提交
    time.sleep(3)
    driver.find_element_by_css_selector('#qr_submit_id').click()
    driver.find_element_by_css_selector('#qr_submit_id').click()

except:
    pass


# """
# 1. 发送请求, 模拟浏览器对url地址发送请求
#
# 实现查询功能:
#     输入出发城市
#     输入到达城市
#     输入出发时间
#
# 城市名字: 字母
# """
# # 读取文件 城市字母文件
# f = open('city.json', encoding='utf-8')
# # f.read() 返回字符串数据类型 把字符串转成json字典数据 --> 根据键值对取值
# json_data = json.loads(f.read())
# # 输入内容
# from_city = input('请输入你要出发城市: ')
# to_city = input('请输入你要到达城市: ')
# date = '2022-11-09'
# # 确定请求链接
url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_city]}&leftTicketDTO.to_station={json_data[to_city]}&purpose_codes=ADULT'
# # 模拟伪装 ---> headers 请求头
# headers = {
#     # Cookie 用户信息, 表示常用于检测是否有登陆账号
#     'Cookie': '_uab_collina=165650330916153394558455; JSESSIONID=34AFEC7D7370756179A2976A79434D6A; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u957F%u6C99%2CCSQ; BIGipServerotn=1911030026.24610.0000; BIGipServerpassport=770179338.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1668129535127; RAIL_DEVICEID=TbHG0I9N4zNOVXocTOo6JdSREGznbbsYb5f_xQPshKLa1Y8Qx7LbGMu_h4Zwb6MyBOk_1zvlhZn85dlBcC4F1SEL1hwpTWuAkNkA7dSIqQ-dgdZAcoL1jMCS4bWfKSgKEstpGs8BAzfO-ItsTfKkP6YQL9Y24vGA; fo=uyys4j4q4rs7diywCDbOKBwdzYaDJcHjbyEG0hwDDZbF9Swz2dB79o6CCDC_EOHwJ7XidDtuZKQKjz6vYdfE3PDpSX9YvVulaMDDQmKGRPhrjzRZHlNGKC2S6egp70_4PJGqyv770aRXnJgffGRwkABzbJZDDiUtaTyHzatcoZpt_YO-T-dfbdjNQrQ; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2022-11-09; _jc_save_toDate=2022-11-07',
#     # User-Agent 用户代理 表示浏览器基本身份信息
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
# }
# # 发送请求
# response = requests.get(url=url, headers=headers)
# # <Response [200]> 表示请求成功了
# print(response)
# """
# 2. 获取数据, 获取服务器返回响应数据
#     为什么获取response.json() 数据的时候报错?
#     - simplejson.errors.JSONDecodeError: Expecting value: line 1 column 4 (char 3)
#         一定获取的数据, 不是完整json数据格式
#     解决方法:
#         1. 获取response.text 看数据返回情况
#             - 发现自己获取的数据, 和开发者工具里面所看到不一样 <因为你被反爬了 [要么得不到数据, 要么得到数据不是想要的]>
#         2. 因为没有伪装, 加headers 伪装一下
#
# 3. 解析数据, 提取我们想要车次信息
#     response.json() 获取响应json字典数据  完整的花括号
#     response.text 获取响应文本数据 字符串数据
#
# 根据基础语法知识点: 字典取值 --> 键值对取值, 根据冒号左边的内容[键], 提取冒号有右边的内容[值]
# """
# # 实例化一个对象
# tb = pt.PrettyTable()
# # 输出添加字段名
# tb.field_names = [
#     '序号',
#     '车次',
#     '出发时间',
#     '到达时间',
#     '耗时',
#     '特等座',
#     '一等',
#     '二等',
#     '软卧',
#     '硬卧',
#     '硬座',
#     '无座',
# ]
# # 添加序号 每次循环+1
# page = 0
# # for循环遍历, 把列表里面元素 一个一个提出来
# for i in response.json()['data']['result']:
#     # 先用 split 分割, 再用列表取值: 根据索引位置
#     index = i.split('|')
#     num = index[3]  # 车次
#     start_time = index[8]  # 出发时间
#     end_time = index[9]  # 到达时间
#     use_time = index[10]  # 耗时
#     topGrade = index[32]  # 特等座
#     first_class = index[31]  # 一等
#     second_class = index[30]  # 二等
#     hard_sleeper = index[28]  # 硬卧
#     hard_seat = index[29]  # 硬座
#     no_seat = index[26]  # 无座
#     soft_sleeper = index[23]  # 软卧
#     dit = {
#         '序号': page,
#         '车次': num,
#         '出发时间': start_time,
#         '到达时间': end_time,
#         '耗时': use_time,
#         '特等座': topGrade,
#         '一等': first_class,
#         '二等': second_class,
#         '软卧': soft_sleeper,
#         '硬卧': hard_sleeper,
#         '硬座': hard_seat,
#         '无座': no_seat,
#     }
#     # print(dit)
#     # 添加每行输出内容
#     tb.add_row([page, num, start_time, end_time,
#                 use_time,
#                 topGrade,
#                 first_class,
#                 second_class,
#                 soft_sleeper,
#                 hard_sleeper,
#                 hard_seat,
#                 no_seat,
#                 ])
#     page += 1 # 每次循环+1
#
# print(tb)
