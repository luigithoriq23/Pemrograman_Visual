from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class Lingkaran:
    def __init__(self, jarijari):
        self.jarijari = jarijari
    
    def hitung_luas(self):
        return math.pi * (self.jarijari ** 2)
    
    def hitung_keliling(self):
        return 2 * math.pi * self.jarijari

class FrmLingkaran:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill=BOTH, expand=YES)
        
        Label(main_frame, text='Masukan Jari-Jari Lingkaran:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Luas Lingkaran:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Keliling Lingkaran:").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtJariJariLingkaran = Entry(main_frame)
        self.txtJariJariLingkaran.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(main_frame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(main_frame)
        self.txtKeliling.grid(row=4, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(main_frame, text='Hitung',
        command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    def onHitung(self, event=None):
        jarijari = float(self.txtJariJariLingkaran.get())
        lingkaran = Lingkaran(jarijari)
        luas = lingkaran.hitung_luas()
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(round(luas,2)))
        kel = lingkaran.hitung_keliling()
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(round(kel,2)))
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLingkaran(root, "Program Menghitung Keliling Luas Lingkaran")
    root.mainloop()