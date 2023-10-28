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


# Fungsi pemberian ID unik pada pelanggan dengan limit 6 digit
def generate_unique_membership_id(prefix):
    # Membuat membership_id unik dengan format AXXXXXX (Platinum) atau SXXXXXX (Gold)
    unique_id = "".join(random.choices(
        string.ascii_uppercase + string.digits, k=6))
    return prefix + unique_id

<<<<<<< HEAD
def daftar_paket(data):
    table = PrettyTable()
    table.field_names = list(data['Daftar_paket'][0].keys())

    for paket in data['Daftar_paket']:
        table.add_row(list(paket.values()))

    print(table)

# Fungsi menu pelanggan
def menu_pelanggan(user_role):
    data = load_data()
=======

def show_available_packages(Daftar_paket, membership_id):
    if "Daftar_paket" in Daftar_paket:
        data = Daftar_paket["Daftar_paket"]
        if data:
            table = PrettyTable()
            table.field_names = [
                "Nomor", "Deskripsi", "Jenis", "Harga", "Stok"]

            for paket in data:
                if "akses" in paket and "stock" in paket:
                    if paket["akses"] == membership_id and (
                        paket["stock"] == "Tidak terbatas" or int(
                            paket["stock"]) > 0
                    ):
                        table.add_row(
                            [
                                paket.get("Nomor", ""),
                                paket.get("Deskripsi", ""),
                                paket.get("jenis", ""),
                                paket.get("Harga", ""),
                                paket.get("stock", ""),
                            ]
                        )

            print(table)
        else:
            print("Tidak ada data 'Daftar_paket' dalam file JSON.")
    else:
        print("Tidak ada data 'Daftar_paket' dalam file JSON.")


# Fungsi menu pelanggan
def menu_pelanggan():
    data = load_data()  # Memuat data pelanggan
>>>>>>> 70d450b8aad1e0ae4ff975d8db1a29a42a2ad7f2
    if data is None:
        return

    Daftar_paket = load()  # Memuat data Daftar_paket
    if Daftar_paket is None:
        return

    while True:
        print(Fore.MAGENTA + "\n== 🛒 Menu Pelanggan 🛒 ==")
        print(Fore.CYAN + "1. 📦 Lihat daftar paket")
        print(Fore.GREEN + "2. 🛍️ Beli paket")
        print(Fore.BLUE + "3. 💰 Top up saldo e-money")
        print(Fore.RED + "4. 📋 Daftar sebagai anggota")
        print(Fore.MAGENTA + "5. 🚪 Keluar")
        pilihan = input(Fore.WHITE + "👉 Masukkan pilihan (1-5): ")

        if pilihan == "1":
<<<<<<< HEAD
            daftar_paket(data)
=======
            membership_id = data.get("membership_id", "")
            show_available_packages(Daftar_paket, membership_id)
>>>>>>> 70d450b8aad1e0ae4ff975d8db1a29a42a2ad7f2
        elif pilihan == "2":
            Daftar_paket = (
                load()
            )  # Menginisialisasi variabel Daftar_paket dengan data dari file JSON
            if Daftar_paket is None:
                return
                while True:
                    # Memproses pembelian paket
                    nomor_paket = int(
                        input("Masukkan nomor paket yang ingin Anda beli: ")
                    )

                    # Gunakan loop untuk mencari paket yang sesuai
                    selected_package = None
                    for paket in Daftar_paket:
                        if paket["Nomor"] == nomor_paket:
                            selected_package = paket
                            break  # Keluar dari loop setelah menemukan paket yang sesuai

                if selected_package:
                    customer_access = selected_package["akses"]
                    if customer_access == "Plat_member":
                        if int(selected_package["stock"]) > 0 and pelanggan[
                            "saldo_e_money"
                        ] >= int(
                            selected_package["Harga"]
                            .replace("Rp. ", "")
                            .replace(".", "")
                        ):
                            print("Paket berhasil dibeli.")
                            pelanggan["saldo_e_money"] -= int(
                                selected_package["Harga"]
                                .replace("Rp. ", "")
                                .replace(".", "")
                            )
                            selected_package["stock"] = str(
                                int(selected_package["stock"]) - 1
                            )  # Kurangi stok
                        else:
                            print(
                                "Saldo e-money Anda tidak mencukupi atau paket tidak tersedia."
                            )
                    elif customer_access == "Gold_member":
                        if selected_package["akses"] == "Plat_member":
                            print(
                                "Anda adalah Gold_member, Anda tidak bisa membeli paket Plat_member."
                            )
                        else:
                            if int(selected_package["stock"]) > 0 and pelanggan[
                                "saldo_e_money"
                            ] >= int(
                                selected_package["Harga"]
                                .replace("Rp. ", "")
                                .replace(".", "")
                            ):
                                print("Paket berhasil dibeli.")
                                pelanggan["saldo_e_money"] -= int(
                                    selected_package["Harga"]
                                    .replace("Rp. ", "")
                                    .replace(".", "")
                                )
                                selected_package["stock"] = str(
                                    int(selected_package["stock"]) - 1
                                )  # Kurangi stok
                            else:
                                print(
                                    "Saldo e-money Anda tidak mencukupi atau paket tidak tersedia."
                                )
                    elif customer_access == "Reguler":
                        if (
                            selected_package["akses"] == "Plat_member"
                            or selected_package["akses"] == "Gold_member"
                        ):
                            print(
                                "Anda adalah Reguler, Anda tidak bisa membeli paket Plat_member atau Gold_member."
                            )
                        else:
                            if (
                                selected_package["stock"] == "Tidak terbatas"
                                or (int(selected_package["stock"])) > 0
                                and pelanggan["saldo_e_money"]
                                >= int(
                                    selected_package["Harga"]
                                    .replace("Rp. ", "")
                                    .replace(".", "")
                                )
                            ):
                                print("Paket berhasil dibeli.")
                                if selected_package["stock"] != "Tidak terbatas":
                                    pelanggan["saldo_e_money"] -= int(
                                        selected_package["Harga"]
                                        .replace("Rp. ", "")
                                        .replace(".", "")
                                    )
                                    selected_package["stock"] = str(
                                        int(selected_package["stock"]) - 1
                                    )  # Kurangi stok
                            else:
                                print(
                                    "Saldo e-money Anda tidak mencukupi atau paket tidak tersedia."
                                )
                else:
                    print("Nomor paket tidak valid. Silakan coba lagi.")

        elif pilihan == "3":
            # Melakukan top up saldo e-money
            jumlah_topup = int(
                input(
                    "Masukkan jumlah top up saldo e-money (minimal 30.000, maksimal 500.000): "
                )
            )
            if 30000 <= jumlah_topup <= 500000:
                pelanggan["saldo_e_money"] += jumlah_topup
                print(
                    f"Saldo e-money Anda sekarang: Rp. {pelanggan['saldo_e_money']}")
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


if __name__ == "__main__":
    menu_pelanggan()
