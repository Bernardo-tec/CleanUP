import tkinter as tk

def show_alert(message):
    root = tk.Tk()
    root.title("Alerta do Antivírus")
    label = tk.Label(root, text=message)
    label.pack()
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack()
    root.mainloop()

# Exemplo de uso
show_alert("Arquivo suspeito detectado!")