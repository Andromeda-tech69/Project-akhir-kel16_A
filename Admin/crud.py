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
        data = {"kamar_pc": []}
    return data

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    try:
        with open(f"{ROOT_DIR}/dataset/data.json", "w") as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError: print("File Not Found")
        
def read_data(data):
    kamar_pc = data["kamar_pc"]

    if not kamar_pc:
        print("Tidak ada data 'kamar_pc' dalam file JSON.")
        return

    table = PrettyTable()
    
    # Mengambil nama kolom dari kunci (keys) JSON pertama
    field_names = kamar_pc[0].keys()
    table.field_names = field_names

    for entry in kamar_pc:
        table.add_row([entry.get(key, "") for key in field_names])

    print(table)

# Fungsi untuk menambahkan data baru
def create_data(data):
    new_entry = {
        "nomor_kamar": len(data["kamar_pc"]) + 1,
        "jenis": input("Masukkan jenis kamar: "),
        "akses": input("Masukkan akses kamar: "),
        "spek_pc": input("Masukkan spesifikasi PC: "),
    }

    data["kamar_pc"].append(new_entry)
    save_data(data)
    print("Data berhasil ditambahkan.")


# Fungsi untuk mengubah data
def update_data(data):
    read_data(data)
    while True:
        try:
            nomor_kamar = int(input("Masukkan nomor kamar yang ingin diubah: "))
            break
        except:print("Masukan Dengan Benar")
    for entry in data["kamar_pc"]:
        if entry["nomor_kamar"] == nomor_kamar:
            entry["jenis"] = input("Masukkan jenis kamar baru: ")
            entry["akses"] = input("Masukkan akses kamar baru: ")
            entry["spek_pc"] = input("Masukkan spesifikasi PC baru: ")
            save_data(data)
            print("Data berhasil diubah.")
            return
    print("Nomor kamar tidak ditemukan.")

# Fungsi untuk menghapus data
def delete_data(data):
    read_data(data)
    while True:
        try:
            nomor_kamar = int(input("Masukkan nomor kamar yang ingin dihapus: "))
            break
        except: print("Masukan Dengan Benar")
    for entry in data["kamar_pc"]:
        if entry["nomor_kamar"] == nomor_kamar:
            data["kamar_pc"].remove(entry)
            save_data(data)
            print(f"Data nomor kamar {nomor_kamar} berhasil dihapus.")
            return
    print("Nomor kamar tidak ditemukan.")

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
            create_data(data)
        elif pilihan == '2':
            read_data(data)
        elif pilihan == '3':
            update_data(data)
        elif pilihan == '4':
            delete_data(data)
        elif pilihan == '5':
            main.clear()
            main.main()
            break
        else:
            print("Menu tidak valid. Silakan pilih menu yang benar.")

menu()