data_mahasiswa = []

def tambah_data():
    print("\nA) MASUKAN DATA MAHASISWA")
    print("------------------------------------")
    nama = input("1. MASUKAN NAMA  : ")
    nbi = input("2. MASUKAN NBI   : ")
    kelas = input("3. MASUKAN KELAS : ")

    data = {
        "nama": nama,
        "nbi": nbi,
        "kelas": kelas
    }

    data_mahasiswa.append(data)
    print("✅ Data berhasil ditambahkan!")

def tampilkan_data():
    print("\nB) TAMPILKAN KESELURUHAN DATA")
    print("------------------------------------")

    if len(data_mahasiswa) == 0:
        print("⚠️ Data masih kosong!")
    else:
        for i, mhs in enumerate(data_mahasiswa, start=1):
            print(f"{i}. Nama: {mhs['nama']}, NBI: {mhs['nbi']}, Kelas: {mhs['kelas']}")

def cari_data():
    print("\nB) CARI DATA MAHASISWA")
    print("------------------------------------")
    nama = input("1. CARI NAMA : ")
    nbi = input("2. CARI NBI  : ")

    ditemukan = False

    for mhs in data_mahasiswa:
        if (nama and mhs["nama"] == nama) or (nbi and mhs["nbi"] == nbi):
            print(f"✔️ Ditemukan -> Nama: {mhs['nama']}, NBI: {mhs['nbi']}, Kelas: {mhs['kelas']}")
            ditemukan = True

    if not ditemukan:
        print("❌ Data tidak ditemukan!")

def ubah_data():
    print("\nC) RUBAH DATA MAHASISWA")
    print("------------------------------------")
    nbi_lama = input("1. MASUKAN NBI LAMA : ")
    nbi_baru = input("2. MASUKAN NBI BARU : ")

    ditemukan = False

    for mhs in data_mahasiswa:
        if mhs["nbi"] == nbi_lama:
            mhs["nbi"] = nbi_baru
            print("✅ Data berhasil diubah!")
            ditemukan = True
            break

    if not ditemukan:
        print("❌ Data tidak ditemukan!")

def hapus_data():
    print("\nD) HAPUS DATA MAHASISWA")
    print("------------------------------------")
    nbi = input("1. NBI YANG AKAN DI HAPUS : ")

    for mhs in data_mahasiswa:
        if mhs["nbi"] == nbi:
            data_mahasiswa.remove(mhs)
            print("🗑️ Data berhasil dihapus!")
            return

    print("❌ Data tidak ditemukan!")

def menu():
    while True:
        print("\n---- SELAMAT DATANG DI SIAKAD UNTAG ----")
        print("A) MASUKAN DATA MAHASISWA")
        print("B) TAMPILKAN KESELURUHAN DATA")
        print("C) RUBAH DATA MAHASISWA")
        print("D) HAPUS DATA MAHASISWA")
        print("E) KELUAR")

        pilihan = input("Pilih menu (A/B/C/D/E): ").upper()

        if pilihan == "A":
            tambah_data()
        elif pilihan == "B":
            tampilkan_data()
            cari_data()   # sesuai format kamu (ada fitur cari)
        elif pilihan == "C":
            ubah_data()
        elif pilihan == "D":
            hapus_data()
        elif pilihan == "E":
            print("\n-----------------------------------")
            print("---- TERIMA KASIH ----")
            break
        else:
            print("❌ Pilihan tidak valid!")

# Jalankan program
menu()