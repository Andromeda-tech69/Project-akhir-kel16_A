import os, json, time, sys, re
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
from datetime import datetime

# Inisialisasi Colorama
init(autoreset=True)

# Path Awal
ROOT_DIR = os.path.abspath(os.curdir)


def clear():
    os.system("cls")
    time.sleep(1)

# Fungsi untuk membaca data file data.json
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
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("File Not Found")


# Membaca data login dari file JSON
def loadLogin():
    try:
        with open(f"{ROOT_DIR}/dataset/LoginData.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    
def save_Login(data):
    try:
        with open(f"{ROOT_DIR}/dataset/LoginData.json", "w") as file:
            json.dump(data,file,indent=4)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def daftar_paket(data):
    if data['Daftar_paket']:
        table = PrettyTable()
        table.field_names = list(data['Daftar_paket'][0].keys())
        for item in data['Daftar_paket']:
            item["membership"] = "Member" if item["membership"] else "Reguler"
        for paket in data['Daftar_paket']:
            table.add_row(list(paket.values()))

        print(table)
    else:print('Data Kosong')

def top_up(username):
    while True:
        try:
            saldo = int(input("Masukkan jumlah saldo yang ingin ditambahkan (minimal 30.000, maksimal 500.000): "))
            if 30000 <= saldo <= 500000:
                break
            else:
                print("Saldo harus antara 30.000 dan 500.000.")
        except ValueError:
            print("Masukkan harus berupa angka atau integer.")

    login_data = loadLogin()

    for user in login_data['pelanggan']:
        if user['username'] == username:
            current_balance = int(user.get('Saldo E-money', 0))
            user['Saldo E-money'] = current_balance + saldo
            print(f"Saldo E-money berhasil ditambahkan. Saldo sekarang: {user['Saldo E-money']}")

    save_Login(login_data)


# fungsi membeli barang dengan melakukan pencekan data apakah member atau bukan
def beli_barang(username,is_membership):
    data_barang = load()
    data_user = loadLogin()
    table = PrettyTable()
    table.field_names = ["Nomor", "Deskripsi", "Harga", "Stock"]
    for barang in data_barang['Daftar_paket']:
        if barang.get('membership', False) and (is_membership or not barang['membership']):
            table.add_row([barang['Nomor'], barang['Deskripsi'], barang['Harga'], barang['stock']])
        elif not barang.get('membership', False):
            table.add_row([barang['Nomor'], barang['Deskripsi'], barang['Harga'], barang['stock']])

    print("Daftar Barang yang Tersedia:")
    print(table)
    while True:
        try:
            nomor_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
            break
        except: 
            print("Masukan Dengan Benar")
            continue
    
    dicari = False
    for barang in data_barang['Daftar_paket']:
        if barang['Nomor'] == nomor_barang:
            dicari = True
            if (barang.get('membership', False) and (is_membership or not barang['membership'])) or not barang.get('membership', False):
                harga_barang = barang['Harga']
                stock_barang = barang['stock']

                # Periksa saldo pengguna
                saldo = 0
                for user in data_user['pelanggan']:
                    if user['username'] == username:
                        saldo = int(user.get('Saldo E-money', 0))
                        break

                if saldo >= harga_barang and stock_barang > 0:

                    for user in data_user['pelanggan']:
                        if user['username'] == username:
                            user['Saldo E-money'] = int(user['Saldo E-money']) - harga_barang
                            break

                    # Update stok barang
                    for data in data_barang['Daftar_paket']:
                        if data['Nomor'] == nomor_barang:
                            data['stock'] -= 1
                            break
                    
                    #update saldo dan stock json setelah dibeli
                    save_data(data_barang)
                    save_Login(data_user)

                    time.sleep(1)
                    os.system('cls')
                    waktu = datetime.now()
                    print("Saldo mencukupi dan barang tersedia. Melakukan pembelian...")
                    print(f'''Invoice Date: {waktu}\n\nKepada : {username}\nAnda berhasil membeli {barang['Deskripsi']}.\nDengan Harga : {harga_barang}\nTerima kasih!''')
                    time.sleep(2)
                else:
                    if saldo < harga_barang:
                        print("Saldo tidak mencukupi untuk melakukan pembelian.")
                    if stock_barang <= 0:
                        print("Maaf, stok barang telah habis.")
                return
            else:
                print("Anda Bukan Member.")
                tanya = input("Apakah Anda Mau Jadi Member? : ya / tidak:").lower()
                if tanya == 'ya' or tanya =='y':
                    for user in data_user['pelanggan']:
                        if user['username'] == username:
                            user['membership_id'] = True
                            time.sleep(1)
                            print("Selamat Menjadi Member ",username)
                    save_Login(data_user)
                else:continue
    
    if not dicari:print("Nomor Barang Tidak Ada")
            
# Fungsi menu pelanggan
def menu_pelanggan(user_role):
    while True:
        try:
            data = load()
            userData = loadLogin()
            print(Fore.MAGENTA + "\n== 🛒 Menu Pelanggan 🛒 ==")
            print(Fore.CYAN + "1. 📦 Lihat daftar paket")
            print(Fore.GREEN + "2. 🛍️ Beli paket")
            print(Fore.BLUE + "3. 💰 Top up saldo e-money")
            print(Fore.MAGENTA + "4. 🚪 Logout")
            pilihan = input(Fore.WHITE + "👉 Masukkan pilihan (1-5): ")

            if pilihan == "1":
                daftar_paket(data)
            elif pilihan == "2":
                daftar_paket(data)
                is_membership = False
                for user in userData['pelanggan']:
                    if user['username'] == user_role['username']:
                        is_membership = user.get('membership_id', False)
                        break
                if is_membership:
                    print("Anda adalah member.")
                else:
                    print("Anda bukan member.")
                beli_barang(user_role['username'],is_membership)
            elif pilihan == "3":
                top_up(user_role['username'])
            elif pilihan == "4":
                print("Terima kasih! Sampai jumpa.")
                sys.exit()
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
                break
        except KeyboardInterrupt:
            print("\n" + Fore.YELLOW + "⚠ KeyboardInterrupt")
            continue