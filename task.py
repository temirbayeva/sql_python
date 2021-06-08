import tkinter as tk
def changtext():
    edit.delete(0, 'end')
window = tk.Tk()
t1 = tk.Label(window, text='Enter your text',fg='red')
t1.pack()
edit=tk.Entry(window, width=30, bg='pink')
edit.pack()
but=tk.Button(window, text='Puch', command=changtext)
but.pack()
window.mainloop()
