from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
class FrmLayang2:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("250x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Diagonal 1').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Diagonal 2").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 1").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 2").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 3").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 4").grid(row=5, column=0, sticky=W, padx=5, pady=5)
       
        Label(mainFrame, text="Luas").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling").grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.txtD1 = Entry(mainFrame)
        self.txtD1.grid(row=0, column=1, padx=5, pady=5)
        self.txtD2 = Entry(mainFrame)
        self.txtD2.grid(row=1, column=1, padx=5, pady=5)
        self.txtS1 = Entry(mainFrame)
        self.txtS1.grid(row=2, column=1, padx=5, pady=5)
        self.txtS2 = Entry(mainFrame)
        self.txtS2.grid(row=3, column=1, padx=5, pady=5)
        self.txtS3 = Entry(mainFrame)
        self.txtS3.grid(row=4, column=1, padx=5, pady=5)
        self.txtS4 = Entry(mainFrame)
        self.txtS4.grid(row=5, column=1, padx=5, pady=5)

        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=7, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=8, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=6, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        D1 = int(self.txtD1.get())
        D2 = int(self.txtD2.get())
        luas = (D1*D2)/2
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
           
        S1 = int(self.txtS1.get())
        S1 = int(self.txtS1.get())
        S2 = int(self.txtS2.get())
        S3 = int(self.txtS3.get())
        S4 = int(self.txtS4.get())
        kel = S1+S2+S3+S4
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(kel))
    
    def onKeluar(self, event=None):
            self.parent.destroy()

if __name__ == '__main__' :
    root = Tk()
    aplikasi = FrmLayang2(root, "Program Luas dan Keliling Layang-Layang" )
    root.mainloop()