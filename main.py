from tkinter import Tk, Button, Entry

def igual():
    exp = pantalla.get()
    try:
        result = eval(exp)
        pantalla.delete(0, "end")
        pantalla.insert(0, str(result))
    except:
        pantalla.delete(0, "end")
        pantalla.insert(0, "Error")


def dar_click(num):
    num_actual = pantalla.get()
    num_nuevo = num_actual + str(num)
    pantalla.delete(0, "end")
    pantalla.insert(0, num_nuevo)


def punto():
    num_actual = pantalla.get()
    if "." not in num_actual:
        numero_nuevo = num_actual + "."
        pantalla.delete(0, "end")
        pantalla.insert(0, numero_nuevo)


root = Tk()
root.title('Calculadora POO')
root.resizable(0, 0)

pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: dar_click(9)).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=punto).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: dar_click("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: dar_click("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: dar_click("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: dar_click("/")).grid(row=4, column=3, padx=0, pady=1)


root.mainloop()