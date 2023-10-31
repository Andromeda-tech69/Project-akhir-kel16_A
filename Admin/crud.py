import json, os, time
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# Path Awal
ROOT_DIR = os.path.abspath(os.curdir)


def clear():
    os.system("cls")
    time.sleep(1)

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
    except FileNotFoundError:
        print("File Not Found")


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
    os.system("cls")
    while True:
        try:
            data_baru = {
                "Nomor": len(data["Daftar_paket"]) + 1,
                "Deskripsi": str(input("Masukkan Deskripsi: ")),
                "jenis": str(input("Masukkan jenis: ")),
                "membership": str(input("Masukkan Membership: ")),
                "Harga": int(input("Masukkan harga: ")),
                "stock": int(input("Masukkan jumblah stok :")),
            }
            break
        except:
            print("Masukan Dengan Benar")
            continue
    data["Daftar_paket"].append(data_baru)
    save_data(data)
    print("Data berhasil ditambahkan.")


# Fungsi untuk mengubah data
def update_data(data):
    read_data(data)
    while True:
        try:
            nomor = int(input("Masukkan nomor paket yang ingin diubah: "))
            break
        except:
            print("Masukan Dengan Benar")
    for entry in data["Daftar_paket"]:
        if entry["Nomor"] == nomor:
            while True:
                entry["Deskripsi"] = input("Masukkan Deskripsi baru: ").lower()
                entry["jenis"] = input("Masukkan jenis baru: ").lower()
                entry["akses"] = input("Masukkan akses baru: ").lower()
                while True:
                    try:
                        entry["Harga"] = int(input("Masukkan harga baru: "))
                        entry["stock"] = int(input("Masukkan stock baru: "))
                        break
                    except:
                        print("Masukkan Dengan Benar")
                save_data(data)
                print("Data berhasil diubah.")
                return
    print("Nomor kamar tidak ditemukan.")


# Fungsi untuk menghapus data
def delete_data(data):
    read_data(data)
    while True:
        try:
            nomor = int(input("Masukkan nomor paket yang ingin dihapus: "))
            break
        except:
            print("Masukan Dengan Benar")
    for entry in data["Daftar_paket"]:
        if entry["Nomor"] == nomor:
            data["Daftar_paket"].remove(entry)
            save_data(data)
            print(f"Data nomor paket {nomor} berhasil dihapus.")
            return
    print("Nomor paket tidak ditemukan.")


def menu():
    # Program utama
    data = load()

    while True:
        try:
            print(Fore.MAGENTA + "✨" * 20)
            print(Fore.CYAN + "🚀 Menu Admin:")
            print(Fore.YELLOW + "1. Tambah Data")
            print(Fore.GREEN + "2. Baca Data")
            print(Fore.BLUE + "3. Ubah Data")
            print(Fore.RED + "4. Hapus Data")
            print(Fore.MAGENTA + "5. Manage Akun")
            print(Fore.CYAN + "6. Keluar")

            pilihan = input(Fore.WHITE + "👉 Pilih menu: ")

            if pilihan == "1":
                clear()
                create_data(data)
            elif pilihan == "2":
                clear()
                read_data(data)
            elif pilihan == "3":
                clear()
                update_data(data)
            elif pilihan == "4":
                clear()
                delete_data(data)
            elif pilihan == "5":
                import Admin.userController as admin

                admin.control_menu()
                clear()
            elif pilihan == "6":
                clear()
                break
            else:
                print(Fore.RED + "❌ Menu tidak valid. Silakan pilih menu yang benar.")
        except KeyboardInterrupt:
            print("\n" + Fore.YELLOW + "⚠ KeyboardInterrupt")
            continue
