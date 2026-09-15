from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_letter():
    p = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not p:
        return
    txt_edit.delete("1.0", END)
    with open(p, "r") as f:
        txt_edit.insert(END, f.read())
    w.title(p)

def save_letter():
    p = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not p:
        return
    with open(p, "w") as f:
        f.write(txt_edit.get("1.0", END))
    w.title(p)

w = Tk()
w.title("Letter Writing Application")
w.geometry("600x500")
w.rowconfigure(0, weight=1)
w.columnconfigure(1, weight=1)

txt_edit = Text(w)
fr_buttons = Frame(w, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open Letter", command=open_letter)
btn_save = Button(fr_buttons, text="Save Letter As...", command=save_letter)

btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

w.mainloop()
