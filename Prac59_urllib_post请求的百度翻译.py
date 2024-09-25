
import urllib.parse
import urllib.request



url = 'https://fanyi.baidu.com/sug'
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

data = {
  'kw': 'spider'
}

# post 请求的参数，必须要进行编码
# 编码之后必须调用encode方法
new_data = urllib.parse.urlencode(data).encode('utf-8')
#data = bytes(data,encodings="utf-8")

# post的请求的参数 是不会拼接在url的后边的，而是需要放在请求对象定制的参数中
# post请求的参数必须进行编码
request = urllib.request.Request(url=url,data=new_data,headers=header)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

print(type(content))

# 字符串变成json对象

import json

obj = json.loads(content)
print(obj)