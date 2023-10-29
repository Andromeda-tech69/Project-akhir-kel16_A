import os, json, time, random, string
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# Path Awal
ROOT_DIR = os.path.abspath(os.curdir)


def clear():
    os.system("cls")
    time.sleep(1)


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


# Membaca data dari file JSON
def load_data():
    try:
        with open(f"{ROOT_DIR}/dataset/data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None


# Menyimpan data ke file JSON
def save_data(data):
    with open(f"{ROOT_DIR}/dataset/data.json", "w") as file:
        json.dump(data, file, indent=4)

def daftar_paket(data):
    if data['Daftar_paket']:
        table = PrettyTable()
        table.field_names = list(data['Daftar_paket'][0].keys())

        for paket in data['Daftar_paket']:
            table.add_row(list(paket.values()))

        print(table)
    else:print('Data Kosong')

# Fungsi menu pelanggan
def menu_pelanggan(user_role):
    data = load_data()
    
    while True:
        print(Fore.MAGENTA + "\n== 🛒 Menu Pelanggan 🛒 ==")
        print(Fore.CYAN + "1. 📦 Lihat daftar paket")
        print(Fore.GREEN + "2. 🛍️ Beli paket")
        print(Fore.BLUE + "3. 💰 Top up saldo e-money")
        print(Fore.RED + "4. 📋 Daftar sebagai anggota")
        print(Fore.MAGENTA + "5. 🚪 Keluar")
        pilihan = input(Fore.WHITE + "👉 Masukkan pilihan (1-5): ")

        if pilihan == "1":
            daftar_paket(data)
        elif pilihan == "2":
            daftar_paket(data)
            pilih = int(input("Masukan Pilihan : "))
            for i in data['Daftar_paket']:
                if i['Nomor'] == pilih:
                    print(i['Deskripsi'])
        elif pilihan == "3":
            user = user_role
            # Melakukan top up saldo e-money
            jumlah_topup = int(
                input(
                    "Masukkan jumlah top up saldo e-money (MIN 30.000, MAX 500.000): "
                )
            )
            if 30000 <= jumlah_topup <= 500000:
                user["saldo_e_money"] += jumlah_topup
                print(
                    f"Saldo e-money Anda sekarang: Rp. {user['saldo_e_money']}")
            else:
                print("Jumlah top up tidak valid. Minimal 30.000, maksimal 500.000.")
        elif pilihan == "4":
            # Mendaftar sebagai anggota
            if "membership_id" in pelanggan and pelanggan["membership_id"] == "":
                print("Pilih Jenis Keanggotaan:")
                print("1. Platinum")
                print("2. Gold")
                jenis_anggota = input("Masukkan angka 1 atau 2: ")

                if jenis_anggota == "1":
                    prefix = "A"  # Platinum
                    biaya_daftar = 200000
                elif jenis_anggota == "2":
                    prefix = "S"  # Gold
                    biaya_daftar = 100000
                else:
                    print("Pilihan jenis anggota tidak valid.")
                    continue

                if pelanggan["saldo_e_money"] >= biaya_daftar:
                    pelanggan["membership_id"] = generate_unique_membership_id(
                        prefix)
                    pelanggan["saldo_e_money"] -= biaya_daftar
                    print("Anda telah menjadi anggota.")
                    print(f"Membership ID Anda: {pelanggan['membership_id']}")

                    # Menyimpan data setelah perubahan
                    save_data(data)
                else:
                    print(
                        "Saldo e-money Anda tidak mencukupi untuk mendaftar sebagai anggota."
                    )
            else:
                print("Anda sudah menjadi anggota atau belum login.")

        elif pilihan == "5":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

