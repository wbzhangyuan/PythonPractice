
import urllib.parse
import urllib.request



url = 'https://fanyi.baidu.com/sug'
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

data = {
  'kw': 'spilder'
}


new_data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url,data=data,headers=header)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)