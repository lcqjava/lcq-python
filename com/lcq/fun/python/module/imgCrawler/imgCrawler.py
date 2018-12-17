#/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import urllib

from bs4 import  BeautifulSoup

"""
下载图片
"""
def downloadImg(imgUrl,downloadPath,imgName):
    urllib.request.urlretrieve(imgUrl,downloadPath+imgName)


"""
获取网页的图片地址
"""
def getImgFromWebpage(webpageUrl):

    html = requests.get(webpageUrl).text

    soup = BeautifulSoup(html,"html.parser")
    all_img = (soup.find_all('img'))
    return  all_img


# 本地存储路径
path = "/Users/chaoqunluo/Documents/javaDev/python-workspace/lcq-python/images/"
# 网页地址
webpageUrl = "http://www.win4000.com/meinv166930.html"
# 获取网页中的所有图片
allImg = getImgFromWebpage(webpageUrl)

i = 0
for img in allImg:
   if(img['data-original'] != ''):
     downloadImg(img['data-original'],path,str(i)+".jpg")
     i+=1

