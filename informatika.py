import random, os, time
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def biner(x):
    nums=list(item for item in str(x))[::-1]
    out=0
    for loop_count, number in enumerate(nums):
        out+=int(number)*2**loop_count
    return out
def oktal(x):
    nums=list(item for item in str(x))[::-1]
    out=0
    for loop_count, number in enumerate(nums, start=0):
        out+=int(number)*8**loop_count
    return out
def hexadesimal(x):
    nums=list(item for item in str(x))[::-1]
    out=0
    value_hexadesimal={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    for loop_count, number in enumerate(nums, start=0):
        out += value_hexadesimal[number]*16**loop_count
    return out 
def desimal(x):
    return x 
def BINER(x):
    x=int(x)
    lst=[]
    even=lambda x: lst.append(0) if x%2==0 else lst.append(1)
    while x > 0:
        even(x)
        x=x//2
    finish = ''.join([str(n) for n in lst[::-1]])
    return finish
def OKTAL(x):
    x=int(x)
    lst=[]
    while x > 0:
        sisa,x=x%8,x//8
        lst.append(sisa)
    finish = ''.join([str(n) for n in lst[::-1]])
    return finish
def HEXADESIMAL(x):
    x=int(x)
    value_hexadesimal={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    lst=[]
    while x > 0:
        sisa,x=x%16,x//16
        lst.append(value_hexadesimal[sisa])
    finish = ''.join([str(n) for n in lst[::-1]])
    return finish

def DESIMAL(x):
    return x 

def enter():
    input("------------------------\nTekan enter untuk melanjutkan\n> ")

def milih():
    jenis = ["desimal", "hexadesimal", "oktal", "biner"]
    awal = random.choice(jenis)
    jenis.remove(awal)
    akhir = random.choice(jenis)
    return (awal, akhir)

def soal_bil():
    angka = random.randint(1,512)
    awal,akhir = milih()
    des = angka
    angka_tampil = globals()[akhir.upper()](des)
    desimal_jawaban = globals()[akhir.lower()](angka_tampil)
    jawaban = globals()[awal.upper()](desimal_jawaban)
    clear()
    tebakan = input(f"Bilangan {akhir} {angka_tampil} jika diubah ke {awal} adalah?\n------------------------\n> ")
    if tebakan.upper() == str(jawaban):
        return (1, "!!!JAWABANMU BENAR!!!")
    else:
        return (0, f"!!!PAKAI KALKULATOR MAKANYA!!!\nJawaban yang benar : {jawaban}")
    
def konverter():
    clear()
    masukan=input("PERINGATAN\nMASUKAN SISTEM BILANGAN PERTAMA,KEDUA DAN ANGKA \nPERSIS DENGAN CONTOH [""DESIMAL KE BINER 12345678] (return untuk kembali)\n------------------------\n> ").split()
    match masukan:
        case [awal,ke,akhir,angka]:
            print(f'ANGKA DARI SISTEM BILANGAN {str.upper(awal)} KE {str.upper(akhir)} ADALAH {globals()[str.upper(akhir)](globals()[str.lower(awal)](angka))}')
            enter()
        case other:
            return 'return'