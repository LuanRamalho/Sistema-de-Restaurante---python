import tkinter as tk
from tkinter import ttk

def calculate_total():
    """Calcula o preço total dos itens selecionados."""
    total = 0
    for var, price in zip(checkbox_vars, prices):
        if var.get():
            total += price
    total_label.config(text=f"R${total:.2f}")
    calculate_change()

def calculate_change():
    """Calcula o troco com base no valor pago."""
    try:
        total = float(total_label.cget("text")[2:])
        payment = float(payment_entry.get())
        change = payment - total
        change_label.config(text=f"R${max(change, 0):.2f}")
    except ValueError:
        change_label.config(text="R$0.00")

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Restaurante")
root.geometry("450x700")
root.configure(bg="#f4f4f4")

# Estilo principal
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f4f4f4", foreground="#555")
style.configure("TFrame", background="#f4f4f4")

# Cabeçalho
header = tk.Label(root, text="Sistema de Restaurante", font=("Arial", 24, "bold"), bg="#6200ea", fg="white")
header.pack(fill="x", pady=20)

subheader = tk.Label(root, text="Escolha seus itens", font=("Arial", 16), bg="#f4f4f4", fg="#6200ea")
subheader.pack(pady=10)

# Frame para scroll
scroll_frame = tk.Frame(root)
scroll_frame.pack(fill="both", expand=True, pady=10)

canvas = tk.Canvas(scroll_frame, bg="#f4f4f4")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

content_frame = tk.Frame(canvas, bg="#fff")
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Itens e preços
items = [
    ("Bife a Cavalo", 15.00),
    ("Carne Comum", 10.00),
    ("Sopa", 8.00),
    ("Filé Mignon", 12.00),
    ("Bife à Milanesa", 15.00),
    ("Frango Comum", 7.50),
    ("Frango Empanado", 12.00),
    ("Linguiça Mineira", 11.50),
    ("Linguiça Toscana", 12.50),
    ("Linguiça Calabresa", 14.00),
    ("Legumes", 5.00),
    ("Refrigerante", 2.50),
    ("Suco", 1.50)
]

prices = [item[1] for item in items]
checkbox_vars = []

# Criação dos checkboxes dentro do content_frame
for item, price in items:
    var = tk.BooleanVar()
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(
        content_frame,
        text=f"{item} - R${price:.2f}",
        variable=var,
        font=("Arial", 12),
        bg="#fff",
        fg="#555",
        anchor="w",
        activebackground="#f4f4f4",
        command=calculate_total
    )
    checkbox.pack(fill="x", padx=20, pady=5)

# Ajuste do canvas para scroll
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", configure_canvas)

# Exibição do total
total_frame = tk.Frame(root, bg="#f4f4f4")
total_frame.pack(pady=10)

total_label_text = tk.Label(total_frame, text="Total: ", font=("Arial", 14), bg="#f4f4f4", fg="#6200ea")
total_label_text.pack(side="left")

total_label = tk.Label(total_frame, text="R$0.00", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#28a745")
total_label.pack(side="left")

# Entrada do pagamento
payment_entry = tk.Entry(root, font=("Arial", 14), justify="center", fg="#333")
payment_entry.pack(pady=10, padx=20)
payment_entry.insert(0, "Digite o valor pago")
payment_entry.bind("<FocusIn>", lambda e: payment_entry.delete(0, tk.END))
payment_entry.bind("<KeyRelease>", lambda e: calculate_change())

# Exibição do troco
change_frame = tk.Frame(root, bg="#f4f4f4")
change_frame.pack(pady=20)

change_label_text = tk.Label(change_frame, text="Troco: ", font=("Arial", 14), bg="#f4f4f4", fg="#6200ea")
change_label_text.pack(side="left")

change_label = tk.Label(change_frame, text="R$0.00", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#28a745")
change_label.pack(side="left")

# Inicia o loop principal
root.mainloop()
