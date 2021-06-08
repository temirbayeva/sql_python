import tkinter as tk
window = tk.Tk()
label=tk.Label(text="ИМЯ:")
entry=tk.Entry()
label.pack()
entry.pack()
name=entry.get()
window.mainloop()
