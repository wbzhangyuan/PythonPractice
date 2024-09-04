import urllib.request

'''
爬虫三步思路
1.访问网站
2.获取资源
3.解析数据
'''

# 使用urllib获取百度源码

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')  # 返回字节形式的二进制数据

print(content)





