from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

# Nama: Galang Anggara
# NIM: 231511014
# Kelas: TI22B/R2

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def onHitung(self):
        R = int(self.txtReamur.get())
        valueC = 5/4 * R
        valueF = (9/4 * R) + 34 
        valueK = 5/4 * R + 273

        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(valueC))
        self.txtFahrenheit.delete(0,END)
        self.txtFahrenheit.insert(END,str(valueF))
        self.txtKelvin.delete(0,END)
        self.txtKelvin.insert(END,str(valueK))
    
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)      
        # Label
        Label(mainFrame, text='Reamur:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # textbox
        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=0, column=1, padx=5, pady=5)  
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius .grid(row=2, column=1, padx=5, pady=5)
        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit .grid(row=3, column=1, padx=5, pady=5)
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin .grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung, bg="purple", fg="white", font=("Arial", 10, "bold"))
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
            
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmSuhu(root, "Aplikasi Konversi Suhu Reamur")
    root.mainloop() 