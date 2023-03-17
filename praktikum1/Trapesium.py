from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
class FrmTrapesium:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("250x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Sisi a').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi b").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi c").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi d").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Luas").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling").grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.txtSa = Entry(mainFrame)
        self.txtSa.grid(row=0, column=1, padx=5, pady=5)
        self.txtSb = Entry(mainFrame)
        self.txtSb.grid(row=1, column=1, padx=5, pady=5)
        self.txtSc = Entry(mainFrame)
        self.txtSc.grid(row=2, column=1, padx=5, pady=5)
        self.txtSd = Entry(mainFrame)
        self.txtSd.grid(row=3, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=4, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=6, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=5, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        Sa = int(self.txtSa.get())    
        Sb = int(self.txtSb.get())
        Sc = int(self.txtSc.get())    
        Sd = int(self.txtSd.get())
        T= int(self.txtTinggi.get())

        Kel = Sa + Sb + Sc + Sd
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(Kel))
        Luas = ((Sa+Sb)*T)/2
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(Luas))
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__' :
    root = Tk()
    aplikasi = FrmTrapesium(root, "Program Luas dan Trapesium" )
    root.mainloop()

            
    

