import os, json, time, random, string
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# Path Awal
ROOT_DIR = os.path.abspath(os.curdir)

def clear():
    os.system('cls')
    time.sleep(1)

# Membaca data dari file JSON
def load_data():
    try:
        with open(f"{ROOT_DIR}/dataset/LoginData.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Menyimpan data ke file JSON
def save_data(data):
    with open(f"{ROOT_DIR}/dataset/LoginData.json", "w") as file:
        json.dump(data, file, indent=4)

# Fungsi pemberian ID unik pada pelanggan dengan limit 6 digit
def generate_unique_membership_id(prefix):
    # Membuat membership_id unik dengan format AXXXXXX (Platinum) atau SXXXXXX (Gold)
    unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return prefix + unique_id

# Fungsi menu pelanggan
def menu_pelanggan():
    data = load_data()
    if data is None:
        return
    pelanggan = data.get("pelanggan", {})
    
    while True:
        print(Fore.MAGENTA + "\n== 🛒 Menu Pelanggan 🛒 ==")
        print(Fore.CYAN + "1. 📦 Lihat daftar paket")
        print(Fore.GREEN + "2. 🛍️ Beli paket")
        print(Fore.BLUE + "3. 💰 Top up saldo e-money")
        print(Fore.RED + "4. 📋 Daftar sebagai anggota")
        print(Fore.MAGENTA + "5. 🚪 Keluar")
        pilihan = input(Fore.WHITE + "👉 Masukkan pilihan (1-5): ")

        if pilihan == "1":
            pelanggan = load_data()

            if pelanggan is not None:
                if pilihan == "1":
                    # Menampilkan daftar paket yang tersedia
                    for paket in pelanggan.get("Daftar_paket", []):  # Mengakses "Daftar_paket" dalam pelanggan
                        print("\nDaftar Paket yang Tersedia:")
                        if "akses" in paket and "stock" in paket:
                            if pelanggan.get("membership_id") and int(paket.get("stock", 0)) > 0:
                                print(f"Nomor: {paket.get('Nomor', '')}")
                                print(f"Deskripsi: {paket.get('Deskripsi', '')}")
                                print(f"Jenis: {paket.get('jenis', '')}")
                                print(f"Harga: {paket.get('Harga', '')}")
                                print(f"Stok: {paket.get('stock', '')}\n")
        elif pilihan == "2":
            customer_access = pelanggan["akses"]
            # Memproses pembelian paket
            nomor_paket = int(input("Masukkan nomor paket yang ingin Anda beli: "))
            for paket in daftar_paket:
                if paket["Nomor"] == nomor_paket:
                    if customer_access == "Plat_member":
                        if paket["stock"] > 0 and pelanggan["saldo_e_money"] >= int(paket["Harga"].replace("Rp. ", "").replace(".", "")):
                            print("Paket berhasil dibeli.")
                            pelanggan["saldo_e_money"] -= int(paket["Harga"].replace("Rp. ", "").replace(".", ""))
                            paket["stock"] -= 1
                        else:
                            print("Saldo e-money Anda tidak mencukupi atau paket tidak tersedia.")
                    elif customer_access == "Gold_member":
                        if paket["akses"] == "Plat_member":
                            print("Anda adalah Gold_member, Anda tidak bisa membeli paket Plat_member.")
                        else:
                            if paket["stock"] > 0 and pelanggan["saldo_e_money"] >= int(paket["Harga"].replace("Rp. ", "").replace(".", "")):
                                print("Paket berhasil dibeli.")
                                pelanggan["saldo_e_money"] -= int(paket["Harga"].replace("Rp. ", "").replace(".", ""))
                                paket["stock"] -= 1
                            else:
                                print("Saldo e-money Anda tidak mencukupi atau paket tidak tersedia.")
                    elif customer_access == "Reguler":
                        if paket["akses"] == "Plat_member" or paket["akses"] == "Gold_member":
                            print("Anda adalah Reguler, Anda tidak bisa membeli paket Plat_member atau Gold_member.")
                        else:
                            if paket["stock"] == "Tidak terbatas" or (paket["stock"] > 0 and pelanggan["saldo_e_money"] >= int(paket["Harga"].replace("Rp. ", "").replace(".", ""))):
                                print("Paket berhasil dibeli.")
                                if paket["stock"] != "Tidak terbatas":
                                    pelanggan["saldo_e_money"] -= int(paket["Harga"].replace("Rp. ", "").replace(".", ""))
                                    paket["stock"] -= 1
                            else:
                                print("Saldo e-money Anda tidak mencukupi atau paket tidak tersedia.")
        
        elif pilihan == "3":
            # Melakukan top up saldo e-money
            jumlah_topup = int(input("Masukkan jumlah top up saldo e-money (minimal 30.000, maksimal 500.000): "))
            if 30000 <= jumlah_topup <= 500000:
                pelanggan["saldo_e_money"] += jumlah_topup
                print(f"Saldo e-money Anda sekarang: Rp. {pelanggan['saldo_e_money']}")
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
                    pelanggan["membership_id"] = generate_unique_membership_id(prefix)
                    pelanggan["saldo_e_money"] -= biaya_daftar
                    print("Anda telah menjadi anggota.")
                    print(f"Membership ID Anda: {pelanggan['membership_id']}")

                    # Menyimpan data setelah perubahan
                    save_data(data)
                else:
                    print("Saldo e-money Anda tidak mencukupi untuk mendaftar sebagai anggota.")
            else:
                print("Anda sudah menjadi anggota atau belum login.")

        elif pilihan == "5":
            print("Terima kasih! Sampai jumpa.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    menu_pelanggan()
