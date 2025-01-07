import tkinter as tk
from tkinter import messagebox

# Función para manejar las operaciones
def press(key):
    if key == "=":
        try:
            # Evaluar la expresión matemática
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Entrada inválida")
    elif key == "C":
        # Limpiar el campo de entrada
        entry.delete(0, tk.END)
    elif key == "Reiniciar":
        # Reiniciar la calculadora a su estado inicial
        entry.delete(0, tk.END)
        messagebox.showinfo("Reiniciar", "La calculadora se ha reiniciado.")
    else:
        # Insertar los números y operadores en el campo de entrada
        entry.insert(tk.END, key)

# Crear la ventana principal
root = tk.Tk()
root.title("SUPER CALCULADORA 3000")

# Crear un campo de entrada
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=8, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "Reiniciar"  # Botón adicional para reiniciar
]

# Crear y colocar los botones en una cuadrícula
row, col = 1, 0
for button in buttons:
    # Ajustar el ancho del botón de "Reiniciar"
    if button == "Reiniciar":
        tk.Button(root, text=button, width=20, height=2, font=("Arial", 14), command=lambda key=button: press(key)).grid(row=row, column=0, columnspan=4, padx=5, pady=5)
        row += 1
    else:
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18), command=lambda key=button: press(key)).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

# Iniciar la aplicación
root.mainloop()
