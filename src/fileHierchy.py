#create catalog tree of url

from tkinter import *
import os
import requests
from bs4 import BeautifulSoup
import re
import os
import random
import time

class urlHierchy:
    def __init__(self, url, name, fa=None):
        print(url)
        self.user_agent = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
        ]
        self.url = url
        self.name = name
        self.created = False
        self.sons = []
        if fa == None:
            self.dir = [name]
        else:
            self.dir = fa.dir+[name]

    def mkdir(self, path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    def getWebpage(self):
        print("get "+self.url)
        sleep_download_time = 1
        while True:
            try:
                time.sleep(sleep_download_time)
                self.webpage = requests.get(self.url, headers={
                    'User-Agent': random.choice(self.user_agent)})
                print("get webpage success")
                self.webpage.close()
                break
            except:
                print("retry", self.url)
            sleep_download_time += 5

    def countFileNum(self):
        if self.__class__.__name__ == 'file':
            return 1
        else:
            ans=0
            for i in self.sons:
                ans+=i.countFileNum()
            return ans

    def downloadAllSelected(self, inter):
        print("download process enter %s as %s" %
              (self.name, self.__class__.__name__))
        if self.__class__.__name__ == 'file':
            print(self.name)
            self.download(inter)
        else:
            for i in self.sons:
                i.downloadAllSelected(inter)


class file(urlHierchy):
    def download(self, inter):  # 下载该文件
        inter.updateDownloadStatus(self.name)
        dir = inter.rootDirection+'/'+'/'.join(self.dir[1:])
        self.mkdir(inter.rootDirection+'/'+'/'.join(self.dir[1:-1]))
        if os.path.exists(dir):
            print("file exists")
            return
        pdf = open(dir, 'wb')
        print("downloading %s into %s" % (self.name, dir))
        self.getWebpage()
        pdf.write(self.webpage.content)
        pdf.close()


class folder(urlHierchy):

    def __delete__(self):
        for i in self.sons:
            del i

    def findList(self):  # 生成可能的儿子节点列表
        if self.created == True:
            return
        self.created = True
        self.getWebpage()
        self.list = []
        try:
            listRaw = BeautifulSoup(self.webpage.text, 'html5lib')
            listRaw = listRaw.find(
                attrs={"class": "paperslist"})
            print("identify raw list success")
            listRaw = listRaw.find_all('a')
            print("identify list success")
            for content in listRaw:
                self.list.append(content.attrs['href'])
            return self.list
        except:
            print("error when finding list after %s" % self.name)
            return self.list

    def createSon(self, name):  # 生成儿子节点
        if name[-3:] == 'pdf':
            son = file(self.url+'/'+name, name, fa=self)
        else:
            son = folder(self.url+'/'+name, name, fa=self)
        self.sons.append(son)
        return son

    def findByCriteria(self, criteria):  # 正则表达式匹配
        createdSons = []
        for son in self.sons:
            if re.search(criteria, son.name, flags=re.I) != None:
                createdSons.append(son.name)
        ans = []
        print("finding contents in %s by %s" % (self.name, criteria))
        for name in self.list:
            #print(criteria,name)
            if re.search(criteria, name, flags=re.I) != None and name not in createdSons:
                print(re.search(criteria, name, flags=re.I))
                print('matches')
                ans.append(self.createSon(name).name)
            elif name in createdSons:
                ans.append(name)

        return ans
