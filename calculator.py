import tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry("500x500")

font_general = font.Font(size=20, family="Arial")

eingabe = tk.Entry(root, font=font_general, borderwidth=20, bg="#064E3B", fg="#D1FAE5")
eingabe.grid(row=0, column=0, columnspan=4, sticky="nswe")

def addChar(char):
    eingabe.insert(tk.END, char)

def clear_entry():
    eingabe.delete(0, tk.END)

def show_results():

    try:
        resutl = eval(eingabe.get())
        eingabe.delete(0, tk.END)
        eingabe.insert(0, str(resutl))

    except: 
        eingabe.delete(0, tk.END)
        eingabe.insert(0, str('Error'))

buttons = [
    ("7", lambda: addChar('7'), "#134E4A", "#CCFBF1"),
    ("8", lambda: addChar('8'), "#134E4A", "#CCFBF1"),
    ("9", lambda: addChar('9'), "#134E4A", "#CCFBF1"),
    ("clear", clear_entry, "#134E4A", "#CCFBF1"),
    ("4", lambda: addChar('4'), "#164E63", "#CFFAFE"),
    ("5", lambda: addChar('5'), "#164E63", "#CFFAFE"),
    ("6", lambda: addChar('6'), "#164E63", "#CFFAFE"),
    ("-", lambda: addChar('-'), "#164E63", "#CFFAFE"),
    ("1", lambda: addChar('1'), "#0C4A6E", "#E0F2FE"),
    ("2", lambda: addChar('2'), "#0C4A6E", "#E0F2FE"),
    ("3", lambda: addChar('3'), "#0C4A6E", "#E0F2FE"),
    ("+", lambda: addChar('+'), "#0C4A6E", "#E0F2FE"),
    ("*", lambda: addChar('*'), "#1E3A8A", "#DBEAFE"),
    ("0", lambda: addChar('0'), "#1E3A8A", "#DBEAFE"),
    ("/", lambda: addChar('/'), "#1E3A8A", "#DBEAFE"),
    ("=", show_results, "#1E3A8A", "#DBEAFE")
]

row_idx = 1
col_idx = 0
for text, command, bg, fg in buttons:
    button = tk.Button(root, text=text, font=font_general, command=command, bg=bg, fg=fg)
    button.grid(row=row_idx, column=col_idx, sticky="nswe")
    col_idx += 1
    if col_idx > 3:
        col_idx = 0
        row_idx += 1

for column in range(4):
    root.columnconfigure(column, weight=1)

for row in range(5):
    root.rowconfigure(row, weight=1)

root.mainloop()

