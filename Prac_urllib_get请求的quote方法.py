import urllib.request
import urllib.response

url = 'https://www.baidu.com/s?wd='
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 将周杰伦三个字变成unicode编码的格式
name = urllib.parse.quote('周杰伦');

request = urllib.request.Request(url=url+name, headers=header)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)