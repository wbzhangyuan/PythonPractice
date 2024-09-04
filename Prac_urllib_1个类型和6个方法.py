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

# 按照一个字节一个字节的去读
# content = response.read().decode('utf-8')  # 返回字节形式的二进制数据
content = response.read(5).decode('utf-8')  # 返回字节形式的二进制数据
# response是HTTPResponse的类型
# print(type(response))
# print(content)
content = response.readline() # 读取一行
# print(content)
content = response.readlines() # 读取多行
# print(content)
print(response.getcode())# 返回状态码，如果是200就说明没错

print(response.geturl()) # 返回url地址

print(response.getheaders()) # 返回状态信息




