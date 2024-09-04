import urllib.request
import urllib.response
import urllib.parse

url = 'https://www.baidu.com/s?'
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

data = {
    'wd':'周杰伦',
    'sex':'男',
}

new_data = urllib.parse.urlencode(data)

request = urllib.request.Request(url=url+new_data, headers=header)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)