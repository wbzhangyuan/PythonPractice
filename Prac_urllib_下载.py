

import urllib.request

url_page = 'http://www.baidu.com'
# url:下载路径
# filename：文件的名字
# 在python中可以写变量的名字也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
# url_img='https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1phG8u.img?w=768&h=432&m=6&x=1202&y=338&s=574&d=574'
# urllib.request.urlretrieve(url=url_img,filename='lisa.jpg')

# 下载视频
url_video = 'https://vdept3.bdstatic.com/mda-qhgjqsi32m8iggn9/cae_h264/1723990214123700831/mda-qhgjqsi32m8iggn9.mp4?v_from_s=hkapp-haokan-hnb&auth_key=1724498223-0-0-4717e72b4160b0e1397fa36030bfb0c4&bcevod_channel=searchbox_feed&cr=0&cd=0&pd=1&pt=3&logid=1022861262&vid=7169681455938006766&klogid=1022861262&abtest=87345_1'

urllib.request.urlretrieve(url=url_video,filename='hxekyyds.mp4')






