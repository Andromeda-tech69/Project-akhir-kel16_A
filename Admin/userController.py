import json, os
from colorama import Fore, Back, Style, init
from prettytable import PrettyTable

# Path Awal
ROOT_DIR = os.path.abspath(os.curdir)

# Membaca data dari Logindata.json
with open(f"{ROOT_DIR}/dataset/Logindata.json", "r") as file:
    data = json.load(file)


def save_data():
    # Menyimpan data kembali ke Logindata.json
    with open(f"{ROOT_DIR}/dataset/Logindata.json", "w") as file:
        json.dump(data, file, indent=4)


def delete_user(username):
    if username == "admin":
        print("Tidak dapat menghapus akun admin.")
        return
    if "pelanggan" in data:
        users = data["pelanggan"]
        for user in users:
            if user["username"] == username:
                users.remove(user)
                save_data()
                print(f"Akun '{username}' telah dihapus.")
                return
    print(f"Akun '{username}' tidak ditemukan.")


def sort_users(ascending=True):
    if "pelanggan" in data:
        data["pelanggan"] = sorted(
            data["pelanggan"], key=lambda x: x["username"], reverse=not ascending
        )
        save_data()
        order = "ascending" if ascending else "descending"
        print(f"Akun pelanggan telah diurutkan {order} berdasarkan nama pengguna.")
    display_users()


def search_user(username):
    if "pelanggan" in data:
        for user in data["pelanggan"]:
            if user["username"] == username:
                return user
<<<<<<< HEAD
=======
    else:
        print("User %s not found")
>>>>>>> 0550a476cd8c9003dfbef035c64a7b65e1c12202
    return None


# Menampilkan daftar akun pelanggan dengan PrettyTable
def display_users():
    if "pelanggan" in data:
        table = PrettyTable()
        if data["pelanggan"]:
            table.field_names = data["pelanggan"][
                0
            ].keys()  # Ambil keys dari entri pertama dalam list pelanggan
            for user in data["pelanggan"]:
                table.add_row(user.values())
            print(table)
        else:
            print("Tidak ada data pelanggan.")


def control_menu():
    while True:
        try:
            print("\n🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟")
            print("🐍   Menu Manage User   🐍")
            print("🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟🌈🌟")

            print(Fore.LIGHTBLUE_EX+ "\n📋 Menu:")
            print(Fore.RED+ "1. 🗑️ Hapus Akun")
            print(Fore.LIGHTCYAN_EX+ "2. 🔢 Urutkan Akun (Ascending)")
            print(Fore.LIGHTGREEN_EX+ "3. 🔣 Urutkan Akun (Descending)")
            print(Fore.YELLOW+ "4. 🔍 Cari Akun")
            print(Fore.GREEN+ "5. 📄 Tampilkan Akun Pelanggan")
            print(Fore.LIGHTRED_EX+ "6. 🚪 Keluar")
            
            choice = input("🚀 Pilih Menu: ")


            if choice == "1":
                username = input("Masukkan username akun yang ingin dihapus: ")
                delete_user(username)
            elif choice == "2":
                sort_users(ascending=True)
            elif choice == "3":
                sort_users(ascending=False)
            elif choice == "4":
                username = input("Masukkan username akun yang ingin dicari: ")
                user = search_user(username)
                if user:
                    print(f"Akun ditemukan: Username: {user['username']},\nEmail: {user['email']},\nMembership ID: {user['membership_id']}")
                else:
                    print(f"Akun '{username}' tidak ditemukan.")
            elif choice == "5":
                display_users()
            elif choice == "6":
                print("Kembali Ke Crud Admin")
                break
            else:
                print("Pilihan tidak valid.")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            continue
