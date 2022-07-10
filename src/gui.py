from tkinter import *
import os
from tkinter import messagebox
import re
import os
from tkinter.filedialog import askdirectory

class gui():
    def __init__(self):
        self.root = Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)
        self.root.title("Past Paper Downloader")
        self.root.geometry('600x400')
        self.root.grid_propagate(0)
        self.root.resizable(False, False)
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
        self.subjectFrame = Frame(self.root, bg='red', height=296, width=396)
        self.subjectFrame.grid_propagate(0)
        self.subjectFrame.grid(row=0, column=0, sticky=NS,
                               padx=2, pady=2)
        self.detailFrame = Frame(self.root, bg='green', height=296, width=196)
        self.detailFrame.grid_propagate(0)
        self.detailFrame.grid(row=0, column=1, sticky=N,
                              padx=2, pady=2)
        self.downloadFrame = Frame(self.root, bg='blue', height=96, width=596)
        self.downloadFrame.grid_propagate(0)
        self.downloadFrame.grid(
            row=1, column=0, columnspan=2, sticky=NSEW, padx=2, pady=2)

        self.subjectFrame.rowconfigure(0, weight=1)
        self.subjectFrame.rowconfigure(1, weight=1)
        self.subjectFrame.rowconfigure(2, weight=10)
        self.qualiFrame = Frame(self.subjectFrame, height=25, width=392)
        self.qualiFrame.grid_propagate(0)
        self.qualiFrame.grid(row=0, column=0, sticky=W,
                             padx=2, pady=2)
        Checkbutton(self.qualiFrame, text="A/AS Level",
                    variable=self.alFlag).grid(row=0, column=0)
        Checkbutton(self.qualiFrame, text="O Level",
                    variable=self.olFlag).grid(row=0, column=1)
        Checkbutton(self.qualiFrame, text="IGCSE",
                    variable=self.igFlag).grid(row=0, column=2)

        self.subEntryFrame = Frame(self.subjectFrame, height=34, width=392)
        self.subEntryFrame.grid_propagate(0)
        self.subEntryFrame.grid(
            row=1, column=0, sticky=EW, padx=2, pady=0)
        Entry(self.subEntryFrame, textvariable=self.subjectSearched,
              width=49).grid(row=0, column=0, sticky=W, padx=0, pady=0)
        Button(self.subEntryFrame, text='Search',
               command=self.search).grid(row=0, column=1, sticky=NS, padx=0, pady=0)

        self.subListFrame = Frame(self.subjectFrame, height=235, width=392)
        self.subListFrame.grid_propagate(0)
        self.subListFrame.pack_propagate(0)
        self.subListFrame.grid(row=2, column=0, padx=2, pady=2)

        self.yearFrame = Frame(self.detailFrame, height=50, width=192)
        self.yearFrame.grid_propagate(0)
        self.yearFrame.grid(row=0, column=0, padx=2, pady=2)
        Label(self.yearFrame, text="Year").grid(
            row=0, column=0, columnspan=3, sticky=W)
        Entry(self.yearFrame, textvariable=self.syear,
              width=10).grid(row=1, column=0, sticky=W)
        Label(self.yearFrame, text='-').grid(row=1, column=1, sticky=W)
        Entry(self.yearFrame, textvariable=self.eyear,
              width=10).grid(row=1, column=2, sticky=W)

        self.seasonFrame = Frame(self.detailFrame, height=25, width=192)
        self.seasonFrame.grid_propagate(0)
        self.seasonFrame.grid(row=1, column=0, padx=2, pady=0)
        Checkbutton(self.seasonFrame, text="m",
                    variable=self.mFlag).grid(row=0, column=0, sticky=W)
        Checkbutton(self.seasonFrame, text="s",
                    variable=self.sFlag).grid(row=0, column=1, sticky=W)
        Checkbutton(self.seasonFrame, text="w",
                    variable=self.wFlag).grid(row=0, column=2, sticky=W)

        self.typeFrame = Frame(self.detailFrame, height=50, width=192)
        self.typeFrame.grid_propagate(0)
        self.typeFrame.grid(row=2, column=0, padx=2, pady=2)
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

        self.paperFrame = Frame(self.detailFrame, height=50, width=192)
        self.paperFrame.grid_propagate(0)
        self.paperFrame.grid(row=3, column=0, padx=2, pady=0)
        Label(self.paperFrame, text="Paper").grid(row=0, column=0, sticky=W)
        Entry(self.paperFrame, textvariable=self.paper).grid(
            row=1, column=0, sticky=W)

        self.detailButtonFrame = Frame(self.detailFrame, height=44, width=192)
        self.detailButtonFrame.grid_propagate(0)
        self.detailButtonFrame.grid(row=4, column=0, padx=2, pady=2)
        self.altButtonFrame = Frame(
            self.detailButtonFrame, height=40, width=92, bg='blue')
        self.altButtonFrame.grid_propagate(0)
        self.altButtonFrame.pack_propagate(0)
        self.altButtonFrame.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        self.deleButtonFrame = Frame(
            self.detailButtonFrame, height=40, width=92, bg='blue')
        self.deleButtonFrame.grid_propagate(0)
        self.deleButtonFrame.pack_propagate(0)
        self.deleButtonFrame.grid(row=0, column=1, sticky=E, padx=2, pady=2)
        self.altButton = Button(self.altButtonFrame,
                                text='apply', command=self.alt)
        self.altButton.pack(fill="both", expand=1)
        self.deleButton = Button(
            self.deleButtonFrame, text='delete', command=self.delete)
        self.deleButton.pack(fill="both", expand=1)

        self.downloadButtonFrame = Frame(
            self.detailFrame, height=60, width=192)
        self.downloadButtonFrame.pack_propagate(0)
        self.downloadButtonFrame.grid(
            row=5, column=0, padx=2, pady=2, sticky=S)
        self.downloadButton = Button(
            self.downloadButtonFrame, text="Select Download Path\n&\nStart Download", command=self.startDownload)
        self.downloadButton.pack(fill='both', expand=1)

        self.selectedListFrame = Frame(
            self.downloadFrame, height=92, width=394)
        self.selectedListFrame.grid_propagate(0)
        self.selectedListFrame.pack_propagate(0)
        self.selectedListFrame.grid(row=0, column=0, padx=2, pady=2)
        Label(self.selectedListFrame, text="Paper Seleceted").grid(
            row=0, column=0)

        self.downloadProcessFrame = Frame(
            self.downloadFrame, height=92, width=194)
        self.downloadProcessFrame.grid_propagate(0)
        self.downloadProcessFrame.grid(row=0, column=1, padx=2, pady=2)
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
        if int(self.syear.get()) < 2000 or int(self.syear.get()) > 2030:
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
        if int(self.eyear.get()) < 2000 or int(self.eyear.get()) > 2030 or int(self.eyear.get()) < int(self.syear.get()):
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
        #messagebox.showinfo("Message", "Apply success")
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
            detailString = re.search("\((\d\d\d\d)\)", subject).group(0)+'  '
            detailString += str(year[0])+'-'+str(year[1])+'  '
            detailString += 'm/' if season[0] else '*/'
            detailString += 's/' if season[1] else '*/'
            detailString += 'w' if season[2] else '*'
            detailString += '  '
            detailString += 'ms/' if category[0] else '**/'
            detailString += 'qp/' if category[1] else '**/'
            detailString += 'in/' if category[2] else '**/'
            detailString += 'gt/' if category[3] else '**/'
            detailString += 'er' if category[4] else '**'
            detailString += '  '
            detailString += 'Paper '+paper
            print(detailString)
            Label(self.selectedListFrame, text=detailString).pack(anchor='nw')
        self.root.quit()

    def startDownload(self):
        self.downloadFlag = True
        Label(self.downloadProcessFrame, text="Download Starts, Please Wait",
              fg='red').grid(row=0, column=0)
        self.root.quit()

    def downloadStart(self):
        self.rootDirection = os.getcwd()+r"/pastpapers"
        dir = askdirectory(initialdir=os.getcwd(),
                           title='Select Download Path')
        if dir != '':
            self.rootDirection = dir+"/past papers"
        messagebox.showinfo("message", "Download Start")
        self.downloadFlag = False

    def downloadSuccess(self):
        messagebox.showinfo("message", "Download success")
        self.downloadFlag = False
        self.destroy()

    #def updateDownloadStatus(self,message):
        #Label(self.downloadProcessFrame,text=message).pack()
        #self.root.quit()
    def resetFlag(self):
        self.downloadFlag = False
        self.delFlag = False
        self.altFlag = False
        self.subFilFlag = False

    def destroy(self):
        self.qFlag = True
        self.root.quit()

    def destroyEnd(self):
        self.root.destroy()

    def getInfo(self):
        self.root.mainloop()
        return self.subFilFlag, self.qual, self.subjectSearched.get(), self.altFlag, self.delFlag, self.subSelected.get(), (int(self.Syear), int(self.Eyear), False), (self.mFlag.get(), self.sFlag.get(), self.wFlag.get()), (self.msFlag.get(), self.qpFlag.get(), self.inFlag.get(), self.gtFlag.get(), self.erFlag.get()), self.paper.get(), self.downloadFlag, self.qFlag
