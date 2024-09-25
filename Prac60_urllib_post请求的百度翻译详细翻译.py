
import urllib.parse
import urllib.request



url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
header = {
'    Accept':' */*',
'Accept-Encoding':' gzip, deflate, br, zstd',
'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6 ',
'Acs-Token': '1725703211947_1725761651411_eUE/17idZ5HRvZHtjwpAwVtvc4pPomkVZ4HIwdV4LM2uBrfDsmWDdZc07W5JGyF3fAGQC6Xs7Xd990m3lNwKM6cK4JC2KCM38Clp5'
+'8XthPJNHonYEEPIITbWPHDw6FBqSnUFvGLpxGEyU1lfrxt6/0NPYjXnxgusSzsiuyFIca/SGbLbCstL'
+'FGRSL3iuxca1i7yu/EBRO2dbUTFwjxjyfCOmmBchxm+JWzCfelLSHCPQjy0DUMw81FdEjSeNLZ6/zAMcbPI'
+'FsNvrCQRobTuCN6+rNse4oL560oIVCg4pc2ozD0Uqv3lljRg2nLzNux9zSgCkVOimZJT2emRsKIxMeWgu'
+'JN0JFlJeWjaywdYeLO6YS83DYBcybJBYM1DawUbrkHACk+KRrdu0oWj56RvuFBtkupWqOYIPVAotA+8SjqWp40bCH'
+'VQtuCjik3ALysyjqC8SIxC8dG3bj37X/Uz0swG0Prt7GoIE7MuNqXJrdjWSGy8OU5TDPha4JUSI0wth',
'Connection':' keep-alive',
'Content-Length': '150',
'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
Cookie: BAIDU_WISE_UID=wapp_1716625439308_440; __bid_n=18fc8d54aad0576e3e55c9; BDUSS=JLWUg5b3RHM3VYTFhvZmxyTkU1cFhuZHJjYzFGVWhzVnVxQU9Qc1lIaUFLcWRtSVFBQUFBJCQAAAAAAAAAAAEAAABGt1sgd2J6aGFuZ3l1YW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICdf2aAnX9mbG; BDUSS_BFESS=JLWUg5b3RHM3VYTFhvZmxyTkU1cFhuZHJjYzFGVWhzVnVxQU9Qc1lIaUFLcWRtSVFBQUFBJCQAAAAAAAAAAAEAAABGt1sgd2J6aGFuZ3l1YW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICdf2aAnX9mbG; BAIDUID=8E86DAF3BE483650EEB3A95F063D1B2B:FG=1; BAIDUID_BFESS=8E86DAF3BE483650EEB3A95F063D1B2B:FG=1; ZFY=jxA9DYQpcqxyB:B3EZnxky5aru7S:Alz4GMoADP8fGJq4:C; BIDUPSID=8E86DAF3BE483650EEB3A95F063D1B2B; PSTM=1723506846; H_PS_PSSID=60271_60623_60629_60665_60678_60672; ZD_ENTRY=bing; H_WISE_SIDS_BFESS=60271_60629_60665_60678_60672_60681_60692_60573_60724; MCITY=-330%3A; smallFlowVersion=old; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; RT="z=1&dm=baidu.com&si=5acc6975-b659-4a6d-875d-08c32e30b65a&ss=m0pafxm7&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=gjr7&ul=oyhh3&hd=oyhhw"; H_WISE_SIDS=60271_60629_60678_60681_60692_60573_60724
'Host':' fanyi.baidu.com'
Origin: https://fanyi.baidu.com
'Referer: https':'//fanyi.baidu.com/'
Sec-Fetch-Dest: empty
'Sec-Fetch-Mode':' cors'
Sec-Fetch-Site: same-origin
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
X-Requested-With: XMLHttpRequest
'sec-ch-ua':' "Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"'
sec-ch-ua-mobile: ?0
'sec-ch-ua-platform':' "Windows"'


}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'lo',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '646722.867699',
    'token': 'c56cdfca2661393ea340fa2d564cff28',
    'domain': 'common',
    'ts': '1725542326722'
}

# post 请求的参数，必须要进行编码
# 编码之后必须调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
#data = bytes(data,encodings="utf-8")

# post的请求的参数 是不会拼接在url的后边的，而是需要放在请求对象定制的参数中
# post请求的参数必须进行编码
request = urllib.request.Request(url=url,data=data,headers=header)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

# print(type(content))

# 字符串变成json对象
#
import json

obj = json.loads(content)
print(obj)