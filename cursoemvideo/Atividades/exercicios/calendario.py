import tkinter as tk
import calendar


def showCal():
    new_gui = tk.Tk()
    new_gui.config(background='white')
    new_gui.title('CALNENDÁRIO',)
    new_gui.geometry('550x600')
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = tk.Label(new_gui, text=cal_content, font='Consolas 10 bold')
    cal_year.grid(row=5, column=1, padx=20)
    new_gui.mainloop()


if __name__ == '__main__':
    gui = tk.Tk()
    gui.config(background='white')
    gui.title('CALENDÁRIO')
    gui.geometry('300x210')
    cal = tk.Label(gui, text='CALENDÁRIO', bg='dark gray', font=('times', 28, 'bold'))
    year = tk.Label(gui, text='Informe o ano', bg='light green')
    year_field = tk.Entry(gui)
    Show = tk.Button(gui, text='Mostrar calendário', fg='Black', bg='Red', command=showCal)
    Exit = tk.Button(gui, text='Sair', fg='Black', bg='Red', command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    gui.mainloop()
