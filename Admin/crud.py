import json

# Fungsi untuk membaca data dari file
def load_data():
    try:
        with open("../dataset/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Fungsi untuk menyimpan data ke file
def save_data(data):
    try:
        with open("../dataset/data.json", "w") as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        raise SystemExit

# Fungsi untuk menambahkan data baru
def create_data(data):
    new_entry = {
        "nama": input("Masukkan nama: "),
        "umur": input("Masukkan umur: "),
    }

    data.append(new_entry)
    save_data(data)
    print("Data berhasil ditambahkan.")

# Fungsi untuk membaca data
def read_data(data):
    for i, entry in enumerate(data):
        print(f"Data ke-{i + 1}:")
        print(f"Nama: {entry['nama']}")
        print(f"Umur: {entry['umur']}")
        print()

# Fungsi untuk mengubah data
def update_data(data):
    read_data(data)
    index = int(input("Masukkan nomor data yang ingin diubah: ") - 1)
    if 0 <= index < len(data):
        data[index]["nama"] = input("Masukkan nama baru: ")
        data[index]["umur"] = input("Masukkan umur baru: ")
        save_data(data)
        print("Data berhasil diubah.")
    else:
        print("Nomor data tidak valid.")

# Fungsi untuk menghapus data
def delete_data(data):
    read_data(data)
    index = int(input("Masukkan nomor data yang ingin dihapus: ") - 1)
    if 0 <= index < len(data):
        deleted_entry = data.pop(index)
        save_data(data)
        print("Data berikut berhasil dihapus:")
        print(f"Nama: {deleted_entry['nama']}")
        print(f"Umur: {deleted_entry['umur']}")
    else:
        print("Nomor data tidak valid.")

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
