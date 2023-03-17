from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
class frmsegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x280")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Alas' ). grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi" ).grid(row=1, column=0, sticky=W, padx=5, pady=5) 
        Label(mainFrame, text="S1").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="S2").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="S3").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas" ).grid(row=7, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling" ).grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.txtAlas = Entry(mainFrame)
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtS1 = Entry(mainFrame)
        self.txtS1.grid(row=3, column=1, padx=5, pady=5)
        self.txtS2 = Entry(mainFrame)
        self.txtS2.grid(row=4, column=1, padx=5, pady=5)
        self.txtS3 = Entry(mainFrame)
        self.txtS3.grid(row=5, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=7, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=8, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=6, column=1, padx=5, pady=5)

    def onHitung(self, event=0):
        Alas = int(self.txtAlas.get())
        Tinggi = int(self.txtTinggi.get())
        
        Luas = (Alas * Tinggi)/2
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(Luas))

        S1 = int(self.txtS1.get())
        S2 = int(self.txtS2.get())
        S3 = int(self.txtS3.get())

        Keliling = (S1 + S2 + S3)
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(Keliling))
    
 


    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__== '__main__':
    root = Tk()
    aplikasi = frmsegitiga(root, "Program Luas dan Keliling Segitiga")
    root.mainloop()