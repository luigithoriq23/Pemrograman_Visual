from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
class FrmLingkaran:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("250x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Jari-Jari:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        self.txtjarijari = Entry(mainFrame)
        self.txtjarijari.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=2, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=3, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        r = int(self.txtjarijari.get())
        phi = 22/7

        luas = phi*r*r
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END, str(luas))

        kel = 2*phi*r
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END, str(kel))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLingkaran(root, "Program Luas dan Keliling Lingkaran")
    root.mainloop()




