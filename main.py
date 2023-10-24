import subprocess,importlib,os,time

# Daftar library yang diperlukan
required_libraries = ['pwinput', 'prettytable']

# Periksa dan instal library yang belum terpasang
print('Checking library')
time.sleep(2)
for lib in required_libraries:
    try:
        importlib.import_module(lib)
        print(f"Library {lib} sudah terinstal.")
    except ImportError:
        print(f"Library {lib} belum terinstal. Menginstal...")
        subprocess.check_call(['pip', 'install', lib])
        for i in range(3, 0, -1):
                time.sleep(1)
                print("Installing Library")
        print(f"Library {lib} telah diinstal.")

import Login.login as login

if __name__ == "__main__":
    while True:
        try:
            login.main()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            os.system('cls')
            print("\nKeyboard Interrupt")
            for i in range(3, 0, -1):
                time.sleep(1)
                print("Auto Logout In", i)
            continue