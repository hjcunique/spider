#--coding:utf-8--
'''
Created on 2017年7月19日

@author: hanjiachao
'''
from urllib import request
import re

def getHTML(url,header):
    req=request.Request(url=url,headers=header)
    html=request.urlopen(req).read()
    html=html.decode('UTF-8')
    return html
def getImage(html):
    key_re=re.compile(r'"hbimg", "key":"(.*?)",')
    key_list=re.findall(key_re,html)
    #http://img.hb.aicdn.com/5dadf9def76f61619cd090a1d0919df4ed97700bd545e-Hddyjc_fw658
    X=0
    for image_key in key_list:
        image_url="http://img.hb.aicdn.com/"+image_key+"_fw658"
        try:
            request.urlretrieve(image_url,'D:\\software\\eclipse\\workspace\\spider\\huaban\\'+'%s.jpg' %X)
        except:
            print("下载图片：%s失败，跳过，获取下一张。" %image_url)
            continue
        print("下载图片%s成功，下载下一张" %image_url)
        X += 1
    print("图片保存成功！")       
    
        

if __name__ == '__main__':  
    url='http://huaban.com/favorite/beauty/'
    user_agent='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
    header={'User-Agent':user_agent}
    html=getHTML(url,header)
    #print(html)
    getImage(html)