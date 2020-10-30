import http
import urllib.request
import re
import os
import urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url = "https://www.google.com/search?q=%E7%A1%85%E8%83%B6O%E5%9E%8B%E5%9C%88&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizvaTVi9TsAhWQF6YKHdPDAQEQ_AUoAXoECAsQAw&biw=1858&bih=1097"
searchName = ""
path = 'd:\\lianxi\\mypic\\test'  # 设置图片的保存地址
# payload = "paged=5"
payload = {'type': 'index', 'paged': 1}
formdata = {
    "type": "AUTO",
    "i": "i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}


def get_html(searchName):
    url2 = "https://www.google.com/search?q=" + searchName + "&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj_ldfjqtfsAhXRZt4KHa_8DD0Q_AUoAXoECAwQAw&biw=857&bih=1087"
    # req = urllib.request.Request(url=url2, headers=headers)
    # req = urllib.request.Request(url=url, headers=headers)
    req = urllib.request.Request(url=url, data=formdata, headers=headers)
    page = urllib.request.urlopen(req).read()
    return page.decode('utf-8')


def get_img(html):
    reg = r'https://[^\s]*?\.jpg'
    imgre = re.compile(reg)  # 转换成一个正则对象
    imglist = imgre.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    x = 0  # 声明一个变量赋值
    if not os.path.isdir(path):
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'  # 保存在test路径下
    for imgurl in imglist:
        # if(urllib.request.Request(imgurl))
        try:
            urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))  # 打开imgList,下载图片到本地
        except:
            print(imgurl, "异常")

        x = x + 1
        print('图片开始下载，注意查看文件夹')
    return imglist


def photosInit(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.getsize(path + "\\" + name) < 100:
                # if name.endswith(".jpg"):  # 填写规则
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))


html_b = get_html("silicone loop")  # 获取该网页的详细信息
print(get_img(html_b))  # 从网页源代码中分析下载保存图片
photosInit(path)
