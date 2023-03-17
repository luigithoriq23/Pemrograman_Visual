from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math 
class FrmBelah_Ketupat:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='d1:' ).grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="d2:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.txtd1 = Entry(mainFrame)
        self.txtd1.grid(row=0, column=1, padx=5, pady=5)
        self.txtd2 = Entry(mainFrame)
        self.txtd2.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        d1 = int(self.txtd1.get())
        d2 = int(self.txtd2.get())  
        
        S = math.sqrt(pow(d1/2, 2) + pow(d2/2, 2))
        
        luas = (d1*d2)/2
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        kel = S*4
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(kel))
    
    def onKeluar(self, event=None):
        self.parent.destroy()
if __name__ == '__main__' :
    root = Tk()
    aplikasi = FrmBelah_Ketupat(root, "Program Luas dan Keliling Belah Ketupat" )
    root.mainloop()