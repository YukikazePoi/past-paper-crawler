# application module

from tkinter import *
import socket
import threading
from sys import exit
from fileHierchy import *


"""
Communication with interface module:
    getInfo()
    updateSubjectList(list of subjects in string)
    deleteSuccess()
    downloadStart()
    downloadSuccess()
    destroyEnd()
    refer to fileHierchy.folder.downloadAllSelected()
"""

class app():
    def __init__(self, interface):#initialize variables
        self.root = folder("https://papers.gceguide.com", "/")
        # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        socket.setdefaulttimeout(20)
        self.root.findList()
        self.inter = interface
        self.root.findByCriteria(".*")
        self.downloadList = {}
        self.downloadingFlag = False

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

    def download(self):  # Start download process
        self.downloadingFlag = True
        self.inter.updateDownloadTitle("(Fetching Address)")
        for detail in self.downloadList.items():
            subject = detail[0]
            year = detail[1][0]
            season = detail[1][1]
            category = detail[1][2]
            paper = detail[1][3]  # extract details
            for q in self.root.sons:
                for s in q.sons:
                    if s.name == subject: # build normal expression
                        yearCriteria = ''
                        for y in range(year[0], year[1]+1):
                            yearCriteria += str(y)+'|'
                        if year[2]:
                            yearCriteria += 'Specimen|'
                        yearCriteria = yearCriteria[:-1]
                        paperCriteria = '_['
                        if season[0]:
                            paperCriteria += 'm'
                        if season[1]:
                            paperCriteria += 's'
                        if season[2]:
                            paperCriteria += 'w'
                        if category[0] or category[1] or category[2]:
                            paperCriteria += r']\d\d_(('
                            if category[0]:
                                paperCriteria += 'ms|'
                            if category[1]:
                                paperCriteria += 'qp|'
                            if category[2]:
                                paperCriteria += 'in|'
                            paperCriteria = paperCriteria[:-1]
                            paperCriteria += ')_['+paper+'][123]?|'
                        else:
                            paperCriteria += r']\d\d_('
                        if category[3]:
                            paperCriteria += 'gt|'
                        if category[4]:
                            paperCriteria += 'er|'
                        paperCriteria = paperCriteria[:-1]
                        paperCriteria += ')'
                        s.findList()
                        s.findByCriteria(yearCriteria)
                        for year in s.sons:
                            year.findList()
                            year.findByCriteria(paperCriteria)
                        print("find %s end" % subject)
        print("start download")
        num=self.root.countFileNum()
        self.inter.downloadTotal=num
        self.inter.updateDownloadTitle("(0/%d)"%num)
        self.root.downloadAllSelected(self.inter)
        self.inter.downloadSuccess()

    def run(self):
        while True:
            #applySubFil, qual, sub, alt, dele, subject, year, season, category, paper, download, quit = self.inter.getInfo()
            applySubFil, alt, dele, download, quit = self.inter.getFlag()
            if not self.downloadingFlag:
                if applySubFil:
                    qual, sub=self.inter.getSubFilInfo()
                    sublist = self.applySubjectFilter(qual, sub)
                    self.inter.updateSubjectList(sublist)
                elif alt:
                    subject, year, season, category, paper=self.inter.getSubDetInfo()
                    self.alterDownloadList(
                        subject, year, season, category, paper)
                    self.inter.alterSuccess(self.downloadList)
                elif dele:
                    subject, year, season, category, paper = self.inter.getSubDetInfo()
                    self.delDownloadList(subject)
                    self.inter.deleteSuccess(self.downloadList)
                elif download:
                    self.inter.downloadStart()
                    download = threading.Thread(target=self.download)
                    download.setDaemon(True)
                    download.start()
            if quit:
                self.inter.destroyEnd()
                exit(0)
