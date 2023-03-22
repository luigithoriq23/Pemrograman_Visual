from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class layang:
    def __init__(self, sisiPertama, sisiKedua):
        self.sisiPertama = sisiPertama
        self.sisiKedua = sisiKedua
        
    def hitung_keliling(self):
        return 2 * (self.sisiPertama + self.sisiKedua)

class FrmLayangLayang:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Masukan Sisi Pertama:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan Sisi Kedua:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling Layang-Layang:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        self.txtSisiPertama = Entry(mainFrame)
        self.txtSisiPertama.grid(row=0, column=1, padx=5, pady=5)
        self.txtSisiKedua = Entry(mainFrame)
        self.txtSisiKedua.grid(row=1, column=1, padx=5, pady=5)
        
        
        self.txtKelilingLayangLayang = Entry(mainFrame)
        self.txtKelilingLayangLayang.grid(row=3, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(mainFrame, text='Hitung',
        command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    def onHitung(self, event=None):
        sisiPertama = float(self.txtSisiPertama.get())
        sisiKedua = float(self.txtSisiKedua.get())
        layangan = layang(sisiPertama, sisiKedua)
        kel = layangan.hitung_keliling()
        self.txtKelilingLayangLayang.delete(0, END)
        self.txtKelilingLayangLayang.insert(END, int(kel))
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLayangLayang(root, "Program Keliling Layang Layang")
    root.mainloop() 