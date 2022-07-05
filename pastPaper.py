from tkinter import *
import os
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import re
import os
import random
import time
import socket
import threading
from sys import exit
from tkinter.filedialog import askdirectory
sleep_download_time = 10
timeout = 20
socket.setdefaulttimeout(timeout)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
user_agent = [
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
rootDirection = os.getcwd()+r"\pastpapers"
mainurl = "https://papers.gceguide.com"


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


class urlHierchy:
    def __init__(self, url, name, fa=None):
        print(url)
        self.url = url
        self.name = name
        self.created = False
        self.sons = []
        if fa == None:
            self.dir = [name]
        else:
            self.dir = fa.dir+[name]

    def getWebpage(self):
        print("get "+self.url)
        sleep_download_time=1
        while True:
            try:
                time.sleep(sleep_download_time)
                self.webpage = requests.get(self.url, headers={
                    'User-Agent': random.choice(user_agent)})
                print("get webpage success")
                self.webpage.close()
                break
            except:
                print("retry",self.url)
            sleep_download_time+=5

    def downloadAllSelected(self,inter):
        print("download process enter %s as %s"%(self.name,self.__class__.__name__))
        if self.__class__.__name__ == 'file':
            print(self.name)
            self.download(inter)
        else:
            for i in self.sons:
                i.downloadAllSelected(inter)


class file(urlHierchy):
    def download(self,inter):  # 下载该文件
        dir = rootDirection+'/'+'/'.join(self.dir[1:])
        mkdir(rootDirection+'/'+'/'.join(self.dir[1:-1]))
        if os.path.exists(dir):
            print("file exists")
            return
        pdf = open(dir, 'wb')
        #inter.updateDownloadStatus("Downloading %s into %s" % (self.name, dir))
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
            if re.search(criteria, son.name, flags=re.I)!=None:
                createdSons.append(son.name)
        ans = []
        print("finding contents in %s by %s" % (self.name, criteria))
        for name in self.list:
            #print(criteria,name)
            if re.search(criteria, name, flags=re.I)!=None and name not in createdSons:
                print(re.search(criteria, name, flags=re.I))
                print('matches')
                ans.append(self.createSon(name).name)
            elif name in createdSons:
                ans.append(name)

        return ans


class app():
    def __init__(self, interface):
        self.root = folder(mainurl, "/")
        self.root.findList()
        self.inter = interface
        self.root.findByCriteria(".*")
        self.downloadList = {}
        self.downloadingFlag=False

    # returns a list of subject names fitting qualification and subject filter
    def applySubjectFilter(self, qualification, subjecuCriteria):
        ans = []
        for q in self.root.sons:
            print(q.name)
            if q.name in qualification:
                q.findList()
                ans.extend(q.findByCriteria(subjecuCriteria))
        return ans

    # subject:科目全名字符串，year:(int(start)，int(end)，Specimen(bool))，season:(bool(m),bool(s),bool(w))
    def alterDownloadList(self, subject, year, season, category, paper):
        # category:(bool(ms),bool(qp),bool(in),bool(gt),bool(er))，paper:"123"字符串
        print(subject, year, season, category, paper)
        self.downloadList[subject] = (year, season, category, paper)

    def delDownloadList(self, subject):
        if subject in self.downloadList.keys():
            del self.downloadList[subject]

    def download(self):#Start download process
        self.downloadingFlag=True
        for detail in self.downloadList.items():
            subject = detail[0]
            year = detail[1][0]
            season = detail[1][1]
            category = detail[1][2]
            paper = detail[1][3]#extract details
            for q in self.root.sons:
                for s in q.sons:
                    if s.name == subject:
                        yearCriteria = ''
                        for y in range(year[0], year[1]+1):
                            yearCriteria += str(y)+'|'
                        if year[2]:
                            yearCriteria += 'Specimen|'
                        yearCriteria=yearCriteria[:-1]
                        paperCriteria = '_['
                        if season[0]:
                            paperCriteria += 'm'
                        if season[1]:
                            paperCriteria += 's'
                        if season[2]:
                            paperCriteria += 'w'
                        if category[0]or category[1] or category[2]:
                            paperCriteria += r']\d\d_(('
                            if category[0]:
                                paperCriteria += 'ms|'
                            if category[1]:
                                paperCriteria += 'qp|'
                            if category[2]:
                                paperCriteria += 'in|'
                            paperCriteria=paperCriteria[:-1]
                            paperCriteria += ')_['+paper+'][123]?|'
                        else:
                            paperCriteria+=r']\d\d_('
                        if category[3]:
                            paperCriteria += 'gt|'
                        if category[4]:
                            paperCriteria += 'er|'
                        paperCriteria=paperCriteria[:-1]
                        paperCriteria += ')'
                        s.findList()
                        print(yearCriteria)
                        s.findByCriteria(yearCriteria)
                        for year in s.sons:
                            year.findList()
                            year.findByCriteria(paperCriteria)
                        print("find %s end"%subject)
        print("start download")
        self.root.downloadAllSelected(self.inter)
        self.inter.downloadSuccess()

    def run(self):
        while True:
            applySubFil, qual, sub, alt, dele, subject, year, season, category, paper, download, quit = self.inter.getInfo()
            if not self.downloadingFlag:
                if applySubFil:
                    sublist = self.applySubjectFilter(qual, sub)
                    self.inter.updateSubjectList(sublist)
                elif alt:
                    self.alterDownloadList(subject, year, season, category, paper)
                    self.inter.alterSuccess(self.downloadList)
                elif dele:
                    self.delDownloadList(subject)
                    self.inter.deleteSuccess(self.downloadList)
                elif download:
                    self.inter.downloadStart()
                    download=threading.Thread(target=self.download)
                    download.setDaemon(True)
                    download.start()
            if quit:
                    self.inter.destroyEnd()
                    exit(0)


class gui():
    def __init__(self):
        self.root = Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)
        self.root.title("Past Paper Downloader")
        self.root.geometry('600x400')
        self.root.grid_propagate(0)
        self.root.resizable(False,False)
        self.subFilFlag = False
        self.altFlag = False
        self.delFlag = False
        self.downloadFlag = False
        self.qFlag = False
        self.qual = []
        self.subjectSearched = StringVar()
        self.syear = StringVar()
        self.Syear = 0
        self.eyear = StringVar()
        self.Eyear = 0
        self.paper = StringVar()
        self.subSelected = StringVar()
        self.alFlag = IntVar()
        self.olFlag = IntVar()
        self.igFlag = IntVar()
        self.mFlag = IntVar()
        self.sFlag = IntVar()
        self.wFlag = IntVar()
        self.msFlag = IntVar()
        self.qpFlag = IntVar()
        self.inFlag = IntVar()
        self.erFlag = IntVar()
        self.gtFlag = IntVar()

        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=3)
        self.root.rowconfigure(0, weight=1)
        self.subjectFrame = Frame(self.root, bg='red',height=296,width=396)
        self.subjectFrame.grid_propagate(0)
        self.subjectFrame.grid(row=0, column=0, sticky=NS,
                               padx=2, pady=2)
        self.detailFrame = Frame(self.root, bg='green',height=296,width=196)
        self.detailFrame.grid_propagate(0)
        self.detailFrame.grid(row=0, column=1, sticky=N,
                              padx=2, pady=2)
        self.downloadFrame = Frame(self.root, bg='blue',height=96,width=596)
        self.downloadFrame.grid_propagate(0)
        self.downloadFrame.grid(
            row=1, column=0, columnspan=2, sticky=NSEW, padx=2, pady=2)

        self.subjectFrame.rowconfigure(0, weight=1)
        self.subjectFrame.rowconfigure(1, weight=1)
        self.subjectFrame.rowconfigure(2, weight=10)
        self.qualiFrame = Frame(self.subjectFrame,height=25,width=392)
        self.qualiFrame.grid_propagate(0)
        self.qualiFrame.grid(row=0, column=0, sticky=W,
                             padx=2, pady=2)
        Checkbutton(self.qualiFrame, text="A/AS Level",
                    variable=self.alFlag).grid(row=0, column=0)
        Checkbutton(self.qualiFrame, text="O Level",
                    variable=self.olFlag).grid(row=0, column=1)
        Checkbutton(self.qualiFrame, text="IGCSE",
                    variable=self.igFlag).grid(row=0, column=2)

        self.subEntryFrame = Frame(self.subjectFrame,height=34,width=392)
        self.subEntryFrame.grid_propagate(0)
        self.subEntryFrame.grid(
            row=1, column=0, sticky=EW, padx=2, pady=0)
        Entry(self.subEntryFrame, textvariable=self.subjectSearched,
              width=49).grid(row=0, column=0, sticky=W,padx=0,pady=0)
        Button(self.subEntryFrame, text='Search',
               command=self.search).grid(row=0, column=1, sticky=NS,padx=0,pady=0)

        self.subListFrame = Frame(self.subjectFrame,height=235,width=392)
        self.subListFrame.grid_propagate(0)
        self.subListFrame.pack_propagate(0)
        self.subListFrame.grid(row=2, column=0,padx=2,pady=2)

        self.yearFrame = Frame(self.detailFrame,height=50,width=192)
        self.yearFrame.grid_propagate(0)
        self.yearFrame.grid(row=0, column=0,padx=2,pady=2)
        Label(self.yearFrame, text="Year").grid(row=0, column=0, columnspan=3,sticky=W)
        Entry(self.yearFrame, textvariable=self.syear,
              width=10).grid(row=1, column=0,sticky=W)
        Label(self.yearFrame, text='-').grid(row=1, column=1,sticky=W)
        Entry(self.yearFrame, textvariable=self.eyear,
              width=10).grid(row=1, column=2,sticky=W)

        self.seasonFrame = Frame(self.detailFrame,height=25,width=192)
        self.seasonFrame.grid_propagate(0)
        self.seasonFrame.grid(row=1, column=0,padx=2,pady=0)
        Checkbutton(self.seasonFrame, text="m",
                    variable=self.mFlag).grid(row=0, column=0,sticky=W)
        Checkbutton(self.seasonFrame, text="s",
                    variable=self.sFlag).grid(row=0, column=1,sticky=W)
        Checkbutton(self.seasonFrame, text="w",
                    variable=self.wFlag).grid(row=0, column=2,sticky=W)

        self.typeFrame = Frame(self.detailFrame,height=50,width=192)
        self.typeFrame.grid_propagate(0)
        self.typeFrame.grid(row=2, column=0,padx=2,pady=2)
        Checkbutton(self.typeFrame, text="ms",
                    variable=self.msFlag).grid(row=0, column=0)
        Checkbutton(self.typeFrame, text="qp",
                    variable=self.qpFlag).grid(row=0, column=1)
        Checkbutton(self.typeFrame, text="in",
                    variable=self.inFlag).grid(row=0, column=2)
        Checkbutton(self.typeFrame, text="gt",
                    variable=self.gtFlag).grid(row=1, column=0)
        Checkbutton(self.typeFrame, text="er",
                    variable=self.erFlag).grid(row=1, column=1)

        self.paperFrame = Frame(self.detailFrame,height=50,width=192)
        self.paperFrame.grid_propagate(0)
        self.paperFrame.grid(row=3, column=0,padx=2,pady=0)
        Label(self.paperFrame, text="Paper").grid(row=0, column=0,sticky=W)
        Entry(self.paperFrame, textvariable=self.paper).grid(row=1, column=0,sticky=W)

        self.detailButtonFrame = Frame(self.detailFrame,height=44,width=192)
        self.detailButtonFrame.grid_propagate(0)
        self.detailButtonFrame.grid(row=4, column=0,padx=2,pady=2)
        self.altButtonFrame=Frame(self.detailButtonFrame,height=40,width=92,bg='blue')
        self.altButtonFrame.grid_propagate(0)
        self.altButtonFrame.pack_propagate(0)
        self.altButtonFrame.grid(row=0,column=0,sticky=W,padx=2,pady=2)
        self.deleButtonFrame=Frame(self.detailButtonFrame,height=40,width=92,bg='blue')
        self.deleButtonFrame.grid_propagate(0)
        self.deleButtonFrame.pack_propagate(0)
        self.deleButtonFrame.grid(row=0,column=1,sticky=E,padx=2,pady=2)
        self.altButton = Button(self.altButtonFrame,
                                text='apply',command=self.alt)
        self.altButton.pack(fill="both", expand=1)
        self.deleButton = Button(
            self.deleButtonFrame, text='delete',command=self.delete)
        self.deleButton.pack(fill="both", expand=1)

        self.downloadButtonFrame=Frame(self.detailFrame,height=60,width=192)
        self.downloadButtonFrame.pack_propagate(0)
        self.downloadButtonFrame.grid(row=5,column=0,padx=2,pady=2,sticky=S)
        self.downloadButton = Button(
            self.downloadButtonFrame, text="Start Download", command=self.startDownload)
        self.downloadButton.pack(fill='both',expand=1)

        self.selectedListFrame = Frame(self.downloadFrame,height=92,width=394)
        self.selectedListFrame.grid_propagate(0)
        self.selectedListFrame.pack_propagate(0)
        self.selectedListFrame.grid(row=0, column=0,padx=2,pady=2)
        Label(self.selectedListFrame, text="Paper Seleceted").grid(
            row=0, column=0)

        self.downloadProcessFrame=Frame(self.downloadFrame,height=92,width=194)
        self.downloadProcessFrame.grid_propagate(0)
        self.downloadProcessFrame.grid(row=0,column=1,padx=2,pady=2)
        #Label(self.downloadProcessFrame,text="Download Process").grid(row=0,column=0)

    def search(self):
        print("search start")
        self.qual = []
        if self.alFlag.get():
            self.qual += [r'/A%20Levels/']
        if self.olFlag.get():
            self.qual += [r'/O%20Levels/']
        if self.igFlag.get():
            self.qual += [r'/IGCSE/']
        # print(self.qual)
        if self.qual == []:
            messagebox.showwarning("warning", "No qualification selected")
            return
        if self.subjectSearched.get() == '':
            messagebox.showwarning("warning", 'No subject searched')
            return
        self.subFilFlag = True
        self.root.quit()

    def updateSubjectList(self, subList):
        print("update subject list")
        print(subList)
        self.subFilFlag = False
        self.subSelected = StringVar()
        for widget in self.subListFrame.winfo_children():
            widget.destroy()
        for sub in subList:
            Radiobutton(self.subListFrame, text=sub,
                        variable=self.subSelected, value=sub).pack(anchor='nw')

    def resetDetail(self):
        self.Syear = 0
        self.Eyear = 0

    def alt(self):
        self.Syear = self.syear.get()
        self.Eyear = self.eyear.get()
        if self.subSelected.get() == '':
            messagebox.showwarning("warning", 'No subject selected')
            self.resetDetail()
            return
        if self.syear.get() == '':
            messagebox.showwarning("warning", 'No start year entered')
            self.resetDetail()
            return
        if re.search("^[0-9]*$", self.syear.get()) == None:
            messagebox.showwarning(
                "warning", 'Enter a valid number in start year')
            self.resetDetail()
            return
        if int(self.syear.get() )<2000 or int(self.syear.get())>2030:
            messagebox.showwarning(
                "warning", 'Enter a valid number in start year')
            self.resetDetail()
            return
        if self.eyear.get() == '':
            messagebox.showwarning("warning", 'No end year entered')
            self.resetDetail()
            return
        if re.search("^[0-9]*$", self.eyear.get()) == None:
            messagebox.showwarning(
                "warning", 'Enter a valid number in end year')
            self.resetDetail()
            return
        if int(self.eyear.get()) < 2000 or int(self.eyear.get()) > 2030 or int(self.eyear.get())<int(self.syear.get()):
            messagebox.showwarning(
                "warning", 'Enter a valid number in end year')
            self.resetDetail()
            return
        if not(self.mFlag.get() or self.sFlag.get() or self.wFlag.get()):
            messagebox.showwarning("warning", 'No season selected')
            self.resetDetail()
            return
        if not(self.msFlag.get() or self.qpFlag.get() or self.inFlag.get() or self.gtFlag.get() or self.erFlag.get()):
            messagebox.showwarning("warning", 'No type of paper selected')
            self.resetDetail()
            return
        if re.search("^[0-9]+$", self.paper.get()) == None:
            messagebox.showwarning(
                "warning", "Enter paper wanted numbers only without split char")
            self.resetDetail()
            return
        self.altFlag = True
        self.root.quit()

    def alterSuccess(self, newDownloadList):
        self.updateDownloadList(newDownloadList)
        messagebox.showinfo("Message", "Apply success")
        self.altFlag = False

    def delete(self):
        self.delFlag = True
        self.root.quit()

    def deleteSuccess(self, newDownloadList):
        self.updateDownloadList(newDownloadList)
        messagebox.showinfo("Message", "Delete success")
        self.delFlag = False

    def updateDownloadList(self, downloadList):
        for widget in self.selectedListFrame.winfo_children():
            widget.destroy()
        Label(self.selectedListFrame, text='Paper selected:').pack(anchor='nw')
        for detail in downloadList.items():
            subject = detail[0]
            year = detail[1][0]
            season = detail[1][1]
            category = detail[1][2]
            paper = detail[1][3]
            detailString = "code"+re.search("\((\d\d\d\d)\)",subject).group(0)+'  '
            detailString += str(year[0])+'-'+str(year[1])+'  '
            detailString += 'm/' if season[0] else ' /'
            detailString += 's/' if season[1] else ' /'
            detailString += 'w' if season[2] else ' '
            detailString += '  '
            detailString += 'ms/' if category[0] else '  /'
            detailString += 'qp/' if category[1] else '  /'
            detailString += 'in/' if category[2] else '  /'
            detailString += 'gt/' if category[3] else '  /'
            detailString += 'er' if category[4] else '  '
            detailString+='  '
            detailString+='Paper '+paper
            print(detailString)
            Label(self.selectedListFrame, text=detailString).pack(anchor='nw')
        self.root.quit()

    def startDownload(self):
        self.downloadFlag = True
        Label(self.downloadProcessFrame,text="Download Starts, Please Wait",fg='red').grid(row=0,column=0)
        self.root.quit()
    def downloadStart(self):
        global rootDirection
        dir = askdirectory(initialdir=os.getcwd(),title='Select Download Path')
        if dir!='':
            rootDirection=dir+"\\past papers"
        messagebox.showinfo("message","Download Start")
        self.downloadFlag=False
    def downloadSuccess(self):
        messagebox.showinfo("message","Download success")
        self.downloadFlag = False
        self.destroy()
    
    #def updateDownloadStatus(self,message):
        #Label(self.downloadProcessFrame,text=message).pack()
        #self.root.quit()
    def resetFlag(self):
        self.downloadFlag=False
        self.delFlag=False
        self.altFlag=False
        self.subFilFlag=False
    def destroy(self):
        self.qFlag=True
        self.root.quit()
    def destroyEnd(self):
        self.root.destroy()
    def getInfo(self):
        self.root.mainloop()
        return self.subFilFlag, self.qual, self.subjectSearched.get(), self.altFlag, self.delFlag, self.subSelected.get(), (int(self.Syear), int(self.Eyear), False), (self.mFlag.get(), self.sFlag.get(), self.wFlag.get()), (self.msFlag.get(), self.qpFlag.get(), self.inFlag.get(), self.gtFlag.get(), self.erFlag.get()), self.paper.get(), self.downloadFlag, self.qFlag


inter = gui()
cc = app(inter)
cc.run()
