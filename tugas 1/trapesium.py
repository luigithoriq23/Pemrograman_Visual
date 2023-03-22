from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class Trapesium:
    def __init__(self, panjangAtas, panjangBawah, tinggiTrapesium):
        self.panjangAtas = panjangAtas
        self.panjangBawah = panjangBawah
        self.tinggiTrapesium = tinggiTrapesium
    
    def hitung_luas(self):
        return round(0.5 * (self.panjangAtas + self.panjangBawah) * self.tinggiTrapesium, 2)

class TrapesiumGUI:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill=BOTH, expand=YES)
        
        Label(main_frame, text='Masukan Panjang Sisi Atas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Masukan Panjang Sisi Bawah:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Masukan Tinggi Trapesium:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Luas Trapesium:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        
        self.txtPanjangAtas = Entry(main_frame)
        self.txtPanjangAtas.grid(row=0, column=1, padx=5, pady=5)
        self.txtPanjangBawah = Entry(main_frame)
        self.txtPanjangBawah.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiTrapesium = Entry(main_frame)
        self.txtTinggiTrapesium.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(main_frame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(main_frame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
    
    def onHitung(self, event=None):
        panjangAtas = float(self.txtPanjangAtas.get())
        panjangBawah = float(self.txtPanjangBawah.get())
        tinggiTrapesium = float(self.txtTinggiTrapesium.get())
        trapesium = Trapesium(panjangAtas, panjangBawah, tinggiTrapesium)
        luas = trapesium.hitung_luas()
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = TrapesiumGUI(root, "Program Luas Trapesium")
    root.mainloop()