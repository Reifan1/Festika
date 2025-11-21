import random, os

#List
taksonomi = {
    "Harimau"    : ("Panthera", "tigris"),
    "Singa"      : ("Panthera", "leo"),
    "Kucing"     : ("Felis", "catus"),
    "Anjing"     : ("Canis", "familiaris"),
    "Serigala"   : ("Canis", "lupus"),
    "Rubah"      : ("Vulpes", "vulpes"),
    "Beruang"    : ("Ursus", "arctos"),
    "Panda"      : ("Ailuropoda", "melanoleuca"),
    "Jerapah"    : ("Giraffa", "camelopardalis"),
    "Zebra"      : ("Equus", "quagga"),
    "Kuda"       : ("Equus", "caballus"),
    "Bison"      : ("Bison", "bison"),
    "Sapi"       : ("Bos", "taurus"),
    "Kerbau"     : ("Bubalus", "bubalis"),
    "Kambing"    : ("Capra", "hircus"),
    "Domba"      : ("Ovis", "aries"),
    "Gajah"      : ("Elephas", "maximus"),
    "Koala"      : ("Phascolarctos", "cinereus"),
    "Kangguru"   : ("Macropus", "rufus"),
    "Komodo"     : ("Varanus", "komodoensis"),
    "Iguana"     : ("Iguana", "iguana"),
    "Buaya"      : ("Crocodylus", "porosus"),
    "Elang"      : ("Haliaeetus", "leucocephalus"),
    "Merpati"    : ("Columba", "livia"),
    "Cendrawasih": ("Paradisaea", "minor"),
    "Ayam"       : ("Gallus", "gallus"),
    "Bebek"      : ("Anas", "platyrhynchos"),
    "Puyuh"      : ("Coturnix", "japonica"),
    "Hiu"        : ("Carcharodon", "carcharias"),
    "Paus"       : ("Balaenoptera", "musculus"),
    "Katak"      : ("Rana", "temporaria"),
    "Kodok"      : ("Bufo", "bufo"),
    "Tikus"      : ("Rattus", "rattus"),
    "Hamster"    : ("Mesocricetus", "auratus"),
    "Landak"     : ("Hystrix", "cristata"),
    "Unta"       : ("Camelus", "dromedarius"),
    "Llama"      : ("Lama", "glama"),
    "Babi"       : ("Sus", "scrofa"),
    "Badak"      : ("Rhinoceros", "unicornis"),
    "Simpanse"   : ("Pan", "troglodytes"),
    "Gorila"     : ("Gorilla", "gorilla"),
    "Tupai"      : ("Sciurus", "vulgaris"),
    "Sotong"     : ("Sepia", "officinalis"),
    "Gurita"     : ("Octopus", "vulgaris"),
    "Ikan"       : ("Oreochromis", "niloticus"),  
    "Belut"      : ("Anguilla", "anguilla"),
    "Lele"       : ("Clarias", "batrachus"),
    "Patin"      : ("Pangasius", "hypophthalmus"),
    "Semut"      : ("Solenopsis", "invicta"),
    "Nyamuk"     : ("Aedes", "aegypti")
}


nama_hewan = list(taksonomi.keys())

def tebak_gen_spes():
    global taksonomi
    hewan_pilih = random.choice(nama_hewan)
    gen, spes = taksonomi[hewan_pilih][0], taksonomi[hewan_pilih][1]

    tebakan = input(f"Hewan apa yang memilikik genus {gen} dan spesies {spes}?\n------------------------\n> ").title()
    if tebakan == hewan_pilih or tebakan in taksonomi[hewan_pilih]:
        return (1, "!!!JAWABANMU BENAR!!!")
    
    else:
        return (0, f"!!!BELAJAR LAGI MANG!!!\nHewan yang benar adalah {hewan_pilih}")

def enter(x):
    p=input(f'------------------------\n(PAGE : {x}) [Ketik return untuk kembali]\nTekan enter untuk melanjutkan\n> ')
    return p.upper()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def cetak_takson():
    n=0
    for i,p in enumerate(taksonomi): 
        print(f"{i+1}: {p} \n|GEN   : {taksonomi[p][0]} \n|SPES  : {taksonomi[p][1]}")
        if (i+1) % 10 == 0:
            n+=1
            l=enter(n)
            if l=='RETURN':
                break
            clear()