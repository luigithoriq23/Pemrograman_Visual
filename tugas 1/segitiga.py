from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class Segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class FrmSegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill=BOTH, expand=YES)
        
        Label(main_frame, text='Masukan Alas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Masukan Tinggi:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text="Luas Segitiga:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        self.txtAlas = Entry(main_frame)
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(main_frame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(main_frame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(main_frame, text='Hitung', command=self.on_hitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)

    def on_hitung(self, event=None):
        try:
            alas = float(self.txtAlas.get())
            tinggi = float(self.txtTinggi.get())
            segitiga = Segitiga(alas, tinggi)
            luas = segitiga.hitung_luas()
            self.txtLuas.delete(0, END)
            self.txtLuas.insert(END, str(luas))
        except ValueError:
            pass

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmSegitiga(root, "Program Luas Segitiga")
    root.mainloop()
