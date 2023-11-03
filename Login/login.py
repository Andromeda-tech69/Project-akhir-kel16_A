import os, time, pwinput, json
import re
from colorama import Fore, Back, Style, init

# Inisialisasi Colorama
init(autoreset=True)


init(autoreset=True)

"""

    ROOT_DIR untuk mengatur path dari folder paling awal agar path dinamis dan menghindari error

"""
ROOT_DIR = os.path.abspath(os.curdir)


def is_valid_email(email):
    # Pola regex untuk memeriksa alamat email
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Fungsi untuk login
def login(username_or_email, password):
    data = load_data()
    global session
    for user in data["pelanggan"]:
        if (user["username"] == username_or_email or user["email"] == username_or_email) and user["password"] == password:
            session = user
            print("Login berhasil sebagai pelanggan.")
            import Pelanggan.menu_pelanggan as Pelanggan
            Pelanggan.menu_pelanggan(session)
            return

    if (data["admin"]["username"] == username_or_email or data["admin"]["email"] == username_or_email) and data["admin"]["password"] == password:
        session = data["admin"]
        print("Login berhasil sebagai admin.")
    else:
        print("Login gagal. Periksa kembali username/email dan password.")


# Fungsi untuk registrasi
def register(username, email, password):
    data = load_data()
    Usernames = [pelanggan['username'] for pelanggan in data['pelanggan']]
    emails = [pelanggan['email'] for pelanggan in data['pelanggan']]
        
    if username in Usernames:
        print(f"Username '{username}' sudah ada. Silakan pilih username lain.")
        return False
    elif email in emails:
        print(f"Email '{email}' sudah terdaftar. Gunakan email lain.")
        return False
    else:
        new_user = {
            "username": username,
            "email": email,
            "password": password,
            "membership_id": False,
            "Saldo E-money": 0
        }
        data["pelanggan"].append(new_user)
        with open(f"{ROOT_DIR}/dataset/LoginData.json", 'w') as file:
            json.dump(data, file, indent=4)
        print("Registrasi berhasil.")


def is_valid_membership_id(membership_id):
    # Mengecek apakah membership_id memenuhi semua ketentuan
    pattern = re.compile(r"^(A|S)[A-Z0-9]{5}$")
    return bool(pattern.match(membership_id))


def clear():
    os.system("cls")
    time.sleep(1)


def load_data():
    try:
        with open(f"{ROOT_DIR}/dataset/LoginData.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path login.")
        raise SystemExit


def main():
    try:
        admin_login_attempts = 0
        customer_login_attempts = 0
        max_attempts = 3

        while True:
            print(Fore.YELLOW + "=" * 30)
            print(Fore.MAGENTA + "👑 1. Login Admin")
            print(Fore.CYAN + "🛒 2. Login Pelanggan")
            print(Fore.GREEN + "📋 3. Registrasi")
            print(Fore.RED + "🚪 4. Exit")
            print(Fore.YELLOW + "=" * 30)

            masukkan = input(Fore.WHITE + "Masukkan input: ").strip()

            pengguna = load_data()
            if masukkan == "1":
                while admin_login_attempts < max_attempts:
                    username_or_email = input("Masukkan username atau email: ")
                    password = pwinput.pwinput(prompt="Masukkan password: ")
                    if (
                        pengguna["admin"]["username"] == username_or_email
                        or pengguna["admin"]["email"] == username_or_email
                    ) and pengguna["admin"]["password"] == password:
                        print("Login sukses.")
                        admin_login_attempts = 0  # Reset login attempts
                        clear()
                        import Admin.crud as admin
                        admin.menu()
                        break
                    else:
                        admin_login_attempts += 1
                        print(f"Login gagal. Sisa percobaan: {max_attempts - admin_login_attempts}")
                        clear()
                else:
                    print("Batas maksimum percobaan login admin tercapai.")
                    raise SystemExit

            elif masukkan == "2":
                while customer_login_attempts < max_attempts:
                    username_or_email = input("Masukkan username atau email: ")
                    password = pwinput.pwinput(prompt="Masukkan password: ")
                    if login(username_or_email, password):
                        customer_login_attempts = 0  # Reset login attempts
                        break
                    else:
                        customer_login_attempts += 1
                        print(f"Login gagal. Sisa percobaan: {max_attempts - customer_login_attempts}")
                else:
                    print("Batas maksimum percobaan login pelanggan tercapai.")
                    raise SystemExit

            elif masukkan == "3":
                while True:
                    username = input("Masukkan username: ")
                    email = input("Masukkan email: ")
                    password = pwinput.pwinput(prompt="Masukkan password: ")

                    # Memeriksa apakah alamat email valid
                    if not (username.strip() == "" or email.strip() == "" or password.strip() == ""):
                        if is_valid_email(email):
                            register(username, email, password)
                            clear()
                            break
                        else:
                            print("Alamat email tidak valid. Silakan coba lagi.")
                    else: print("input tidak boleh kosong.")
            elif masukkan =="4":
                print(Fore.YELLOW + "#"*40)
                print(Fore.CYAN + "Terima kasih, sampai jumpa kembali.")
                print(Fore.YELLOW + "#"*40)
                raise SystemExit
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

