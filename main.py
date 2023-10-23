import os, time, pwinput, json
from prettytable import PrettyTable

from Admin import crud as admin

def clear():
    os.system('cls')
    time.sleep(1)

def load_data():
    try:
        with open("dataset/LoginData.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        raise SystemExit

def login():
    pengguna = load_data()
    
    while True:
        print("="*30)
        print("1. Login admin")
        print("2. Login Pelanggan")
        print("3. Registrasi")
        print("="*30)
        
        masukkan = input("Masukkan input: ")
        
        if masukkan == "1":
            username_or_email = input("Masukkan username atau email: ")
            password = pwinput.pwinput(prompt="Masukkan password: ")

            if (pengguna["admin"]["username"] == username_or_email or
                pengguna["admin"]["email"] == username_or_email) and pengguna["admin"]["password"] == password:
                print("Login sukses.")
                admin.create_data()
                break
            else:
                print("Login gagal. Silakan coba lagi.")

        elif masukkan == "2":
            username_or_email = input("Masukkan username atau email: ")
            password = pwinput.pwinput(prompt="Masukkan password: ")

            for pelanggan in pengguna["pelanggan"]:
                if (pelanggan["username"] == username_or_email or pelanggan["email"] == username_or_email) and pelanggan["password"] == password:
                    print("Login sukses.")

                    membership_choice = input("Apakah Anda memiliki membership? (ya/tidak): ")

                    if membership_choice.lower() == "ya":
                        if "membership_id" in pelanggan:
                            membership_id = input("Masukkan membership ID Anda: ")
                            if membership_id == pelanggan["membership_id"]:
                                print("Login sukses sebagai pelanggan dengan membership.")
                                clear()
                            else:
                                print("Membership ID salah. Silakan coba lagi.")
                                clear()
                        else:
                            print("Anda tidak memiliki membership. Silakan coba lagi.")
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
                    pengguna_baru = {
                        "username": username,
                        "email": email,
                        "password": password,
                        "membership_id": membership_id
                    }
                else:
                    pengguna_baru = {
                        "username": username,
                        "email": email,
                        "password": password
                    }
                pengguna["pelanggan"].append(pengguna_baru)
                with open("LoginData.json", "w") as file:
                    json.dump(pengguna, file, indent=4)
                print("Registrasi sukses!")

#Keluar dari menu registrasi
                keluar = input("Ingin keluar? (ya/tidak): ")
                if keluar.lower() == "ya":
                    clear()
                    break

if __name__ == "__main__":
    try: login()
    except Exception as e: print(e) 
    except KeyboardInterrupt: print("KeyBoard  Interrupt")