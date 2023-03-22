from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class PersegiBujurSangkar:
    def __init__(self, panjangsisi):
        self.panjangsisi = panjangsisi
        
    def hitung_luas(self):
        return self.panjangsisi ** 2
    
    def hitung_keliling(self):
        return 4 * self.panjangsisi

class Persegi(Frame):
    def __init__(self, parent, title):
        Frame.__init__(self, parent)
        self.parent = parent 
        self.parent.geometry("600x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill=BOTH, expand=YES)

        Label(main_frame, text='Masukan Panjang Sisi:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Luas Persegi atau Bujur Sangkar:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Keliling Persegi atau Bujur Sangkar:").grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.txtPanjangSisi = Entry(main_frame) 
        self.txtPanjangSisi.grid(row=0, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(main_frame) 
        self.txtLuas.grid(row=2, column=1, padx=5, pady=5) 
        self.txtKeliling = Entry(main_frame) 
        self.txtKeliling.grid(row=3, column=1, padx=5, pady=5) 
        
        btnHitung = Button(main_frame, text='Hitung', command=self.onHitung)
        btnHitung.grid(row=1, column=1, padx=5, pady=5)
        
    def onHitung(self):
        panjangsisi = int(self.txtPanjangSisi.get())
        persegi = PersegiBujurSangkar(panjangsisi)
        luas = persegi.hitung_luas()
        kel = persegi.hitung_keliling()
        
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(kel))
        
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk() 
    aplikasi = Persegi(root, "Program Luas dan Keliling Persegi atau Bujur Sangkar")
    root.mainloop()
