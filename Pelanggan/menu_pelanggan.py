import json
from prettytable import PrettyTable


import json
from prettytable import PrettyTable

def load_data_from_json(Daftar_paket):
    with open(Daftar_paket, 'r') as file:
        data = json.load(file)
    return data

def save_data_to_json(Daftar_paket, data):
    with open(Daftar_paket, 'w') as file:
        json.dump(data, file, indent=4)

def lihat_daftar_paket():
    daftar_paket = load_data_from_json('Daftar_paket.json')

    table = PrettyTable()
    table.field_names = ["Nomor", "Deskripsi", "Jenis", "Akses", "Harga", "Stok"]

    for paket in daftar_paket:
        table.add_row([paket["Nomor"], paket["Deskripsi"], paket["jenis"], paket["akses"], paket["Harga"], paket["stock"]])

    print(table)

def beli_paket(member):
    daftar_paket = load_data_from_json('daftar_paket.json')

    paket_dibeli = input("Masukkan nomor paket yang ingin dibeli: ")

    for paket in daftar_paket:
        if paket["Nomor"] == int(paket_dibeli):
            if (member == "platinum" or member == "gold") and (paket["jenis"] == "Platinum" or paket["jenis"] == "Gold"):
                if int(paket["stock"]) > 0:
                    paket["stock"] = str(int(paket["stock"]) - 1)
                    save_data_to_json('daftar_paket.json', daftar_paket)
                    print("Paket berhasil dibeli!")
                else:
                    print("Maaf, stok paket habis.")
            elif member == "reguler":
                if paket["jenis"] == "Reguler":
                    if int(paket["stock"]) > 0:
                        paket["stock"] = str(int(paket["stock"]) - 1)
                        save_data_to_json('daftar_paket.json', daftar_paket)
                        print("Paket berhasil dibeli!")
                    else:
                        print("Maaf, stok paket habis.")
                else:
                    print("Anda hanya dapat mengakses paket reguler.")
            else:
                print("Anda tidak memiliki akses ke paket ini.")
            break
    else:
        print("Nomor paket tidak valid.")


def top_up_saldo():
    jumlah_topup = input("Masukkan jumlah top up saldo: ")

    # Logika untuk menambahkan saldo ke E-money
    

    print("Saldo berhasil ditambahkan!")

def daftar_membership():
    membership = input("Pilih jenis membership (platinum/gold): ")

    # Logika untuk mendaftarkan pelanggan sebagai member platinum atau gold
    

    print("Pendaftaran berhasil!")

# Fungsi utama untuk menjalankan menu
def main_menu():
    while True:
        print("=== Menu Pelanggan ===")
        print("1. Lihat Daftar Paket")
        print("2. Beli Paket")
        print("3. Top Up Saldo E-money")
        print("4. Daftar Menjadi Member")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0-4): ")

        if pilihan == "1":
            lihat_daftar_paket()
        elif pilihan == "2":
            member = input("Apakah Anda member platinum/gold? (platinum/gold): ")
            beli_paket(member)
        elif pilihan == "3":
            top_up_saldo()
        elif pilihan == "4":
            daftar_membership()
        elif pilihan == "0":
            print("Terima kasih! Sampai jumpa lagi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan menu
main_menu()

def create_invoice(data_kamar):
    selected_kamar = int(input("Masukkan nomor kamar yang ingin disewa: "))
    
    if 1 <= selected_kamar <= len(data_kamar["kamar"]):
        kamar = data_kamar["kamar"][selected_kamar - 1]
        
        print("Invoice Pembayaran:")
        print("Nomor Kamar:", kamar["nomor"])
        print("Tipe Kamar:", kamar["tipe"])
        print("Spesifikasi PC:", kamar["spekPC"])
        
        # Harga berdasarkan tipe kamar (contoh: VVIP 500.000, VIP 400.000, Umum 300.000)
        if kamar["tipe"] == "VVIP":
            harga = 500000
        elif kamar["tipe"] == "VIP":
            harga = 400000
        else:
            harga = 300000
        
        # Diskon jika memiliki akses membership
        if kamar["akses"] == "Membership":
            diskon = 10  # Diskon 10%
            harga -= (harga * diskon / 100)
        
        print("Harga (Setelah Diskon):", harga)
    else:
        print("Nomor kamar tidak valid.")

# Contoh penggunaan fungsi
data_kamar = load_data()
pelanggan = input("Masukkan jenis pelanggan (membership/umum): ")
data_kamar = akses_kamar_pelanggan(pelanggan, data_kamar)
list_kamar(data_kamar)
create_invoice(data_kamar)
pilihan_pembayaran()

