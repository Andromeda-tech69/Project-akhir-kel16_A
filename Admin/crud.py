import json,os

from prettytable import PrettyTable

# Path Awal
ROOT_DIR = os.path.abspath(os.curdir)

import main

# Fungsi untuk membaca data dari file JSON

def load():
    try:
        with open(f"{ROOT_DIR}/dataset/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"Daftar_paket": []}
    return data

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    try:
        with open(f"{ROOT_DIR}/dataset/data.json", "w") as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError: print("File Not Found")
        
def read_data(data):
    Daftar_paket = data["Daftar_paket"]

    if not Daftar_paket:
        print("Tidak ada data 'Daftar_paket' dalam file JSON.")
        return

    table = PrettyTable()
    
    # Mengambil nama kolom dari kunci (keys) JSON pertama
    field_names = Daftar_paket[0].keys()
    table.field_names = field_names

    for entry in Daftar_paket:
        table.add_row([entry.get(key, "") for key in field_names])

    print(table)

# Fungsi untuk menambahkan data baru
def create_data(data):
    data_baru = {
        "Deskripsi": len(data["Daftar_paket"]) + 1,
        "jenis": input("Masukkan jenis: "),
        "akses": input("Masukkan akses: "),
        "Harga": input("Masukkan harga: "),
        "Stock": input("Masukkan jumblah stok :"),
    }

    data["Daftar_paket"].append(data_baru)
    save_data(data)
    print("Data berhasil ditambahkan.")


# Fungsi untuk mengubah data
def update_data(data):
    read_data(data)
    while True:
        try:
            Daftar_paket = int(input("Masukkan nomor paket yang ingin diubah: "))
            break
        except:print("Masukan Dengan Benar")
    for entry in data["Daftar_paket"]:
        if entry["nomor"] == nomor:
            while True:
                entry["jenis"] = input("Masukkan jenis kamar baru: ").lower()
                entry["akses"] = input("Masukkan akses kamar baru: ").lower()
                entry["spek_pc"] = input("Masukkan spesifikasi PC baru: ").lower()
                entry["status"] = input("Masukkan status baru: ").lower()
                if entry["status"] == "ready" or entry["status"] == "booked":
                    save_data(data)
                    print("Data berhasil diubah.")
                    return False
                else:print("status hanya 'ready' dan 'booked'")
    print("Nomor kamar tidak ditemukan.")

# Fungsi untuk menghapus data
def delete_data(data):
    read_data(data)
    while True:
        try:
            nomor = int(input("Masukkan nomor paket yang ingin dihapus: "))
            break
        except: print("Masukan Dengan Benar")
    for entry in data["Daftar_paket"]:
        if entry["nomor"] == nomor:
            data["Daftar_paket"].remove(entry)
            save_data(data)
            print(f"Data nomor paket {nomor} berhasil dihapus.")
            return
    print("Nomor paket tidak ditemukan.")

def menu():
    # Program utama
    data = load()
    
    while True:
        print("Menu:")
        print("1. Tambah Data")
        print("2. Baca Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            main.clear()
            create_data(data)
        elif pilihan == '2':
            main.clear()
            read_data(data)
        elif pilihan == '3':
            main.clear()
            update_data(data)
        elif pilihan == '4':
            main.clear()
            delete_data(data)
        elif pilihan == '5':
            main.clear()
            main.main()
            break
        else:
            print("Menu tidak valid. Silakan pilih menu yang benar.")

menu()