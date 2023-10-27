import os, time, pwinput, json
import re
from colorama import Fore, Back, Style, init

# Inisialisasi Colorama
init(autoreset=True)


init(autoreset=True)


def is_valid_membership_id(membership_id):
    # Mengecek apakah membership_id memenuhi semua ketentuan
    pattern = re.compile(r"^(A|S)[A-Z0-9]{5}$")
    return bool(pattern.match(membership_id))


def clear():
    os.system("cls")
    time.sleep(1)


def load_data():
    """

    ROOT_DIR untuk mengatur path dari folder paling awal agar path dinamis dan menghindari error

    """
    ROOT_DIR = os.path.abspath(os.curdir)
    try:
        with open(f"{ROOT_DIR}/dataset/LoginData.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path login.")
        raise SystemExit


def main():
    while True:
        print(Fore.YELLOW + "=" * 30)
        print(Fore.MAGENTA + "👑 1. Login Admin")
        print(Fore.CYAN + "🛒 2. Login Pelanggan")
        print(Fore.GREEN + "📋 3. Registrasi")
        print(Fore.RED + "🚪 4. Exit")
        print(Fore.YELLOW + "=" * 30)

        masukkan = input(Fore.WHITE + "Masukkan input: ")

        if masukkan == "1":
            pengguna = load_data()
            while True:
                username_or_email = input("Masukkan username atau email: ")
                password = pwinput.pwinput(prompt="Masukkan password: ")

                if (
                    pengguna["admin"]["username"] == username_or_email
                    or pengguna["admin"]["email"] == username_or_email
                ) and pengguna["admin"]["password"] == password:
                    print("Login sukses.")
                    clear()
                    import Admin.crud as admin

                    admin.menu()

                    break
                else:
                    clear()
                    print("Login gagal. Silakan coba lagi.")

        elif masukkan == "2":
            pengguna = load_data()
            while True:
                username_or_email = input("Masukkan username atau email: ")
                password = pwinput.pwinput(prompt="Masukkan password: ")

                for pelanggan in pengguna["pelanggan"]:
                    if (
                        pelanggan["username"] == username_or_email
                        or pelanggan["email"] == username_or_email
                    ) and pelanggan["password"] == password:
                        print("Login sukses.")

                        membership_choice = input(
                            "Apakah Anda memiliki membership? (ya/tidak): "
                        )

                        if membership_choice.lower() == "ya":
                            if "membership_id" in pelanggan:
                                membership_id = input("Masukkan membership ID Anda: ")
                                if membership_id == pelanggan["membership_id"]:
                                    print(
                                        "Login sukses sebagai pelanggan dengan membership."
                                    )
                                    import Pelanggan.menu_pelanggan as pelanggan

                                    pelanggan.menu_pelanggan()
                                    clear()
                                else:
                                    print("Membership ID salah. Silakan coba lagi.")
                                    clear()
                            else:
                                print(
                                    "Anda tidak memiliki membership. Silakan coba lagi."
                                )
                                clear()
                        break
                else:
                    print("Login gagal. Silakan coba lagi.")
                    clear()

        elif masukkan == "3":
            pengguna = load_data()
            while True:
                username = input("Masukkan username: ")
                email = input("Masukkan email: ")
                password = pwinput.pwinput(prompt="Masukkan password: ")
                is_member = input("Apakah anda member? (ya/tidak): ")
                if is_member.lower() == "ya":
                    membership_id = input("Masukkan membership ID: ")
                    if is_valid_membership_id(membership_id):
                        break
                    else:
                        print(
                            "Membership ID tidak valid. Pastikan ID memiliki 6 digit."
                        )
                    pengguna_baru = {
                        "username": username,
                        "email": email,
                        "password": password,
                        "membership_id": membership_id,
                    }
                else:
                    pengguna_baru = {
                        "username": username,
                        "email": email,
                        "password": password,
                    }
                pengguna["pelanggan"].append(pengguna_baru)
                with open("LoginData.json", "w") as file:
                    json.dump(pengguna, file, indent=4)
                print("Registrasi sukses!")

                # Keluar dari menu registrasi
                keluar = input("Ingin keluar? (ya/tidak): ")
                if keluar.lower() == "ya":
                    clear()
                    break

        elif masukkan == "4":
            raise SystemExit
