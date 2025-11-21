import sys, random, time, os
import biologi, kimia, informatika

def clear():
    os.system("cls" if os.name == "nt" else "clear")

skor_kimia = {
    'Jumlah sesi      :' : 0,
    'Total pertanyaan :' : 0,
    'Jawaban benar    :' : 0,
    'Akurasi          :' : 0,
    'Highest streak   :' : 0,
}

skor_biologi = {
    'Jumlah sesi      :' : 0,
    'Total pertanyaan :' : 0,
    'Jawaban benar    :' : 0,
    'Akurasi          :' : 0,
    'Highest streak   :' : 0,
}

skor_informatika = {
    'Jumlah sesi      :' : 0,
    'Total pertanyaan :' : 0,
    'Jawaban benar    :' : 0,
    'Akurasi          :' : 0,
    'Highest streak   :' : 0,
}

def puzzle_streak(skor, jenis):
    n = 0
    match jenis:
        case 'KIMIA' | '1':
            while True:
                hasil = kimia.tebak_spu()
                if hasil[0] == 0:
                    print(hasil[1])
                    break
                n+=1
        case 'BIOLOGI' | '2':
            while True:
                hasil = biologi.tebak_gen_spes()
                if hasil[0] == 0:
                    print(hasil[1])
                    break
                n+=1
        case 'INFORMATIKA' | '3':
            while True:
                hasil = informatika.soal_bil()
                if hasil[0] == 0:
                    print(hasil[1])
                    break
                n+=1
        
    return (n, n+1)

def update_akurasi(skor, benar, TTLpertanyaan):
    nama_key = list(skor.keys())
    jumlah_sesi = skor[nama_key[0]]
    total_pertanyaan = skor[nama_key[1]]+TTLpertanyaan
    jawaban_benar = skor[nama_key[2]]+benar
    streak = skor[nama_key[3]]

    #jumlah sesi
    jumlah_sesi+=1

    #streak
    if benar>streak:
        streak=benar

    #akurasi 
    akurasi_new = (jawaban_benar/total_pertanyaan)*100
    skor.update({nama_key[4]:streak, nama_key[3]:akurasi_new, nama_key[2]:jawaban_benar, nama_key[1]:total_pertanyaan, nama_key[0]:jumlah_sesi})

line = 40

def print_ui_1():
    print('----MAIN MENU----')
    print('   1. Latihan soal   ')
    print('   2. Materi   ')
    print('   3. Statistik  ')
    print('   4. Keluar     ')
    print('-----------------')

def print_statistik(stats):
    nama_keys = list(stats.keys())
    for i in nama_keys:
        print(i,stats[i])

def masuk(x):
    a = input(f'{x}\n> ').upper()
    return a

def enter():
    input("------------------------\nTekan enter untuk melanjutkan\n> ")

while True:
    try:
        clear()
        print_ui_1()
        KC = masuk('Apa yang ingin anda lakukan?')
        match KC:
            case '1' | 'LATIHAN SOAL':
                while True:
                    clear()
                    print('---LATIHAN SOAL---')
                    print('   1. KIMIA     ')#1
                    print('   2. BIOLOGI    ')#2
                    print('   3. INFORMATIKA  ')#3
                    print('   4. RETURN    ')#4
                    print('------------------')
                    KC2 = masuk('Pilih mata pelajaran')
                    clear()
                    match KC2:
                        case '1' | 'KIMIA':
                            while True:
                                clear()
                                print('-----------------')
                                print('   1. LATIHAN    ')
                                print('   2. STREAK     ')
                                print('   3. RETURN     ')
                                print('-----------------')
                                KC3 = masuk('Pilih jenis latihan')
                                clear()
                                match KC3:
                                    case '1' | 'LATIHAN SOAL':
                                        jumlah_soal = int(input('Mau mengerjakan berapa soal?\n> '))
                                        clear()
                                        for i in range(jumlah_soal):
                                            print('------------------------')
                                            hasil = kimia.tebak_spu()
                                            print(f'{hasil[1]}\n')
                                            update_akurasi(skor_kimia, hasil[0],1)
                                        enter()
                                    case '2' | 'STREAK':
                                        hasil = puzzle_streak(skor_kimia,'1')
                                        update_akurasi(skor_kimia, hasil[0],hasil[1])
                                    case '3' | 'RETURN':
                                        break

                        case '2' | 'BIOLOGI':
                            while True:
                                clear()
                                print('-----------------')
                                print('   1. LATIHAN    ')
                                print('   2. STREAK     ')
                                print('   3. RETURN     ')
                                print('-----------------')
                                KC3 = masuk('Pilih jenis latihan')
                                clear()
                                match KC3:
                                    case '1' | 'LATIHAN':
                                        jumlah_soal = int(input('Mau mengerjakan berapa soal?\n> '))
                                        clear()
                                        for i in range(jumlah_soal):
                                            print('------------------------')
                                            hasil = biologi.tebak_gen_spes()
                                            print(f'{hasil[1]}\n')
                                            update_akurasi(skor_biologi, hasil[0],1)
                                        enter()
                                    case '2' | 'STREAK':
                                        hasil = puzzle_streak(skor_biologi,'BIOLOGI')
                                        update_akurasi(skor_biologi, hasil[0],hasil[1])
                                        enter()
                                    case '3' | 'RETURN':
                                        break
                        
                        case '3' | 'INFORMATIKA':
                            while True:
                                clear()
                                print('-----------------')
                                print('   1. LATIHAN    ')
                                print('   2. STREAK     ')
                                print('   3. RETURN     ')
                                print('-----------------')
                                KC3 = masuk('Pilih jenis latihan')
                                clear()
                                match KC3:
                                    case '1' | 'LATIHAN':
                                        jumlah_soal = int(input('Mau mengerjakan berapa soal?\n> '))
                                        clear()
                                        for i in range(jumlah_soal):
                                            print('------------------------')
                                            hasil = informatika.soal_bil()
                                            print(f'{hasil[1]}\n')
                                            update_akurasi(skor_informatika, hasil[0],1)
                                        enter()
                                    case '2' | 'STREAK':
                                        hasil = puzzle_streak(skor_informatika,'INFORMATIKA')
                                        update_akurasi(skor_informatika, hasil[0],hasil[1])
                                        enter()
                                    case '3' | 'RETURN':
                                        break
                            
                        case '4' | 'RETURN':
                            break
            case '2' | 'MATERI':
                while True:
                    clear()
                    print('-----MATERI-----')
                    print('   1. KIMIA     ')#1
                    print('   2. BIOLOGI    ')#2
                    print('   3. INFORMATIKA  ')#3
                    print('   4. RETURN    ')#4
                    print('------------------')
                    KC2 = masuk("Pilih mata pelajaran")
                    match KC2:
                            case '1' | 'KIMIA':
                                clear()
                                kimia.cetak_spu()
                            case '2' | 'BIOLOGI':
                                clear()
                                biologi.cetak_takson()
                            case '3' | 'INFORMATIKA':
                                while True:
                                    clear()
                                    a = informatika.konverter()
                                    if a == 'return':
                                        break
                            case '4' | 'RETURN':
                                break
            case     '3' | 'STATISTIK':
                while True:
                    clear()
                    print('-----CEK SKOR-----')
                    print('   1. KIMIA     ')#1
                    print('   2. BIOLOGI    ')#2
                    print('   3. INFORMATIKA  ')#3
                    print('   4. RETURN    ')#4
                    print('------------------')
                    KC2 = masuk('Pilih mata pelajaran')
                    match KC2:
                        case '1' | 'KIMIA':
                            clear()
                            print('==========KIMIA==========')
                            print_statistik(skor_kimia)
                            enter()
                            clear()
                        case '2' | 'BIOLOGI':
                            clear()
                            print('=========BIOLOGI=========')
                            print_statistik(skor_biologi)
                            enter()
                        case '3' | 'INFORMATIKA':
                            clear()
                            print('=======INFORMATIKA=======')
                            print_statistik(skor_informatika)
                            enter()
                        case '4' | 'RETURN':
                            break
            case '4' | 'KELUAR':
                print("Loging out....")
                time.sleep(1)
                clear()
                break
    except:
        input('TERJADI SUATU KESALAHAN, TEKAN ENTER UNTUK MELANJUTKAN\n> ')