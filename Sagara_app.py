'''
=================================================
Graded Challenge 1

Nama  : Sagara Biru Wilantara Manggala
Batch : HCK-007

Program ini merupakan program shopping cart yang memungkinkan user untuk menambah, menghapus, dan melihat barang di keranjang belanja
=================================================
'''

class CartItem:     #Class CartItem berisikan data dengan atribut nama dan harga

  def __init__(self, nama, harga): #Metode ini berfungsi untuk mendeklarasikan atribut nama dan harga
    self.nama = nama
    self.harga = harga

class Shoppingcart:   #Class ShoppingCart berisikan data berupa berbagai macam fitur untuk menjalankan sistem
  
  def __init__(self):   #Metode ini berfungsi untuk menyimpan data yang ditambahkan dalam bentuk list 
    self.items = []     #self.items merupakan list yang menampung semua data yang ditambahkan pada fungsi add_data

  def add_data(self, nama, harga):    #Metode ini berfungsi untuk menambahkan data ke dalam keranjang yang nantinya disimpan di self.items 
    item = CartItem(nama, harga)     #Mendeklarasikan item sebagai CartItem yang berisikan data berupa nama dan harga
    self.items.append(item)         #Menyimpan hasil penambahan barang pada list pada self.items

  def remove_data(self, nama_barang):   #Metode ini berfungsi untuk menghapus data yang sebelumnya sudah ditambahkan
    for nama in self.items:           
        for item in self.items:
            if item.nama == nama_barang:  #Ketika input dari nama_barang yang dicari menyerupai dengan yang ada pada keranjang, maka barang akan dihapus
                self.items.remove(item)
                return True
        return False
  
  def view_data(self):    #Metode ini berfungsi untuk melihat list berupa daftar belanja dalam keranjang
    for i in range(len(self.items)):
      print(f'{i+1}  {self.items[i].nama} - {self.items[i].harga}')   #Menampilkan data pada self.items

  def cal_total(self):            #Metode ini berfungsi untuk menghitung total harga dari semua barang yang ada di keranjang. 
        total = 0
        for item in self.items:
            total += item.harga     #Disini akan menjumlahkan setiap harga yang ada pada setiap barang di keranjang
        return total

  def run(self):                #Metode ini berfungsi untuk menjalankan user interface
    print('Selamat Datang di Keranjang Belanja Toko Makmur!')     #Kalimat ini akan muncul setiap program dijalankan pertama kali
    while True:                     #While True digunakan untuk membuat looping pada menu utama
      print('\nMenu')                 #Menu utama dimunculkan ketika program dijalankan dan saat proses looping
      print('1. Menambah Barang')
      print('2. Hapus Barang')
      print('3. Tampilkan Barang di Keranjang')
      print('4. Lihat Total Belanja')
      print('5. Exit\n')
      menu = (input('Pilihan: '))         #Input yang diisi oleh user untuk memilih proses yang ingin dilakukan
      if menu == '1':                           #Ketika user menginput angka 1 maka akan dilakukan proses penambahan barang
        nama = input('Masukan nama barang: ')     #User menginput nama barang yang ingin dimasukkan ke dalam keranjang
        harga = int(input('Masukan harga: '))      #User menginput harga dari barang yang sebelumnya dimasukkan dalam bentuk angka
        self.add_data(nama, harga)                  #Fungsi yang sebelumnya sudah dibuat yaitu add_data akan dijalankan
        print(f'Barang "{nama}" berhasil dimasukkan ke keranjang.')       #Pemberitahuan bahwa barang berhasil dimasukkan ke dalam keranjang

      elif menu == '2':                     #Ketika user menginput angka 2 maka akan dilakukan proses penghapusan barang
        hapus_barang = input('Masukan nama barang yang ingin dihapus: ')          #User menginput nama barang yang ingin dihapus dari keranjang
        if self.remove_data(hapus_barang):                                      #Fungsi yang sebelumnya sudah dibuat yaitu remove_data akan dijalankan
            print(f'"{hapus_barang}" telah dihapus dari keranjang belanja.')      #Apabila nama barang sama dengan yang ada pada keranjang maka barang dihapus akan muncul kalimat tersebut
        else:
            print(f"'{hapus_barang}' tidak ditemukan di dalam keranjang belanja.")    #Apabila nama barang tidak sama dengan yang ada pada keranjang maka akan muncul kalimat tersebut

      elif menu == '3':                    #Ketika user menginput angka 3 maka akan memperlihatkan isi dari keranjang
        print('Barang di Keranjang: ')        
        self.view_data()                    #Fungsi yang sebelumnya sudah dibuat yaitu view_data akan dijalankan

      elif menu == '4':                   #Ketika user menginput angka 4 maka akan dilakukan proses kalkulasi dari seluruh isi keranjang
        print(f'Total belanja: {self.cal_total()}')         #Fungsi yang sebelumnya sudah dibuat yaitu cal_total akan dijalankan dan hasilnya akan muncul

      elif menu == '5':                   #Ketika user menginput angka 5 maka looping akan berhenti dan proses selesai
        print("Terima kasih sudah berbelanja!")     
        break

      else:
        print('Pilihannya salah. Coba lagi ya.')      #Ketika user menginput angka maupun string selain 1-5 maka akan muncul kalimat disamping dan kembali ke menu utama 




if __name__ == "__main__":            #Syntax untuk menjalankan aplikasi
    a = Shoppingcart()          
    a.run()                 #Menjalankan fungsi run terlebih dahulu