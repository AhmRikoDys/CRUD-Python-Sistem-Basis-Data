import customtkinter as ctk
from tkinter import ttk
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==========================
# DATABASE
# ==========================
conn = sqlite3.connect("siakad.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mahasiswa (
    nama TEXT,
    nbi TEXT PRIMARY KEY,
    kelas TEXT
)
""")
conn.commit()

# ==========================
# FUNCTION
# ==========================
def refresh():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

    # Dashboard update
    total_label.configure(text=f"Total Mahasiswa: {len(data)}")

def tambah():
    nama = entry_nama.get()
    nbi = entry_nbi.get()
    kelas = entry_kelas.get()

    try:
        cursor.execute("INSERT INTO mahasiswa VALUES (?, ?, ?)", (nama, nbi, kelas))
        conn.commit()
        refresh()
    except:
        pass

def hapus():
    selected = tree.focus()
    if selected:
        data = tree.item(selected)["values"]
        cursor.execute("DELETE FROM mahasiswa WHERE nbi=?", (data[1],))
        conn.commit()
        refresh()

def update():
    selected = tree.focus()
    if selected:
        data = tree.item(selected)["values"]
        cursor.execute("UPDATE mahasiswa SET nama=?, kelas=? WHERE nbi=?",
                       (entry_nama.get(), entry_kelas.get(), data[1]))
        conn.commit()
        refresh()

def pilih(event):
    selected = tree.focus()
    if selected:
        data = tree.item(selected)["values"]
        entry_nama.delete(0, "end")
        entry_nbi.delete(0, "end")
        entry_kelas.delete(0, "end")

        entry_nama.insert(0, data[0])
        entry_nbi.insert(0, data[1])
        entry_kelas.insert(0, data[2])

def search(event):
    keyword = search_entry.get()

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM mahasiswa WHERE nama LIKE ? OR nbi LIKE ?",
                   ('%' + keyword + '%', '%' + keyword + '%'))

    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# ==========================
# UI
# ==========================
app = ctk.CTk()
app.title("SIAKAD MODERN")
app.geometry("900x600")

# ==========================
# DASHBOARD
# ==========================
dashboard = ctk.CTkFrame(app)
dashboard.pack(pady=10, padx=10, fill="x")

total_label = ctk.CTkLabel(dashboard, text="Total Mahasiswa: 0", font=("Arial", 18))
total_label.pack(pady=10)

# ==========================
# INPUT
# ==========================
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

entry_nama = ctk.CTkEntry(frame, placeholder_text="Nama")
entry_nama.grid(row=0, column=0, padx=10)

entry_nbi = ctk.CTkEntry(frame, placeholder_text="NBI")
entry_nbi.grid(row=0, column=1, padx=10)

entry_kelas = ctk.CTkEntry(frame, placeholder_text="Kelas")
entry_kelas.grid(row=0, column=2, padx=10)

ctk.CTkButton(frame, text="Tambah", command=tambah).grid(row=0, column=3, padx=10)
ctk.CTkButton(frame, text="Update", command=update).grid(row=0, column=4, padx=10)
ctk.CTkButton(frame, text="Hapus", command=hapus).grid(row=0, column=5, padx=10)

# ==========================
# SEARCH
# ==========================
search_entry = ctk.CTkEntry(app, placeholder_text="Cari Nama / NBI...")
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", search)

# ==========================
# TABLE
# ==========================
columns = ("Nama", "NBI", "Kelas")
tree = ttk.Treeview(app, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", pilih)

# LOAD DATA
refresh()

app.mainloop()