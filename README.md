# *Tema : PEMBELIAN TIKET KERETA API*

Akan melakukan simulasi pembuatan Tiket Kereta Api dengan menggunakan sistem CRUD dalam rangka belajar, melatih, dan mengembangkan ilmu yang telah dipelajari dalam sebuah mini project
1. Alasan memilih tema Tiket Kereta Api adalah karena, dalam sistem pembelian tiket cukup komplex dimana proses pengolahan data akan dibagi menjadi 2 bagian, yakni data yang diolah oleh ADMIN server 
   dan data yang akan diinput oleh pelanggan/customer dalam melakukan pembelian tiket kereta,
2. Akses data yang dibatasi antara Admin dan Customer menjadi salah satu tantangan dalam melakukan pembuatan mini project,
3. Selain data, menu interface antara Admin dan Customer sudah pasti berbeda hal ini juga menjadi tantangan dalam hal pembuatan menu interface, sehingga pada mini project ini akan membuat 2 menu
   yakni menu admin dan juga menu customer,
4. Setiap kereta memiliki nomor kereta yang unik dan harus berbeda dari 1 kereta dengan kereta lainnya, hal ini juga menambah tantangan dalam hal pembuatan data kereta baru.


Fitur :
Dalam pembuatan mini project pembelian tiket Kereta Api kali ini, saya membuat beberapa fitur yang dibagi menjadi 2 segmen diantaranya:
Admin
   1. Login pegawai,
   2. Menu menampilkan data kereta (READ) yang bisa di akses dengan berbagai cara yakni:
        - Menampilkan bedasarkan No_kereta
        - Menampilkan bedasarkan Kode_kereta
        - Menampilkan bedasarkan Rute_kereta
   3. Menu Penambahan data kereta (CREATE),
   4. Menu Pengubahan data kereta (UPDATE),
   5. Menu Penghapusan data kereta (DELETE) yang bisa di akses dengan berbagai cara yakni:
        - Menghapus data bedasarkan Kode_kereta dan Rute_perjalanan,
        - Menghapus data bedasarkan No_kereta
   6. Menu menampilkan data Pelunasan Tiket Kereta (READ).

Customer
   1. Isi Identitas (Data yang diisi akan digunakan pada fitur CREATE),
   2. Menu menampilkan jadawl kereta (READ) yang bisa di akses dengan berbagai cara yakni:
        - Menampilkan bedasarkan No_kereta
        - Menampilkan bedasarkan Kode_kereta
        - Menampilkan bedasarkan Rute_kereta
   3. Menu Pemesanan tiket kereta (CREATE),
   4. Menu Pengubahan Tiket kereta (UPDATE),
   5. Menu Penghapusan Tiket kereta (DELETE),
   6. Menu menampilkan data Pelunasan Tiket Kereta (READ).


Adapun beberapa flow chart yang terdapat pada menu pembelian tiket kereta adalah sebagai berikut:
Flow Diagram Menu Customer
Flow Diagram 1
![image](https://github.com/user-attachments/assets/1a87cc5e-e399-4f28-8233-3fd0f84311be)
Flow Diagram 2
![image](https://github.com/user-attachments/assets/6b68952a-4e7c-4618-bbcc-81840154ef27)
Flow Diagram 3
![image](https://github.com/user-attachments/assets/7b6d1806-0e70-4ea3-b122-7f4c47ae9ba1)


Sekian saya tutup dalam pengenalan dan penjelasan mengenai mini project yang saya kerjakan, adapaun beberapa Notes dalam mengakses file mini project diantaranya:
-- Admin
   1. User = 'admin'
   2. Password = 'admin1234'

TERIMAKASIH


    
