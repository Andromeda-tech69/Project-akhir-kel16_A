import json,os

ROOT_DIR = os.path.abspath(os.curdir)

# Fungsi untuk membaca data dari file JSON
def load_data():
    try:
        with open(f"{ROOT_DIR}/dataset/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"kamar_pc": []}
    return data

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    try:
        with open(f"{ROOT_DIR}/dataset/data.json", "w") as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError: print("File Not Found")
        
# Fungsi untuk menambahkan data baru
def create_data(data):
    new_entry = {
        "nomor_kamar": len(data["kamar_pc"]) + 1,
        "jenis": input("Masukkan jenis kamar: "),
        "akses": input("Masukkan akses kamar: "),
        "spek_pc": input("Masukkan spesifikasi PC: "),
    }

    data["kamar_pc"].append(new_entry)
    save_data(data)
    print("Data berhasil ditambahkan.")

# Fungsi untuk membaca data
def read_data(data):
    kamar_pc = data["kamar_pc"]
    for entry in kamar_pc:
        print(f"Nomor Kamar: {entry['nomor_kamar']}")
        print(f"Jenis: {entry['jenis']}")
        print(f"Akses: {entry['akses']}")
        print(f"Spesifikasi PC: {entry['spek_pc']}")
        print()

# Fungsi untuk mengubah data
def update_data(data):
    read_data(data)
    nomor_kamar = int(input("Masukkan nomor kamar yang ingin diubah: "))
    for entry in data["kamar_pc"]:
        if entry["nomor_kamar"] == nomor_kamar:
            entry["jenis"] = input("Masukkan jenis kamar baru: ")
            entry["akses"] = input("Masukkan akses kamar baru: ")
            entry["spek_pc"] = input("Masukkan spesifikasi PC baru: ")
            save_data(data)
            print("Data berhasil diubah.")
            return
    print("Nomor kamar tidak ditemukan.")

# Fungsi untuk menghapus data
def delete_data(data):
    read_data(data)
    nomor_kamar = int(input("Masukkan nomor kamar yang ingin dihapus: "))
    for entry in data["kamar_pc"]:
        if entry["nomor_kamar"] == nomor_kamar:
            data["kamar_pc"].remove(entry)
            save_data(data)
            print(f"Data nomor kamar {nomor_kamar} berhasil dihapus.")
            return
    print("Nomor kamar tidak ditemukan.")

# Program utama
data = load_data()

while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Baca Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")

    choice = input("Pilih menu: ")

    if choice == '1':
        create_data(data)
    elif choice == '2':
        read_data(data)
    elif choice == '3':
        update_data(data)
    elif choice == '4':
        delete_data(data)
    elif choice == '5':
        break
    else:
        print("Menu tidak valid. Silakan pilih menu yang benar.")
