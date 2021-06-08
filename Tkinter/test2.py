import tkinter as tk
window = tk.Tk()
button=tk.Button(
    text = "Привет, мир",
    fg='white',  # цвет текста
    bg='yellow',  # цвет фона
    width=20,  #  ширина
    height=20 # высота
)

button.pack()
window.mainloop()
