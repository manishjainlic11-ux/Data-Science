import tkinter as a
from tkinter import ttk as b, messagebox as c
from PIL import Image, ImageTk  # Imports Pillow to handle the JPG file easily

class X:
    def __init__(self, d):
        self.d = d
        self.d.title("Stationery Order Management App")
        self.m = {"NOTEBOOK": 3, "PENCIL PACK": 2, "PEN SET": 4, "ERASER": 1, "GEOMETRY BOX": 6, "COLOUR PENCILS": 5}
        self.e = 82
        self.g(d)
        f = b.Frame(d)
        f.place(relx=0.5, rely=0.5, anchor=a.CENTER)
        b.Label(f, text="Stationery Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)
        self.l = {}
        self.q = {}
        for i, (k, v) in enumerate(self.m.items(), start=1):
            lbl = b.Label(f, text=f"{k} (${v}):", font=("Arial", 12))
            lbl.grid(row=i, column=0, padx=10, pady=5)
            self.l[k] = lbl
            ent = b.Entry(f, width=5)
            ent.grid(row=i, column=1, padx=10, pady=5)
            self.q[k] = ent
        self.v = a.StringVar()
        b.Label(f, text="Currency:", font=("Arial", 12)).grid(row=len(self.m) + 1, column=0, padx=10, pady=5)
        drp = b.Combobox(f, textvariable=self.v, state="readonly", width=18, values=("USD", "INR"))
        drp.grid(row=len(self.m) + 1, column=1, padx=10, pady=5)
        drp.current(0)
        self.v.trace_add("write", self.u)
        btn = b.Button(f, text="Place Order", command=self.p)
        btn.grid(row=len(self.m) + 2, columnspan=3, padx=10, pady=10)

    def g(self, d):
        w, h = 800, 600
        cv = a.Canvas(d, width=w, height=h)
        cv.pack()
        
        # Opens your exact "hi.jpg" file using Pillow
        o = Image.open("hi.jpg")
        
        o_resized = o.resize((w, h))
        bi = ImageTk.PhotoImage(o_resized)
        cv.create_image(0, 0, anchor=a.NW, image=bi)
        cv.image = bi

    def u(self, *args):
        c_cy = self.v.get()
        s = "₹" if c_cy == "INR" else "$"
        rt = self.e if c_cy == "INR" else 1
        for k, lbl in self.l.items():
            lbl.config(text=f"{k} ({s}{self.m[k] * rt}):")

    def p(self):
        tc = 0
        sm = "Stationery Order Summary:\n"
        c_cy = self.v.get()
        s = "₹" if c_cy == "INR" else "$"
        rt = self.e if c_cy == "INR" else 1
        for k, ent in self.q.items():
            qty = ent.get()
            if qty.isdigit():
                qty = int(qty)
                prc = self.m[k] * rt
                cst = qty * prc
                tc += cst
                if qty > 0:
                    sm += f"{k}: {qty} x {s}{prc} = {s}{cst}\n"
        if tc > 0:
            sm += f"\nTotal Cost: {s}{tc}"
            c.showinfo("Order Placed", sm)
        else:
            c.showerror("Error", "Please order at least one stationery item.")

if __name__ == "__main__":
    r = a.Tk()
    z = X(r)
    r.geometry("800x600")
    r.mainloop()
