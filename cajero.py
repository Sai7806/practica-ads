import tkinter as tk
from tkinter import messagebox



def ia_cajero():
  try:

    monto = int(entrada_monto.get())
    if monto <= 0:
      messagebox.showerror("error", "monto invalido")
      return
    billetes = [100000, 50000, 20000, 10000, 5000, 2000]
    resultado_texto = ""

    for billete in billetes:
      cantidad = monto // billete

      if cantidad > 0:
        resultado_texto += f"{cantidad} billetes de {billete}\n"
        monto %= billete
    if monto > 0:
     resultado_texto += f"te sobraron {monto} que no son posibles de entregar en billetes"
    etiqueta_resultado.config(text=resultado_texto, fg="#00ff00")

  except ValueError:
    messagebox.showerror("error", "monto invalido")


ventana = tk.Tk()
ventana.title("Cajero ADSO Ultimate 🏧")
ventana.geometry("400x500")
ventana.configure(bg="#1e1e1e") # Fondo oscuro tipo VS Code

# Título
tk.Label(ventana, text="CAJERO AUTOMÁTICO", font=("Arial", 18, "bold"), 
         bg="#1e1e1e", fg="white").pack(pady=20)

# Entrada de dinero
tk.Label(ventana, text="¿Cuánto vas a retirar?", bg="#1e1e1e", fg="#ccc").pack()
entrada_monto = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada_monto.pack(pady=10)

# Botón de acción
boton_retirar = tk.Button(ventana, text="RETIRAR PLATA", command=ia_cajero,
                          bg="#007acc", fg="white", font=("Arial", 12, "bold"),
                          padx=20, pady=10)
boton_retirar.pack(pady=20)

# Área de resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), 
                              bg="#1e1e1e", fg="white", justify="left")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()

