import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import os

class DigitalDiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hacker's Digital Diary")
        self.root.geometry("650x500")
        self.root.configure(bg="#0f0f0f")
        self.filename = 'diary_entries.txt'
        self.entries = self.load_entries()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="HACKER'S DIARY", font=("Courier", 20, "bold"), bg="#0f0f0f", fg="#00ff00").pack(pady=15)
        self.entry_text = tk.Text(self.root, height=8, width=60, font=("Courier", 12), bg="#1c1c1c", fg="#00ff00", insertbackground="#00ff00")
        self.entry_text.pack(pady=10)
        btn_frame = tk.Frame(self.root, bg="#0f0f0f")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="SAVE ENTRY", font=("Courier", 12, "bold"), bg="#00ff00", fg="#0f0f0f", command=self.save_entry).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="VIEW/EDIT ENTRIES", font=("Courier", 12, "bold"), bg="#00ff00", fg="#0f0f0f", command=self.view_entries).grid(row=0, column=1, padx=10)

    def load_entries(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [line.split('::', 1) for line in file if line.strip()]
        return []

    def save_entry(self):
        entry = self.entry_text.get("1.0", "end-1c").strip()
        if entry:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.entries.append([timestamp, entry])
            with open(self.filename, 'a') as file:
                file.write(f"{timestamp}::{entry}\n")
            self.entry_text.delete("1.0", "end")
            messagebox.showinfo("Success", "Entry saved!")
        else:
            messagebox.showwarning("Empty Entry", "Please write something before saving.")

    def view_entries(self):
        if not self.entries:
            messagebox.showinfo("No Entries", "No diary entries found.")
        else:
            self.show_entries_window()

    def show_entries_window(self):
        win = tk.Toplevel(self.root)
        win.title("View/Edit Entries")
        win.geometry("600x450")
        win.configure(bg="#0f0f0f")
        listbox = tk.Listbox(win, font=("Courier", 12), bg="#1c1c1c", fg="#00ff00", selectbackground="#00ff00")
        listbox.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(listbox)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        for i, entry in enumerate(self.entries):
            listbox.insert("end", f"Entry {i+1}: {entry[0]}")

        tk.Button(win, text="EDIT SELECTED ENTRY", font=("Courier", 12, "bold"), bg="#00ff00", fg="#0f0f0f", command=lambda: self.edit_entry(listbox)).pack(pady=10)

    def edit_entry(self, listbox):
        sel = listbox.curselection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select an entry to edit.")
            return
        idx = sel[0]
        new_text = simpledialog.askstring("Edit Entry", "Edit your entry:", initialvalue=self.entries[idx][1])
        if new_text is not None:
            self.entries[idx][1] = new_text
            self.save_all_entries()
            messagebox.showinfo("Success", "Entry updated!")

    def save_all_entries(self):
        with open(self.filename, 'w') as file:
            for entry in self.entries:
                file.write(f"{entry[0]}::{entry[1]}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalDiaryApp(root)
    root.mainloop()
