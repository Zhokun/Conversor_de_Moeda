from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import requests
import bs4


class Conversor(Tk):
    """
    Obs: Este program foi desenvolvido com intuito de praticar Web Scrapping para desenvolvimento de aplicação
    que converte valores de moeda. Programa desenvolvido por motivo de estudos.

    Ps: This system was developed with the intent to practice Web Scrapping for an app that would convert currency.
    This program was developed with study purpose only.
    """

    def __init__(self):
        Tk.__init__(self)
        self.x = 300
        self.y = 110
        self.geometry(f'{self.x}x{self.y}+'
                      f'{int(self.winfo_screenwidth()/2 - self.x/2)}+{int(self.winfo_screenheight()/2 - self.y/2)}')
        self.iconphoto(True, ImageTk.PhotoImage(Image.open('Da.png')))
        self.mostra_valor = StringVar()
        self.title('Conversor de moeda')

        # =========================================================================================================
        # Opção de moeda disponíveis para conversão
        self.f_row1 = Frame(self)
        self.f_row1.pack()
        self.options = ['EUR', 'BRL', 'USD', 'GBP', 'CAD']
        # Cria um evento para adicionar as opções de moeda
        self.dropdown_from = StringVar()
        self.dropdown_to = StringVar()
        self.dropdown_from.set(self.options[2])  # Insere as moedas no evento from
        self.dropdown_to.set(self.options[1])
        # Cria o menu para escolher o valor 'from/de'
        self.opt_from = OptionMenu(self.f_row1, self.dropdown_from, *self.options)
        self.opt_from.grid(row=0, column=2)
        # Cria o menu para escolher o valor 'to/para'
        self.opt_to = OptionMenu(self.f_row1, self.dropdown_to, *self.options)
        self.opt_to.grid(row=0, column=4)
        # =========================================================================================================
        # Sessão destinada à criação de labels, entries e do botão calcular, juntamente com o posicionamento de cada
        # elemento
        self.l_valor = Label(self.f_row1, text='Valor: ', font=('Verdana', 10))
        self.l_valor.grid(row=0, column=0, pady=5, padx=5)

        self.l_para = Label(self.f_row1, text='para', font=('Verdana', 10))
        self.l_para.grid(row=0, column=3)

        self.e_valor = Entry(self.f_row1, width=8, justify=RIGHT, font=('Verdana', 10))
        self.e_valor.grid(row=0, column=1)

        self.f_row2 = Frame(self)  # Frame para o botão
        self.f_row2.pack()
        self.b_calcular = Button(self.f_row2, text='Calcular', width=10, font=('Verdana', 12), command=self.valor)
        self.b_calcular.pack(pady=5)

        # =========================================================================================================
        # Exibe o resultado da conversão
        self.f_m_valor = Frame(self)  # Frame para o resultado
        self.f_m_valor.pack()
        self.l_mostra_valor = Label(self.f_m_valor, font=('Verdana', 14), fg='red')
        self.l_mostra_valor.pack()

    def valor(self):
        if self.e_valor.get():
            url = f"https://www.xe.com/pt/currencyconverter/convert/?Amount={self.e_valor.get()}&From={self.dropdown_from.get()}&To={self.dropdown_to.get()}"
            conn = requests.get(url)
            soup = bs4.BeautifulSoup(conn.content, 'html.parser')
            conn.close()

            resultado = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod').text
            string_size = 0
            for i, v in enumerate(resultado):
                if v == ',':
                    string_size = i+3
                    break

            self.l_mostra_valor.config(text=f"{resultado[:string_size]}")
        else:
            messagebox.showwarning('Warning', 'Please, enter a value to convert')


if __name__ == '__main__':
    app = Conversor()
    app.mainloop()
