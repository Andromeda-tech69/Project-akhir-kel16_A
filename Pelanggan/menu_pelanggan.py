import json
from prettytable import PrettyTable

def load_data():
    with open('data_kamar.json') as file:
        data_kamar = json.load(file)
    return data_kamar

def save_data(data_kamar):
    with open('data_kamar.json', 'w') as file:
        json.dump(data_kamar, file, indent=2)

def akses_kamar_pelanggan(pelanggan, data_kamar):
    if pelanggan == "membership":
        data_kamar["kamar"][0]["akses"] = "Membership"
        data_kamar["kamar"][1]["akses"] = "Membership"
        diskon = 10  # Contoh diskon 10%
        print("Selamat datang, Anda memiliki akses ke kamar VVIP dan VIP.")
        print(f"Anda mendapatkan diskon {diskon}% untuk penyewaan kamar.")
    else:
        print("Selamat datang, Anda memiliki akses ke kamar Umum.")
    return data_kamar

def list_kamar(data_kamar):
    table = PrettyTable()
    table.field_names = ["Nomor Kamar", "Tipe", "Akses", "Spesifikasi PC"]
    
    for kamar in data_kamar["kamar"]:
        table.add_row([kamar["nomor"], kamar["tipe"], kamar["akses"], kamar["spekPC"]])
    
    print(table)

def pilihan_pembayaran():
    print("Silakan pilih metode pembayaran:")
    print("1. Pembayaran offline")
    print("2. Booking secara online")
    metode = int(input("Pilihan (1/2): "))
    
    if metode == 1:
        print("Anda memilih pembayaran offline.")
    elif metode == 2:
        print("Anda memilih booking secara online.")
        print("Silakan pilih metode pembayaran:")
        print("1. Uang")
        print("2. E-money")
        metode_bayar = int(input("Pilihan (1/2): "))
        
        if metode_bayar == 1:
            print("Anda memilih pembayaran dengan uang.")
        elif metode_bayar == 2:
            print("Anda memilih pembayaran dengan E-money.")
        else:
            print("Pilihan metode pembayaran tidak valid.")
    else:
        print("Pilihan metode pembayaran tidak valid.")

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

