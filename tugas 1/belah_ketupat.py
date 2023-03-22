from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class ketupat:
    def __init__(self, diag1, diag2):
        self.diag1 = diag1
        self.diag2 = diag2
        
    def hitung_luas(self):
        return 0.5 * self.diag1 * self.diag2

class FrmBelahKetupat:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Masukan Panjang Diagonal Pertama:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan Panjang Diagonal Pertama:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Belah Ketupat:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        self.txtDiag1 = Entry(mainFrame)
        self.txtDiag1.grid(row=0, column=1, padx=5, pady=5)
        self.txtDiag2 = Entry(mainFrame)
        self.txtDiag2.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtLuasBelahKetupat = Entry(mainFrame)
        self.txtLuasBelahKetupat.grid(row=3, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    def onHitung(self, event=None):
        diag1 = float(self.txtDiag1.get())
        diag2 = float(self.txtDiag2.get())
        luas = 0.5 * diag1 * diag2
        self.txtLuasBelahKetupat.delete(0,END)
        self.txtLuasBelahKetupat.insert(END,str(round(luas,2)))
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmBelahKetupat(root, "Program Mencari Luas Belah Ketupat")
    root.mainloop() 