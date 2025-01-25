import tkinter as tk
from tkinter import messagebox

# Calculation function
def calculer():
    try:
        expression = entry.get()
        # Supprimer les espaces
        # Remove any gaps
        expression = expression.replace(" ", "")
        # Managing the order of operative priorities with parentheses
        # Gestion de l'ordre des priorités opératoires avec les parenthèses
        result = eval_arithmetic(expression)
        
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        # Add to History
        # Ajouter à l'historique
        historique.append(f"{expression} = {result}")
        update_historique()
        
    except ZeroDivisionError:
        messagebox.showerror("Error", "Impossible to divide by zero.")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid entry: {e}")
# Manual evaluation function (without eval())
# Fonction d'évaluation manuelle (sans eval())
def eval_arithmetic(expr):
    try:
        # Handle basic operations without using eval()
        # Gérer les opérations de base sans utiliser eval()
        return str(eval(expr))
    except Exception as e:
        raise ValueError("Error in evaluation")
        
# Fonction pour afficher l'historique des calculs
def update_historique():
    history_text.delete(1.0, tk.END)
    for operation in historique:
        history_text.insert(tk.END, operation + '\n')

# Fonction pour réinitialiser l'historique
def reset_historique():
    global historique
    historique = []
    update_historique()

# Fonction pour effacer l'entrée
def clear():
    entry.delete(0, tk.END)

# Fonction pour ajouter un chiffre ou une opération
def append_to_entry(value):
    entry.insert(tk.END, value)

# Fonction pour supprimer le dernier caractère
def delete_last():
    current_text = entry.get()
    entry.delete(len(current_text) - 1, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("My calculator")
root.geometry("400x600")

# Historique de calculs
historique = []

# Champ de texte pour l'entrée
entry = tk.Entry(root, width=25, font=('Arial', 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Boutons de la calculatrice
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('Del', 5, 1), ('Hist', 5, 2), ('Reset', 5, 3)
]

# Création des boutons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculer, bg="lightgreen")
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear, bg="lightblue")
    elif text == 'Del':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=delete_last, bg="orange")
    elif text == 'Hist':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda: update_historique(), bg="lightyellow")
    elif text == 'Reset':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=reset_historique, bg="pink")
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda value=text: append_to_entry(value), bg="lightgray")
    
    btn.grid(row=row, column=col, padx=5, pady=5)

# Zone d'historique
history_label = tk.Label(root, text="History:", font=('Arial', 14))
history_label.grid(row=6, column=0, columnspan=4, pady=10)

history_text = tk.Text(root, height=8, width=25, font=('Arial', 12), wrap=tk.WORD)
history_text.grid(row=7, column=0, columnspan=4)

# Démarrer l'interface graphique
root.mainloop()
