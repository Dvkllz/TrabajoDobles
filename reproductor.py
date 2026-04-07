import tkinter as tk
from tkinter import messagebox, simpledialog

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current_node = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def move_forward(self):
        if self.current_node and self.current_node.next:
            self.current_node = self.current_node.next
            return True
        return False

    def move_backward(self):
        if self.current_node and self.current_node.prev:
            self.current_node = self.current_node.prev
            return True
        return False

    def get_all_values(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(temp.value)
            temp = temp.next
        return values

class PlayerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor Musical - Listas Dobles")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")
        
        self.playlist = DoublyLinkedList()
        
        title_label = tk.Label(root, text="Mi Lista de Reproducción", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=20)
        
        self.current_display = tk.Label(root, text="Ninguna canción en reproducción", font=("Helvetica", 12, "italic"), bg="#34495e", fg="#1abc9c", width=35, height=3)
        self.current_display.pack(pady=10)
        
        control_frame = tk.Frame(root, bg="#2c3e50")
        control_frame.pack(pady=10)
        
        self.btn_prev = tk.Button(control_frame, text="Anterior", command=self.previous_track, font=("Helvetica", 12), bg="#e74c3c", fg="white", width=10)
        self.btn_prev.grid(row=0, column=0, padx=10)
        
        self.btn_next = tk.Button(control_frame, text="Siguiente", command=self.next_track, font=("Helvetica", 12), bg="#e74c3c", fg="white", width=10)
        self.btn_next.grid(row=0, column=1, padx=10)
        
        tk.Label(root, text="--- Lista de Canciones ---", bg="#2c3e50", fg="white", font=("Helvetica", 10)).pack(pady=10)
        
        self.list_box = tk.Listbox(root, width=40, height=8, font=("Helvetica", 10))
        self.list_box.pack()
        
        self.btn_add = tk.Button(root, text="Agregar Canción", command=self.add_track, font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white", width=20)
        self.btn_add.pack(pady=20)

    def update_ui(self):
        if self.playlist.current_node:
            self.current_display.config(text=f"Reproduciendo:\n{self.playlist.current_node.value}")
        
        self.list_box.delete(0, tk.END)
        for track in self.playlist.get_all_values():
            marker = " (Actual)" if self.playlist.current_node and track == self.playlist.current_node.value else ""
            self.list_box.insert(tk.END, f"{track}{marker}")

    def add_track(self):
        track_name = simpledialog.askstring("Nueva Canción", "Ingresa el nombre de la canción:")
        if track_name:
            self.playlist.append(track_name)
            self.update_ui()

    def next_track(self):
        if not self.playlist.current_node:
            messagebox.showinfo("Aviso", "La lista está vacía.")
            return
        if not self.playlist.move_forward():
            messagebox.showinfo("Fin de la lista", "No hay más canciones hacia adelante.")
        self.update_ui()

    def previous_track(self):
        if not self.playlist.current_node:
            messagebox.showinfo("Aviso", "La lista está vacía.")
            return
        if not self.playlist.move_backward():
            messagebox.showinfo("Inicio de la lista", "Estás en la primera canción, no puedes retroceder.")
        self.update_ui()

if __name__ == "__main__":
    main_window = tk.Tk()
    app = PlayerUI(main_window)
    main_window.mainloop()