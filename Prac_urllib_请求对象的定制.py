import urllib.request

'''
爬虫三步思路
1.访问网站
2.获取资源
3.解析数据
'''

# 使用urllib获取百度源码
'''
url的组成  https://www.baidu.com/s?wd=周杰伦
http/https    www.baidu.com   80/443    s     wd=周杰伦   #
    协议           主机          端口号   路径   参数       锚点

http:80
https:443
mysql 3306
oracle 1521
redis 6379
mongodb 27017
'''

url = 'https://www.baidu.com'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
# 因为urlopen方法中不能存储字段，所以headers不能传递进去
# 请求对象定制,因为参数顺序不同，所以必须要指定关键字才能传
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
# response = urllib.request.urlopen(url,headers)


content = response.read().decode('utf-8')  # 返回字节形式的二进制数据

print(content)






