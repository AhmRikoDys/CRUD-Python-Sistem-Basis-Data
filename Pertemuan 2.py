data_mahasiswa = []

# ==========================
# TAMBAH DATA
# ==========================
def tambah_data():
    print("\nA) MASUKAN DATA MAHASISWA")
    print("------------------------------------")
    
    nama = input("1. MASUKAN NAMA  : ").strip()
    nbi = input("2. MASUKAN NBI   : ").strip()
    kelas = input("3. MASUKAN KELAS : ").strip()

    # Validasi NBI unik
    for mhs in data_mahasiswa:
        if mhs["nbi"] == nbi:
            print("❌ NBI sudah digunakan!")
            return

    data = {
        "nama": nama,
        "nbi": nbi,
        "kelas": kelas
    }

    data_mahasiswa.append(data)
    print("✅ Data berhasil ditambahkan!")


# ==========================
# TAMPILKAN DATA
# ==========================
def tampilkan_data():
    print("\nB) TAMPILKAN KESELURUHAN DATA")
    print("------------------------------------")

    if not data_mahasiswa:
        print("⚠️ Data masih kosong!")
        return

    print(f"{'No':<5}{'Nama':<20}{'NBI':<15}{'Kelas':<10}")
    print("-" * 50)

    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"{i:<5}{mhs['nama']:<20}{mhs['nbi']:<15}{mhs['kelas']:<10}")


# ==========================
# CARI DATA (FLEKSIBEL)
# ==========================
def cari_data():
    print("\nB) CARI DATA MAHASISWA")
    print("------------------------------------")
    
    keyword = input("Masukkan Nama / NBI : ").lower()

    hasil = []

    for mhs in data_mahasiswa:
        if keyword in mhs["nama"].lower() or keyword in mhs["nbi"]:
            hasil.append(mhs)

    if hasil:
        print("\n🔍 HASIL PENCARIAN:")
        for mhs in hasil:
            print(f"Nama: {mhs['nama']}, NBI: {mhs['nbi']}, Kelas: {mhs['kelas']}")
    else:
        print("❌ Data tidak ditemukan!")


# ==========================
# UBAH DATA (FULL UPDATE)
# ==========================
def ubah_data():
    print("\nC) RUBAH DATA MAHASISWA")
    print("------------------------------------")
    
    nbi_lama = input("Masukan NBI yang ingin diubah: ")

    for mhs in data_mahasiswa:
        if mhs["nbi"] == nbi_lama:
            print("Data ditemukan! Silakan isi data baru:")
            
            nama_baru = input("Nama baru   : ")
            nbi_baru = input("NBI baru    : ")
            kelas_baru = input("Kelas baru  : ")

            mhs["nama"] = nama_baru or mhs["nama"]
            mhs["nbi"] = nbi_baru or mhs["nbi"]
            mhs["kelas"] = kelas_baru or mhs["kelas"]

            print("✅ Data berhasil diperbarui!")
            return

    print("❌ Data tidak ditemukan!")


# ==========================
# HAPUS DATA
# ==========================
def hapus_data():
    print("\nD) HAPUS DATA MAHASISWA")
    print("------------------------------------")
    
    nbi = input("Masukan NBI yang akan dihapus: ")

    for mhs in data_mahasiswa:
        if mhs["nbi"] == nbi:
            konfirmasi = input("Yakin ingin hapus? (y/n): ").lower()
            
            if konfirmasi == "y":
                data_mahasiswa.remove(mhs)
                print("🗑️ Data berhasil dihapus!")
            else:
                print("❌ Penghapusan dibatalkan!")
            return

    print("❌ Data tidak ditemukan!")


# ==========================
# MENU UTAMA
# ==========================
def menu():
    while True:
        print("\n==== SIAKAD UNTAG ====")
        print("A) MASUKAN DATA MAHASISWA")
        print("B) TAMPILKAN DATA")
        print("C) RUBAH DATA")
        print("D) HAPUS DATA")
        print("E) KELUAR")

        pilihan = input("Pilih menu: ").upper()

        if pilihan == "A":
            tambah_data()
        elif pilihan == "B":
            tampilkan_data()
            cari_data()
        elif pilihan == "C":
            ubah_data()
        elif pilihan == "D":
            hapus_data()
        elif pilihan == "E":
            print("\n---- TERIMA KASIH ----")
            break
        else:
            print("❌ Pilihan tidak valid!")


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    menu()