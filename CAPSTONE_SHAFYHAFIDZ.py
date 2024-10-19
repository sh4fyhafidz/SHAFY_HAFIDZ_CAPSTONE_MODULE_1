db_pegawai ={
    'rute_1' : {
        'no_kereta' : 'KA001',
        'kode_kereta' : 'LDY',
        'nama_kereta' : 'Lodaya',
        'jenis_kereta' : 'Premium',
        'rute_perjalanan' : 'BDG-JKT',
        'harga' : 110000,
        'waktu_keberangkatan' : '19.00',
        'tanggal_keberangkatan' : '12-01-2025'
    },
    'rute_2' : {
        'no_kereta' : 'KA002',
        'kode_kereta' : 'KTJ',
        'nama_kereta' : 'Kartajaya',
        'jenis_kereta' : 'Reguler',
        'rute_perjalanan' : 'JKT-SBY',
        'harga' : 190000,
        'waktu_keberangkatan' : '21.00',
        'tanggal_keberangkatan' : '14-01-2025'
    },
    'rute_3' : {
        'no_kereta' : 'KA003',
        'kode_kereta' : 'LDY',
        'nama_kereta' : 'Lodaya',
        'jenis_kereta' : 'Reguler',
        'rute_perjalanan' : 'BDG-BGR',
        'harga' : 70000,
        'waktu_keberangkatan' : '19.00',
        'tanggal_keberangkatan' : '12-01-2025'
    },
    'rute_4' : {
        'no_kereta' : 'KA004',
        'kode_kereta' : 'APR',
        'nama_kereta' : 'Argo Parahyangan',
        'jenis_kereta' : 'Premium',
        'rute_perjalanan' : 'JKT-BDG',
        'harga' : 120000,
        'waktu_keberangkatan' : '17.00',
        'tanggal_keberangkatan' : '29-01-2025'
    },
    'rute_5' : {
        'no_kereta' : 'KA005',
        'kode_kereta' : 'ALW',
        'nama_kereta' : 'Argo Lawu',
        'jenis_kereta' : 'Premium',
        'rute_perjalanan' : 'BDG-SOLO',
        'harga' : 210000,
        'waktu_keberangkatan' : '16.00',
        'tanggal_keberangkatan' : '09-01-2025'
     },

}

db_temp_pelanggan ={

}

db_pembayaran_customer ={

}

def menu_4():
    while True:
        print("\n SELAMAT DATANG DI WEB KERETA API INDONESIA")
        print("\n Berikut merupakan DASHBOARD pegawai Kerta Api Indonesia")
        print("="*80)
        print("[1] Show data kereta")
        print("[2] Tambah data Kereta")
        print("[3] Update data kereta")
        print("[4] Delete data kereta")
        print("[5] Data Pembayaran Customer")
        print("[6] Kembali ke menu utama")
        
        kode = input("Masukan pilihan anda : ")

        if kode == '1':
            print("Daftar Kereta Api Indonesia")
            print("="*120)
            print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
            print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
            print("-"*120)

            for i in db_pegawai:
                print(f"{db_pegawai[i]['no_kereta']:^5} "
                f"{db_pegawai[i]['kode_kereta']:^8} "
                f"{db_pegawai[i]['nama_kereta']:^25} "
                f"{db_pegawai[i]['jenis_kereta']:^12} "
                f"{db_pegawai[i]['rute_perjalanan']:^25} "
                f"{db_pegawai[i]['harga']:^12} "
                f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
            print("="*120)
            while True :
                print("[1] Tampilkan semua data kereta ")
                print("[2] Pencarian bedasarkan Kode Kereta ")
                print("[3] Pencarian bedasarkan Rute Kereta ")
                print("[4] Pencarian bedasarkan No Kereta ")
                print("[5] Back ke menu ")
                
                kode = input("Masukan pilihan anda : ")

                if kode == '1':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)

                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)

                elif kode == '2':

                    kode_kereta = input("Masukkan kode kereta yang ingin ditampilkan: ")
                    print("="*120)
                    print(f"{'No':^5}{'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    ketemu = False
                    for i in db_pegawai:
                        if db_pegawai[i]['kode_kereta'] == kode_kereta.upper():
                            print(f"{db_pegawai[i]['no_kereta']:^5} "
                            f"{db_pegawai[i]['kode_kereta']:^8} "
                            f"{db_pegawai[i]['nama_kereta']:^25} "
                            f"{db_pegawai[i]['jenis_kereta']:^12} "
                            f"{db_pegawai[i]['rute_perjalanan']:^25} "
                            f"{db_pegawai[i]['harga']:^12} "
                            f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                            f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                            ketemu = True
                    if not ketemu:
                        print(f"Tidak ada kereta dengan Kode {kode_kereta}")
                    print("-"*120)
                
                elif kode == '3':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)

                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)

                    rute_kereta = input("Masukkan rute kereta yang ingin ditampilkan: ")
                    print("="*120)
                    print(f"{'No':^5}{'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    ketemu = False
                    for i in db_pegawai:
                        if db_pegawai[i]['rute_perjalanan'] == rute_kereta.upper():
                            print(f"{db_pegawai[i]['no_kereta']:^5} "
                            f"{db_pegawai[i]['kode_kereta']:^8} "
                            f"{db_pegawai[i]['nama_kereta']:^25} "
                            f"{db_pegawai[i]['jenis_kereta']:^12} "
                            f"{db_pegawai[i]['rute_perjalanan']:^25} "
                            f"{db_pegawai[i]['harga']:^12} "
                            f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                            f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                            ketemu = True
                    if not ketemu:
                        print(f"Tidak ada kereta dengan Rute {rute_kereta}")
                    print("-"*120)
                
                elif kode == '4':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)

                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)

                    no_kereta = input("Masukkan Nomer kereta yang ingin ditampilkan: ")
                    print("="*120)
                    print(f"{'No':^5}{'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    ketemu = False
                    for i in db_pegawai:
                        if db_pegawai[i]['no_kereta'] == no_kereta.upper():
                            print(f"{db_pegawai[i]['no_kereta']:^5} "
                            f"{db_pegawai[i]['kode_kereta']:^8} "
                            f"{db_pegawai[i]['nama_kereta']:^25} "
                            f"{db_pegawai[i]['jenis_kereta']:^12} "
                            f"{db_pegawai[i]['rute_perjalanan']:^25} "
                            f"{db_pegawai[i]['harga']:^12} "
                            f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                            f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                            ketemu = True
                    if not ketemu:
                        print(f"Tidak ada kereta dengan Rute {no_kereta}")

                    print("-"*120)

                elif kode == '5':
                    return menu_4()
                else:
                    print("Input menu tidak tersedia, seilahkan input kembali")

        elif kode == '2':
            print("Daftar Kereta Api Indonesia")
            print("="*120)
            print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
            print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
            print("-"*120)

            for i in db_pegawai:
                print(f"{db_pegawai[i]['no_kereta']:^5} "
                f"{db_pegawai[i]['kode_kereta']:^8} "
                f"{db_pegawai[i]['nama_kereta']:^25} "
                f"{db_pegawai[i]['jenis_kereta']:^12} "
                f"{db_pegawai[i]['rute_perjalanan']:^25} "
                f"{db_pegawai[i]['harga']:^12} "
                f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
            print("="*120)

            while True:
                print("[1] Tampilkan seluruh data kereta ")
                print("[2] Tambahkan data kereta api ")
                print("[3] Back ke menu ")
                
                kode = input("Masukan pilihan anda : ")
                if kode == '1':

                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)

                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)

                elif kode == '2':

                    no_krt = input(" Masukan Nomor  kereta (format: KA00x): ")
                    kode_krt = input(" Masukan kode kereta (format: singkatan kereta 3 kode): ")
                    nama_krt = input(" Masukan nama kereta : ")
                    jenis_krt = input(" Masukan jenis kereta (format: ex/Premium-Reguler): ")
                    rute_pjn = input(" Masukan Rute perjalanan kereta (format : Keberangkatan - tujuan): ")
                    hrg = int(input(" Masukan harga tiket kereta : "))
                    wkt_kbt = input(" Masukan waktu keberangkatan kereta (format : ex/19.00) : ")
                    tgl_kbt = input(" Masukan tanggal keberankatan kereta (format : ex/12-01-2025) :")

                    new_rute = {
                        'no_kereta' : no_krt.upper(),
                        'kode_kereta' : kode_krt.upper(),
                        'nama_kereta' : nama_krt.capitalize(),
                        'jenis_kereta' : jenis_krt.capitalize(),
                        'rute_perjalanan' : rute_pjn.upper(),
                        'harga' : hrg,
                        'waktu_keberangkatan' : wkt_kbt,
                        'tanggal_keberangkatan' : tgl_kbt
                    }

                    new_rute_key = f"rute_{len(db_pegawai) + 1}"

                    existing_rute = any(
                        (rute['no_kereta'] == no_krt.upper()) or
                        (rute['kode_kereta'] == kode_krt.upper() and rute['rute_perjalanan'] == rute_pjn.upper())
                        for rute in db_pegawai.values()
                    )

                    if existing_rute:
                        if any(rute['no_kereta'] == no_krt.upper() for rute in db_pegawai.values()):
                            print("Nomor kereta sudah ada, silakan gunakan nomor kereta lain")
                        else:
                            print("Kode kereta dan rute perjalanan sudah ada, silakan gunakan kode kereta dan rute perjalanan lain")
                    else:
                        db_pegawai[new_rute_key] = new_rute
                        print("Data telah berhasil ditambahkan")
                
                elif kode == '3':
                    return menu_4()
                else:
                    print("Input menu tidak tersedia, seilahkan input kembali")
        
        elif kode == '3':
            print("Daftar Kereta Api Indonesia")
            print("="*120)
            print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
            print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
            print("-"*120)

            for i in db_pegawai:
                print(f"{db_pegawai[i]['no_kereta']:^5} "
                f"{db_pegawai[i]['kode_kereta']:^8} "
                f"{db_pegawai[i]['nama_kereta']:^25} "
                f"{db_pegawai[i]['jenis_kereta']:^12} "
                f"{db_pegawai[i]['rute_perjalanan']:^25} "
                f"{db_pegawai[i]['harga']:^12} "
                f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
            print("="*120)

            while True:
                print("[1] Tampilkan seluruh data kereta ")
                print("[2] Update data kereta api ")
                print("[3] Back ke menu ")
                
                kode = input("Masukan pilihan anda : ")
                if kode == '1':

                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)

                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)
                
                elif kode == '2':

                    kode_kereta = input("Masukan kode kereta yang ingin diupdate: ").upper()
                    rute_perjalanan = input("Masukan rute perjalanan kereta yang ingin diupdate: ").upper()

                    for i in db_pegawai:
                        if db_pegawai[i]['kode_kereta'] == kode_kereta and db_pegawai[i]['rute_perjalanan'] == rute_perjalanan:
                            updated_data = {
                                #'no_kereta' : input("Masukan no kereta baru (kosongkan jika tidak ingin mengubah): "),
                                'nama_kereta': input("Masukan nama kereta baru (kosongkan jika tidak ingin mengubah): "),
                                'jenis_kereta': input("Masukan jenis kereta baru (kosongkan jika tidak ingin mengubah): "),
                                'harga': int(input("Masukan harga baru (kosongkan jika tidak ingin mengubah): ")),
                                'waktu_keberangkatan': input("Masukan waktu keberangkatan baru (kosongkan jika tidak ingin mengubah): "),
                                'tanggal_keberangkatan': input("Masukan tanggal keberangkatan baru (kosongkan jika tidak ingin mengubah): ")
                            }
                            for key, value in updated_data.items():
                                if value:
                                    db_pegawai[i][key] = value
                            print("Data kereta berhasil diupdate ")
                            break
                    else:
                        print(f"Kode kereta {kode_kereta} dengan rute perjalanan {rute_perjalanan} tidak tersedia ")

                elif kode == '3':
                    return menu_4()
                else:
                    print("Pilihan menu tidak tersedia, silahkan pilih kembali")

                
        elif kode == '4':
            print("Daftar Kereta Api Indonesia")
            print("="*120)
            print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
            print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
            print("-"*120)

            for i in db_pegawai:
                print(f"{db_pegawai[i]['no_kereta']:^5} "
                f"{db_pegawai[i]['kode_kereta']:^8} "
                f"{db_pegawai[i]['nama_kereta']:^25} "
                f"{db_pegawai[i]['jenis_kereta']:^12} "
                f"{db_pegawai[i]['rute_perjalanan']:^25} "
                f"{db_pegawai[i]['harga']:^12} "
                f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
            print("="*120)

            while True:
                print("[1] Tampilkan seluruh data kereta ")
                print("[2] Delete data kereta api by (KODE & RUTE) ")
                print("[3] Delete data kereta api by (NO KERETA) ")
                print("[4] Back ke menu ")
                
                kode = input("Masukan pilihan anda : ")
                if kode == '1':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5}{'Kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)
                
                elif kode == '2':

                    hapus_no = input("Silahkan pilih kode kereta yang ingin dihapus: ").upper()
                    hapus_rute = input("Silahkan pilih rute kereta yang ingin dihapus: ").upper()

                    
                    for key, value in db_pegawai.items():
                        if value['kode_kereta'] == hapus_no and value['rute_perjalanan'] == hapus_rute:
                            del db_pegawai[key]
                            print(f"Data dengan kode kereta {hapus_no} dan rute {hapus_rute} telah berhasil di delete.")
                            break
                    else:
                        print(f"Tidak ada no kereta dengan no {hapus_no} dan rute {hapus_rute}.")
                
                elif kode == '3':
                    
                    hapus_no_kereta = input("Silahkan pilih No kereta yang ingin dihapus: ").upper()

                    for key, value in db_pegawai.items():
                        if value['no_kereta'] == hapus_no_kereta:
                            del db_pegawai[key]
                            print(f"Data dengan No kereta {hapus_no_kereta} telah berhasil di delete.")
                            break
                    else:
                        print(f"Tidak ada no kereta dengan No Kereta {hapus_no_kereta}.")

                elif kode == '4':
                    return menu_4()

        elif kode == '5':
            while True:
                print("[1] Tampilkan Data Pemesanan Tiket Pelanggan. ")
                print("[2] Back to Menu")

                kode = input("Masukan pilihan anda : ")
                if kode == '1':

                    print("TABEL PEMESANAN TIKET KERETA API INDONESIA")
                    print(f"{'No':^5}  {'Nama':^15} {'No':^12} {'Nomor':^8} {'Kode':^7} {'Nama':^18} {'Jenis':^18} {'Rute':^20} {'Harga':^13} {'Waktu':^11} {'Tanggal':^12}")
                    print(f"{'':^5} {'Lengkap':^15} {'KTP':^12} {'Kereta':^8} {'Kereta':^7} {'Kereta':^18} {'Kereta':^18} {'Perjalanan':^20} {'':^13} {'Berangkat':^11} {'Berangkat':^12}")
                    print("-"*144)
                    for i in db_pembayaran_customer:
                        print(f"{db_pembayaran_customer[i]['no']:^5}"
                        f"{db_pembayaran_customer[i]['nama_lengkap']:^15}"
                        f"{db_pembayaran_customer[i]['no_ktp']:^12}"
                        f"{db_pembayaran_customer[i]['no_kereta']:^8} "
                        f"{db_pembayaran_customer[i]['kode_kereta']:^7} "
                        f"{db_pembayaran_customer[i]['nama_kereta']:^18} "
                        f"{db_pembayaran_customer[i]['jenis_kereta']:^18}"
                        f"{db_pembayaran_customer[i]['rute_perjalanan']:^20}"
                        f"{db_pembayaran_customer[i]['harga']:^13}"
                        f"{db_pembayaran_customer[i]['waktu_keberangkatan']:^11}"
                        f"{db_pembayaran_customer[i]['tanggal_keberangkatan']:^12}")
                    print("="*144)
                
                elif kode == '2':
                    return menu_4()
                else:
                    print("Pilihan menu tidak tersedia, silahkan pilih kembali.")

        elif kode == '6':
            return menu_3()
        
        lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
        if lanjut.lower() != 'y':
            return menu_4()

    
def menu_3():
    while True:
        print("\n SELAMAT DATANG DI WEB KERETA API INDONESIA")
        print("="*50)
        print("[1] Login")
        print("[2] Kembali ke menu utama")
        
        kode = input("Masukan pilihan anda : ")

        if kode == '1':
                username = input("Masukan username anda : ")
                password = input("masukan password anda : ")

                try:
                    if username == 'admin' and password =="admin1234":
                        print("Selamat anda berhasil login ")
                        return menu_4()
                    else:
                        if username != 'admin':
                            print("Username salah")
                        else:
                            print("password salah")  

                except:
                    pass

        elif kode == '2':
            return menu_1()
        
        else:
            print("Pilihan tidak valid, silahkah pilih menu pilihan dengan benar")
        
        lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
        if lanjut.lower() != 'y':
            break
        else:
            continue

def menu_5():
    while True:
        print("\n SELAMAT DATANG DI WEB KERETA API INDONESIA")
        print("\n Berikut merupakan DASHBOARD pelanggan Kerta Api Indonesia")
        print("="*80)
        print("[1] Jadwal Keberangkatan Kereta Api")
        print("[2] Pemesanan Tiket Kereta Api")
        print("[3] Delete Pemesanan Tiket Kereta Api")
        print("[4] Pelunasan Tiket Kereta Api")
        print("[5] Kembali ke menu utama")
        
        kode = input("Masukan pilihan anda : ")

        if kode == '1':
            print("Daftar Kereta Api Indonesia")
            print("="*120)
            print(f"{'No':^5} {'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
            print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
            print("-"*120)
            for i in db_pegawai:
                print(f"{db_pegawai[i]['no_kereta']:^5} "
                f"{db_pegawai[i]['kode_kereta']:^8} "
                f"{db_pegawai[i]['nama_kereta']:^25} "
                f"{db_pegawai[i]['jenis_kereta']:^12}"
                f"{db_pegawai[i]['rute_perjalanan']:^25}"
                f"{db_pegawai[i]['harga']:^12}"
                f"{db_pegawai[i]['waktu_keberangkatan']:^14}"
                f"{db_pegawai[i]['tanggal_keberangkatan']:^20}")
            print("="*120)
            
            while True :
                print("[1] Tampilkan semua data kereta ")
                print("[2] Pencarian bedasarkan Kode Kereta ")
                print("[3] Pencarian bedasarkan Rute Kereta ")
                print("[4] Pencarian bedasarkan No Kereta ")
                print("[5] Back ke menu ")
                
                kode = input("Masukan pilihan anda : ")

                if kode == '1':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5}{'Kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^14} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^20}")
                    print("-"*120)

                elif kode == '2':

                    kode_kereta = input("Masukkan kode kereta yang ingin ditampilkan: ")
                    print("="*120)
                    print(f"{'No':^5}{'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    ketemu = False
                    for i in db_pegawai:
                        if db_pegawai[i]['kode_kereta'] == kode_kereta.upper():
                            print(f"{db_pegawai[i]['no_kereta']:^5} "
                            f"{db_pegawai[i]['kode_kereta']:^8} "
                            f"{db_pegawai[i]['nama_kereta']:^25} "
                            f"{db_pegawai[i]['jenis_kereta']:^12} "
                            f"{db_pegawai[i]['rute_perjalanan']:^25} "
                            f"{db_pegawai[i]['harga']:^12} "
                            f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                            f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                            ketemu = True
                    if not ketemu:
                        print(f"Tidak ada kereta dengan Kode {kode_kereta}")
                    print("-"*120)
                
                elif kode == '3':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5}{'Kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)

                    rute_kereta = input("Masukkan rute kereta yang ingin ditampilkan: ")
                    print("="*120)
                    print(f"{'No':^5}{'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    ketemu = False
                    for i in db_pegawai:
                        if db_pegawai[i]['rute_perjalanan'] == rute_kereta.upper():
                            print(f"{db_pegawai[i]['no_kereta']:^5} "
                            f"{db_pegawai[i]['kode_kereta']:^8} "
                            f"{db_pegawai[i]['nama_kereta']:^25} "
                            f"{db_pegawai[i]['jenis_kereta']:^12} "
                            f"{db_pegawai[i]['rute_perjalanan']:^25} "
                            f"{db_pegawai[i]['harga']:^12} "
                            f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                            f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                            ketemu = True
                    if not ketemu:
                        print(f"Tidak ada kereta dengan Rute {rute_kereta}")
                    print("-"*120)
                
                elif kode == '4':
                    print("Daftar Kereta Api Indonesia")
                    print("="*120)
                    print(f"{'No':^5}{'Kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12} "
                        f"{db_pegawai[i]['rute_perjalanan']:^25} "
                        f"{db_pegawai[i]['harga']:^12} "
                        f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                    print("="*120)

                    no_kereta = input("Masukkan Nomer kereta yang ingin ditampilkan: ")
                    print("="*120)
                    print(f"{'No':^5}{'kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5}{'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    
                    ketemu = False
                    for i in db_pegawai:
                        if db_pegawai[i]['no_kereta'] == no_kereta.upper():
                            print(f"{db_pegawai[i]['no_kereta']:^5} "
                            f"{db_pegawai[i]['kode_kereta']:^8} "
                            f"{db_pegawai[i]['nama_kereta']:^25} "
                            f"{db_pegawai[i]['jenis_kereta']:^12} "
                            f"{db_pegawai[i]['rute_perjalanan']:^25} "
                            f"{db_pegawai[i]['harga']:^12} "
                            f"{db_pegawai[i]['waktu_keberangkatan']:^10} "
                            f"{db_pegawai[i]['tanggal_keberangkatan']:^15}")
                            ketemu = True
                    if not ketemu:
                        print(f"Tidak ada kereta dengan Rute {no_kereta}")

                    print("-"*120)

                elif kode == '5':
                    return menu_5()
                else:
                    print("Input menu tidak tersedia, seilahkan input kembali")

        if kode == '2':
            print(f"{'No':^5} {'Kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
            print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
            print("-"*120)
            for i in db_pegawai:
                print(f"{db_pegawai[i]['no_kereta']:^5} "
                f"{db_pegawai[i]['kode_kereta']:^8} "
                f"{db_pegawai[i]['nama_kereta']:^25} "
                f"{db_pegawai[i]['jenis_kereta']:^12}"
                f"{db_pegawai[i]['rute_perjalanan']:^25}"
                f"{db_pegawai[i]['harga']:^12}"
                f"{db_pegawai[i]['waktu_keberangkatan']:^14}"
                f"{db_pegawai[i]['tanggal_keberangkatan']:^20}")
            print("="*120)

            while True :
                print("[1] Tampilkan Jadwal Tiket Kereta Api ")
                print("[2] Pembelian Tiket Kereta Api ")
                print("[3] Back to Menu ")
                
                kode = input("Masukan pilihan anda : ")

                if kode == '1':
                    print(f"{'No':^5} {'Kode':^8} {'Nama':^25} {'Jenis':^12} {'Rute':^25} {'Harga':^12} {'Waktu':^10} {'Tanggal':^15}")
                    print(f"{'Kereta':^5} {'Kereta':^8} {'Kereta':^25} {'Kereta':^12} {'Perjalanan':^25} {'':^12} {'Berangkat':^10} {'Berangkat':^15}")
                    print("-"*120)
                    for i in db_pegawai:
                        print(f"{db_pegawai[i]['no_kereta']:^5} "
                        f"{db_pegawai[i]['kode_kereta']:^8} "
                        f"{db_pegawai[i]['nama_kereta']:^25} "
                        f"{db_pegawai[i]['jenis_kereta']:^12}"
                        f"{db_pegawai[i]['rute_perjalanan']:^25}"
                        f"{db_pegawai[i]['harga']:^12}"
                        f"{db_pegawai[i]['waktu_keberangkatan']:^14}"
                        f"{db_pegawai[i]['tanggal_keberangkatan']:^20}")
                    print("="*120)

                elif kode == '2':

                    pembelian_kode = input("Masukan kode kereta yang dipilih : ").upper()
                    pembelian_rute = input("Masukan rute kereta yang dipilih : ").upper()

                    kode_terpilih = None

                    for key, value in db_pegawai.items():
                        if value['kode_kereta'] == pembelian_kode and value['rute_perjalanan'] == pembelian_rute:
                            kode_terpilih = value
                            break
                    else:
                        print(f"Data no kereta dengan no {pembelian_kode} dan rute {pembelian_rute} tidak tersedia.")

                    if kode_terpilih:
                        db_temp_pelanggan[f"pelanggan_{len(db_temp_pelanggan) + 1}"] = {
                            'no': len(db_temp_pelanggan) + 1,
                            'nama_lengkap': data_pembeli['nama_lengkap'],
                            'no_ktp': data_pembeli['no_ktp'],
                            'no_kereta' : kode_terpilih['no_kereta'],
                            'kode_kereta': kode_terpilih['kode_kereta'],
                            'nama_kereta': kode_terpilih['nama_kereta'],
                            'jenis_kereta': kode_terpilih['jenis_kereta'],
                            'rute_perjalanan': kode_terpilih['rute_perjalanan'],
                            'harga': kode_terpilih['harga'],
                            'waktu_keberangkatan': kode_terpilih['waktu_keberangkatan'],
                            'tanggal_keberangkatan': kode_terpilih['tanggal_keberangkatan']
                        }
                    else:
                        print("data gagal terpilih, silahkan memilih ulang")

                    print("=" * 144)
                    print(f"{'No':^5}{'Nama':^18}{'No':^12}{'Nomor':^8}{'Kode':^7}{'Nama':^18}{'Jenis':^18}{'Rute':^20}{'Harga':^13}{'Waktu':^11}{'Tanggal':^12}")
                    print(f"{'':^5}{'Lengkap':^18}{'KTP':^12}{'Kereta':^8}{'Kereta':^7}{'Kereta':^18}{'Kereta':^18}{'Perjalanan':^20}{'':^13}{'Berangkat':^11}{'Berangkat':^12}")
                    print("-" * 144)

                    for i in db_temp_pelanggan:
                        print(f"{db_temp_pelanggan[i]['no']:^5}"
                            f"{db_temp_pelanggan[i]['nama_lengkap']:^18}"
                            f"{db_temp_pelanggan[i]['no_ktp']:^12}"
                            f"{db_temp_pelanggan[i]['no_kereta']:^8}"
                            f"{db_temp_pelanggan[i]['kode_kereta']:^7}"
                            f"{db_temp_pelanggan[i]['nama_kereta']:^18}"
                            f"{db_temp_pelanggan[i]['jenis_kereta']:^18}"
                            f"{db_temp_pelanggan[i]['rute_perjalanan']:^20}"
                            f"{db_temp_pelanggan[i]['harga']:^13}"
                            f"{db_temp_pelanggan[i]['waktu_keberangkatan']:^11}"
                            f"{db_temp_pelanggan[i]['tanggal_keberangkatan']:^12}")
                    print("=" * 144)

                elif kode == '3':
                    return menu_5()
                else:
                    print('Pilihan Menu tidak tersedia silahkan pilih kembali')

        if kode == '3':
            print("TABEL PEMESANAN TIKET KERETA API INDONESIA")
            print(f"{'No':^5}{'Nama':^18}{'No':^12}{'Nomor':^8}{'Kode':^7}{'Nama':^18}{'Jenis':^18}{'Rute':^20}{'Harga':^13}{'Waktu':^11}{'Tanggal':^12}")
            print(f"{'':^5}{'Lengkap':^18}{'KTP':^12}{'Kereta':^8}{'Kereta':^7}{'Kereta':^18}{'Kereta':^18}{'Perjalanan':^20}{'':^13}{'Berangkat':^11}{'Berangkat':^12}")
            print("-" * 144)
            
            for i in db_temp_pelanggan:
                print(f"{db_temp_pelanggan[i]['no']:^5}"
                    f"{db_temp_pelanggan[i]['nama_lengkap']:^18}"
                    f"{db_temp_pelanggan[i]['no_ktp']:^12}"
                    f"{db_temp_pelanggan[i]['no_kereta']:^8}"
                    f"{db_temp_pelanggan[i]['kode_kereta']:^7}"
                    f"{db_temp_pelanggan[i]['nama_kereta']:^18}"
                    f"{db_temp_pelanggan[i]['jenis_kereta']:^18}"
                    f"{db_temp_pelanggan[i]['rute_perjalanan']:^20}"
                    f"{db_temp_pelanggan[i]['harga']:^13}"
                    f"{db_temp_pelanggan[i]['waktu_keberangkatan']:^11}"
                    f"{db_temp_pelanggan[i]['tanggal_keberangkatan']:^12}")
            print("=" * 144)

            while True :
                print("[1] Tampilkan Pemesanan Tiket Kereta Api ")
                print("[2] Hapus Data Pemesanan Tiket Kereta Api ")
                print("[3] Back to Menu ")
                
                kode = input("Masukan pilihan anda : ")

                if kode == '1':
                    print("TABEL PEMESANAN TIKET KERETA API INDONESIA")
                    print(f"{'No':^5}{'Nama':^18}{'No':^12}{'Nomor':^8}{'Kode':^7}{'Nama':^18}{'Jenis':^18}{'Rute':^20}{'Harga':^13}{'Waktu':^11}{'Tanggal':^12}")
                    print(f"{'':^5}{'Lengkap':^18}{'KTP':^12}{'Kereta':^8}{'Kereta':^7}{'Kereta':^18}{'Kereta':^18}{'Perjalanan':^20}{'':^13}{'Berangkat':^11}{'Berangkat':^12}")
                    print("-" * 144)
                    
                    for i in db_temp_pelanggan:
                        print(f"{db_temp_pelanggan[i]['no']:^5}"
                            f"{db_temp_pelanggan[i]['nama_lengkap']:^18}"
                            f"{db_temp_pelanggan[i]['no_ktp']:^12}"
                            f"{db_temp_pelanggan[i]['no_kereta']:^8}"
                            f"{db_temp_pelanggan[i]['kode_kereta']:^7}"
                            f"{db_temp_pelanggan[i]['nama_kereta']:^18}"
                            f"{db_temp_pelanggan[i]['jenis_kereta']:^18}"
                            f"{db_temp_pelanggan[i]['rute_perjalanan']:^20}"
                            f"{db_temp_pelanggan[i]['harga']:^13}"
                            f"{db_temp_pelanggan[i]['waktu_keberangkatan']:^11}"
                            f"{db_temp_pelanggan[i]['tanggal_keberangkatan']:^12}")
                    print("=" * 144)

                elif kode == '2':
                    hapus_no_urut = int(input("Silahkan pilih nomor kereta yang ingin dihapus: "))

                    for key, value in list(db_temp_pelanggan.items()):
                        if value['no'] == hapus_no_urut:
                            del db_temp_pelanggan[key]
                            print(f"Data {hapus_no_urut} telah berhasil di delete.")
                            break
                    else:
                        print(f"Anda belum berhasil menghapus data .")
                    
                    new_no = 1
                    for key in db_temp_pelanggan:
                        db_temp_pelanggan[key]['no'] = new_no
                        new_no += 1
                
                elif kode == '3':
                    return menu_5()
                else:
                    print("Pilihan menu tidak tersedia, silahkan pilih kembali. ")

        if kode == '4':
            print("PELUNASAN TIKET KERETA API INDONESIA")
            print(f"{'No':^5}{'Nama':^18}{'No':^12}{'Nomor':^8}{'Kode':^7}{'Nama':^18}{'Jenis':^18}{'Rute':^20}{'Harga':^13}{'Waktu':^11}{'Tanggal':^12}")
            print(f"{'':^5}{'Lengkap':^18}{'KTP':^12}{'Kereta':^8}{'Kereta':^7}{'Kereta':^18}{'Kereta':^18}{'Perjalanan':^20}{'':^13}{'Berangkat':^11}{'Berangkat':^12}")
            print("-" * 144)
            
            for i in db_temp_pelanggan:
                print(f"{db_temp_pelanggan[i]['no']:^5}"
                    f"{db_temp_pelanggan[i]['nama_lengkap']:^18}"
                    f"{db_temp_pelanggan[i]['no_ktp']:^12}"
                    f"{db_temp_pelanggan[i]['no_kereta']:^8}"
                    f"{db_temp_pelanggan[i]['kode_kereta']:^7}"
                    f"{db_temp_pelanggan[i]['nama_kereta']:^18}"
                    f"{db_temp_pelanggan[i]['jenis_kereta']:^18}"
                    f"{db_temp_pelanggan[i]['rute_perjalanan']:^20}"
                    f"{db_temp_pelanggan[i]['harga']:^13}"
                    f"{db_temp_pelanggan[i]['waktu_keberangkatan']:^11}"
                    f"{db_temp_pelanggan[i]['tanggal_keberangkatan']:^12}")
            print("=" * 144)
            
            while True :
                print("[1] Tampilkan Pemesanan Tiket Kereta Api ")
                print("[2] Hapus Data Pemesanan Tiket Kereta Api ")
                print("[3] Back to Menu ")
                
                kode = input("Masukan pilihan anda : ")

                if kode == '1':
                    print("PELUNASAN TIKET KERETA API INDONESIA")
                    print(f"{'No':^5}{'Nama':^18}{'No':^12}{'Nomor':^8}{'Kode':^7}{'Nama':^18}{'Jenis':^18}{'Rute':^20}{'Harga':^13}{'Waktu':^11}{'Tanggal':^12}")
                    print(f"{'':^5}{'Lengkap':^18}{'KTP':^12}{'Kereta':^8}{'Kereta':^7}{'Kereta':^18}{'Kereta':^18}{'Perjalanan':^20}{'':^13}{'Berangkat':^11}{'Berangkat':^12}")
                    print("-" * 144)
                    
                    for i in db_temp_pelanggan:
                        print(f"{db_temp_pelanggan[i]['no']:^5}"
                            f"{db_temp_pelanggan[i]['nama_lengkap']:^18}"
                            f"{db_temp_pelanggan[i]['no_ktp']:^12}"
                            f"{db_temp_pelanggan[i]['no_kereta']:^8}"
                            f"{db_temp_pelanggan[i]['kode_kereta']:^7}"
                            f"{db_temp_pelanggan[i]['nama_kereta']:^18}"
                            f"{db_temp_pelanggan[i]['jenis_kereta']:^18}"
                            f"{db_temp_pelanggan[i]['rute_perjalanan']:^20}"
                            f"{db_temp_pelanggan[i]['harga']:^13}"
                            f"{db_temp_pelanggan[i]['waktu_keberangkatan']:^11}"
                            f"{db_temp_pelanggan[i]['tanggal_keberangkatan']:^12}")
                    print("=" * 144)

                elif kode == '2':
                    pelunasan_no = int(input("Masukkan nomor tiket yang ingin dilunasi: "))
                    
                    for key, value in db_temp_pelanggan.items():
                        if value['no'] == pelunasan_no:
                            print(f"\nDetail Tiket:")
                            print(f"Nama: {value['nama_lengkap']}")
                            print(f"Nomor Kereta {value['no_kereta']}")
                            print(f"Kode Kereta {value['kode_kereta']}")
                            print(f"Nama Kereta {value['nama_kereta']}")
                            print(f"Rute: {value['rute_perjalanan']}")
                            print(f"Harga: Rp {value['harga']}")
                            
                            konfirmasi = input("\nApakah Anda yakin ingin melunasi tiket ini? (y/n): ")
                            if konfirmasi.lower() == 'y':
                                total_pembayaran = int(value['harga'])
                                pembayaran = 0
                                while pembayaran < total_pembayaran:
                                    print(f"\nTotal pembayaran anda menjadi Rp. {total_pembayaran}")
                                    if pembayaran > 0:
                                        print(f"Anda sudah membayar Rp. {pembayaran}")
                                        print(f"Sisa yang harus anda bayar Rp. {total_pembayaran - pembayaran}")
                                    
                                    tambahan = int(input("Silahkan masukan nominal pembayaran: "))
                                    pembayaran += tambahan

                                    if pembayaran < total_pembayaran:
                                        print(f"Nominal pembayaran anda masih kurang sebesar Rp. {total_pembayaran - pembayaran}")
                                        lanjut = input("Apakah anda ingin menambah pembayaran? (y/n): ")
                                        if lanjut.lower() != 'y':
                                            print("Pembayaran dibatalkan. Terima kasih.")
                                            break

                                if pembayaran >= total_pembayaran:
                                    kembalian = pembayaran - total_pembayaran
                                    if kembalian > 0:
                                        print(f"Terimakasih uang kembalian anda sebesar Rp. {kembalian}")
                                    else:
                                        print("Terimakasih, Anda membayar dengan uang pas")

                                    
                                    db_konfirmasi_pelanggan = {}
                                    db_konfirmasi_pelanggan[f"pelanggan_{len(db_konfirmasi_pelanggan) + 1}"] = value

                                    db_pembayaran_customer[f"pelanggan_{len(db_pembayaran_customer) + 1}"] = value.copy()
                                    del db_temp_pelanggan[key]
                                    print("Pelunasan berhasil")
                            else:
                                print("Pelunasan dibatalkan.")
                            break
                    else:
                        print(f"Tiket dengan nomor {pelunasan_no} tidak ditemukan.")
                
                elif kode == '3':
                    return menu_5()
                else:
                    print("Pilihan menu tidak tersedia, silahkan pilih kembali. ")

        if kode == '5':
            return menu_2()
        else:
            pass

def menu_2():
    while True:
        print("\n SELAMAT DATANG DI WEB KERETA API INDONESIA")
        print("="*50)
        print("[1] Isi identitas anda")
        print("[2] Kembali ke menu utama")

        kode = input("Masukan pilihan anda : ")

        if kode == '1':
            while True:
                    while True:
                        nama_depan = input("Masukan nama depan anda : ")
                        if not nama_depan.isalpha():
                            print(f"Nama {nama_depan} yang anda input tidak valid, silahkan isikan kembali nama depan anda")
                            continue
                        break

                    while True:
                        nama_belakang = input("masukan nama belakang anda (nama belakang adalah nama setelah nama depan anda) : ")
                        if not nama_belakang.isalpha():
                            print(f"Nama {nama_belakang} yang anda input tidak valid, silahkan isikan kembali nama depan anda")
                            continue
                        break

                    while True:
                        try:
                            no_ktp = int(input("masukan no ktp anda : "))
                            break
                        except:
                             print("No KTP yang anda masukan tidak valid, silahkan isi kembali")

                    nama_lengkap_pembeli = nama_depan.capitalize() + " " + nama_belakang.capitalize()
                    
                    global data_pembeli
                    data_pembeli = {
                        'nama_lengkap': nama_lengkap_pembeli,
                        'no_ktp': no_ktp
                    }

                    print("silahkan komfirmasi data berikut : ")
                    print(f"Nama anda {nama_lengkap_pembeli} ")
                    print(f"No KTP anda adalah {no_ktp}")

                    lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
                    if lanjut.lower() == 'y':
                        return menu_5()
                    else:
                        return menu_2()
                
                
        elif kode == '2':
            return menu_1()
        
        else:
            print("Pilihan tidak valid, silahkah pilih menu pilihan dengan benar")
        
        lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
        if lanjut.lower() != 'y':
            break
        else:
            continue


def menu_1():
    while True:
        print("\n SELAMAT DATANG DI WEB KERETA API INDONESIA")
        print("="*50)
        print("[1] Masuk sebagai Pembeli Tiket")
        print("[2] Masuk sebagai pegawai ")
        print("[3] Keluar")

        kode = input("Pilih menu pilihan anda: ")

        if kode == '1':
            if not menu_2():
                break
        elif kode == '2':
            if not menu_3():
                break
        elif kode == '3':
            print("Terimakasih, silahkan mengunjungi web kami lain waktu")
            break
        else:
            print("Pilihan tidak valid, silahkan masukan pilihan anda dengan benar")

menu_1()