import tkinter as tk
from tkinter import ttk, messagebox

data_mahasiswa = []

# ==========================
# TAMBAH DATA
# ==========================
def tambah_data():
    nama = entry_nama.get()
    nbi = entry_nbi.get()
    kelas = entry_kelas.get()

    if not nama or not nbi or not kelas:
        messagebox.showwarning("Warning", "Semua field harus diisi!")
        return

    for mhs in data_mahasiswa:
        if mhs["nbi"] == nbi:
            messagebox.showerror("Error", "NBI sudah ada!")
            return

    data_mahasiswa.append({
        "nama": nama,
        "nbi": nbi,
        "kelas": kelas
    })

    tampilkan_data()
    clear_input()
    messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")

# ==========================
# TAMPILKAN DATA
# ==========================
def tampilkan_data():
    for row in tree.get_children():
        tree.delete(row)

    for mhs in data_mahasiswa:
        tree.insert("", "end", values=(mhs["nama"], mhs["nbi"], mhs["kelas"]))

# ==========================
# PILIH DATA DARI TABEL
# ==========================
def pilih_data(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_nama.delete(0, tk.END)
        entry_nbi.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)

        entry_nama.insert(0, values[0])
        entry_nbi.insert(0, values[1])
        entry_kelas.insert(0, values[2])

# ==========================
# UBAH DATA
# ==========================
def ubah_data():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Pilih data dulu!")
        return

    values = tree.item(selected, "values")

    for mhs in data_mahasiswa:
        if mhs["nbi"] == values[1]:
            mhs["nama"] = entry_nama.get()
            mhs["nbi"] = entry_nbi.get()
            mhs["kelas"] = entry_kelas.get()
            break

    tampilkan_data()
    clear_input()
    messagebox.showinfo("Sukses", "Data berhasil diubah!")

# ==========================
# HAPUS DATA
# ==========================
def hapus_data():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Pilih data dulu!")
        return

    values = tree.item(selected, "values")

    for mhs in data_mahasiswa:
        if mhs["nbi"] == values[1]:
            data_mahasiswa.remove(mhs)
            break

    tampilkan_data()
    clear_input()
    messagebox.showinfo("Sukses", "Data berhasil dihapus!")

# ==========================
# CLEAR INPUT
# ==========================
def clear_input():
    entry_nama.delete(0, tk.END)
    entry_nbi.delete(0, tk.END)
    entry_kelas.delete(0, tk.END)

# ==========================
# GUI SETUP
# ==========================
root = tk.Tk()
root.title("SIAKAD UNTAG")
root.geometry("600x400")

# LABEL & INPUT
tk.Label(root, text="Nama").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

tk.Label(root, text="NBI").pack()
entry_nbi = tk.Entry(root)
entry_nbi.pack()

tk.Label(root, text="Kelas").pack()
entry_kelas = tk.Entry(root)
entry_kelas.pack()

# BUTTON
tk.Button(root, text="Tambah", command=tambah_data).pack(pady=5)
tk.Button(root, text="Ubah", command=ubah_data).pack(pady=5)
tk.Button(root, text="Hapus", command=hapus_data).pack(pady=5)

# TABLE
columns = ("Nama", "NBI", "Kelas")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)

tree.bind("<<TreeviewSelect>>", pilih_data)

# RUN
root.mainloop()