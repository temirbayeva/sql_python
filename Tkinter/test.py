import tkinter as tk
window = tk.Tk()
label=tk.Label(
    text = "Привет, мир",
    fg='white',  # цвет текста
    bg='black',  # цвет фона
    width=20,  #  ширина
    height=20 # высота
)

label.pack()
window.mainloop()
