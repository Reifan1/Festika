import random,os

tabel_periodik = {
    # Format: Golongan, Periode, Simbol, Nomor Atom

    # Periode 1
    "Hidrogen   ": ("IA", 1, "H", 1),
    "Helium     ": ("VIIIA", 1, "He", 2),

    # Periode 2
    "Litium     ": ("IA", 2, "Li", 3),
    "Berilium   ": ("IIA", 2, "Be", 4),
    "Boron      ": ("IIIA", 2, "B", 5),
    "Karbon     ": ("IVA", 2, "C", 6),
    "Nitrogen   ": ("VA", 2, "N", 7),
    "Oksigen    ": ("VIA", 2, "O", 8),
    "Fluorin    ": ("VIIA", 2, "F", 9),
    "Neon       ": ("VIIIA", 2, "Ne", 10),

    # Periode 3
    "Natrium    ": ("IA", 3, "Na", 11),
    "Magnesium  ": ("IIA", 3, "Mg", 12),
    "Aluminium  ": ("IIIA", 3, "Al", 13),
    "Silikon    ": ("IVA", 3, "Si", 14),
    "Fosfor     ": ("VA", 3, "P", 15),
    "Belerang   ": ("VIA", 3, "S", 16),
    "Klorin     ": ("VIIA", 3, "Cl", 17),
    "Argon      ": ("VIIIA", 3, "Ar", 18),

    # Periode 4
    "Kalium     ": ("IA", 4, "K", 19),
    "Kalsium    ": ("IIA", 4, "Ca", 20),
    "Skandium   ": ("IIIB", 4, "Sc", 21),
    "Titanium   ": ("IVB", 4, "Ti", 22),
    "Vanadium   ": ("VB", 4, "V", 23),
    "Kromium    ": ("VIB", 4, "Cr", 24),
    "Mangan     ": ("VIIB", 4, "Mn", 25),
    "Besi       ": ("VIIIB", 4, "Fe", 26),
    "Kobalt     ": ("VIIIB", 4, "Co", 27),
    "Nikel      ": ("VIIIB", 4, "Ni", 28),
    "Tembaga    ": ("IB", 4, "Cu", 29),
    "Seng       ": ("IIB", 4, "Zn", 30),
    "Galium     ": ("IIIA", 4, "Ga", 31),
    "Germanium  ": ("IVA", 4, "Ge", 32),
    "Arsen      ": ("VA", 4, "As", 33),
    "Selen      ": ("VIA", 4, "Se", 34),
    "Bromin     ": ("VIIA", 4, "Br", 35),
    "Krypton    ": ("VIIIA", 4, "Kr", 36),

    # Periode 5
    "Rubidium   ": ("IA", 5, "Rb", 37),
    "Stronsium  ": ("IIA", 5, "Sr", 38),
    "Yttrium    ": ("IIIB", 5, "Y", 39),
    "Zirkonium  ": ("IVB", 5, "Zr", 40),
    "Niobium    ": ("VB", 5, "Nb", 41),
    "Molibdenum ": ("VIB", 5, "Mo", 42),
    "Teknesium  ": ("VIIB", 5, "Tc", 43),
    "Rutenium   ": ("VIIIB", 5, "Ru", 44),
    "Rodium     ": ("VIIIB", 5, "Rh", 45),
    "Palladium  ": ("VIIIB", 5, "Pd", 46),
    "Perak      ": ("IB", 5, "Ag", 47),
    "Kadmium    ": ("IIB", 5, "Cd", 48),
    "Indium     ": ("IIIA", 5, "In", 49),
    "Timah      ": ("IVA", 5, "Sn", 50),
    "Antimon    ": ("VA", 5, "Sb", 51),
    "Tellurium  ": ("VIA", 5, "Te", 52),
    "Iodin      ": ("VIIA", 5, "I", 53),
    "Xenon      ": ("VIIIA", 5, "Xe", 54),

    # Periode 6
    "Sesium     ": ("IA", 6, "Cs", 55),
    "Barium     ": ("IIA", 6, "Ba", 56),

    # Lantanida (57–71)
    "Lantanum   ": ("Lantanida", 6, "La", 57),
    "Serium     ": ("Lantanida", 6, "Ce", 58),
    "Praseodimium": ("Lantanida", 6, "Pr", 59),
    "Neodimium  ": ("Lantanida", 6, "Nd", 60),
    "Prometium  ": ("Lantanida", 6, "Pm", 61),
    "Samarium   ": ("Lantanida", 6, "Sm", 62),
    "Europium   ": ("Lantanida", 6, "Eu", 63),
    "Gadolinium ": ("Lantanida", 6, "Gd", 64),
    "Terbium    ": ("Lantanida", 6, "Tb", 65),
    "Dysprosium ": ("Lantanida", 6, "Dy", 66),
    "Holmium    ": ("Lantanida", 6, "Ho", 67),
    "Erbium     ": ("Lantanida", 6, "Er", 68),
    "Thulium    ": ("Lantanida", 6, "Tm", 69),
    "Ytterbium  ": ("Lantanida", 6, "Yb", 70),
    "Lutesium   ": ("IIIB", 6, "Lu", 71),

    "Hafnium    ": ("IVB", 6, "Hf", 72),
    "Tantalum   ": ("VB", 6, "Ta", 73),
    "Tungsten   ": ("VIB", 6, "W", 74),
    "Renium     ": ("VIIB", 6, "Re", 75),
    "Osmium     ": ("VIIIB", 6, "Os", 76),
    "Iridium    ": ("VIIIB", 6, "Ir", 77),
    "Platina    ": ("VIIIB", 6, "Pt", 78),
    "Emas       ": ("IB", 6, "Au", 79),
    "Raksa      ": ("IIB", 6, "Hg", 80),
    "Talium     ": ("IIIA", 6, "Tl", 81),
    "Timbal     ": ("IVA", 6, "Pb", 82),
    "Bismut     ": ("VA", 6, "Bi", 83),
    "Polonium   ": ("VIA", 6, "Po", 84),
    "Astatin    ": ("VIIA", 6, "At", 85),
    "Radon      ": ("VIIIA", 6, "Rn", 86),

    # Periode 7
    "Fransium   ": ("IA", 7, "Fr", 87),
    "Radium     ": ("IIA", 7, "Ra", 88),

    # Aktinida (89–103)
    "Aktinium   ": ("Aktinida", 7, "Ac", 89),
    "Thorium    ": ("Aktinida", 7, "Th", 90),
    "Protaktinium": ("Aktinida", 7, "Pa", 91),
    "Uranium    ": ("Aktinida", 7, "U", 92),
    "Neptunium  ": ("Aktinida", 7, "Np", 93),
    "Plutonium  ": ("Aktinida", 7, "Pu", 94),
    "Amerisium  ": ("Aktinida", 7, "Am", 95),
    "Kurium     ": ("Aktinida", 7, "Cm", 96),
    "Berkelium  ": ("Aktinida", 7, "Bk", 97),
    "Kalifornium": ("Aktinida", 7, "Cf", 98),
    "Einsteinium": ("Aktinida", 7, "Es", 99),
    "Fermium    ": ("Aktinida", 7, "Fm", 100),
    "Mendelevium": ("Aktinida", 7, "Md", 101),
    "Nobelium   ": ("Aktinida", 7, "No", 102),
    "Lawrensium ": ("IIIB", 7, "Lr", 103),

    "Rutherfordium": ("IVB", 7, "Rf", 104),
    "Dubnium    ": ("VB", 7, "Db", 105),
    "Seaborgium ": ("VIB", 7, "Sg", 106),
    "Bohrium    ": ("VIIB", 7, "Bh", 107),
    "Hassium    ": ("VIIIB", 7, "Hs", 108),
    "Meitnerium ": ("VIIIB", 7, "Mt", 109),
    "Darmstadtium": ("VIIIB", 7, "Ds", 110),
    "Roentgenium": ("IB", 7, "Rg", 111),
    "Kopernisium": ("IIB", 7, "Cn", 112),
    "Nihonium   ": ("IIIA", 7, "Nh", 113),
    "Flerovium  ": ("IVA", 7, "Fl", 114),
    "Moskovium  ": ("VA", 7, "Mc", 115),
    "Livermorium": ("VIA", 7, "Lv", 116),
    "Tenesin    ": ("VIIA", 7, "Ts", 117),
    "Oganesson  ": ("VIIIA", 7, "Og", 118),
}

nama_unsur = list(tabel_periodik.keys())

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def gol_per():
    global tabel_periodik
    unsur_dipilih = random.choice(nama_unsur)
    gol,per = tabel_periodik[unsur_dipilih][0],tabel_periodik[unsur_dipilih][1]
    info_tambahan = ''

    if gol=='VIIIB' or gol=='Lantanida' or gol=='Aktinida':
        info_tambahan = f'dengan nomer atom {tabel_periodik[unsur_dipilih][3]}'
    
    tebakan = input(f'Sebutkan nama unsur dengan golongan {gol} dan periode {per} {info_tambahan}\n------------------------\n> ').title()
    
    if tebakan==unsur_dipilih or tebakan in tabel_periodik[unsur_dipilih]:
        return (1,"!!!JAWABANMU BENER LEEE!!!")
    else:
        return (0,f"!!!SALAH , BELAJAR LAGI PREN!!!\nUnsur yang benar adalah {unsur_dipilih}")

def no_unsur():
    global tabel_periodik
    unsur_dipilih = random.choice(nama_unsur)
    nomer_atom = 0

    while True:
        if tabel_periodik[unsur_dipilih][0]=='VIIIB':
            pass
        else:
            nomer_atom = tabel_periodik[unsur_dipilih][3]
            break

    tebakan = input(f'Tebak nama unsur dengan nomer atom {nomer_atom}\n------------------------\n> ').title()
    if tebakan==unsur_dipilih or tebakan in tabel_periodik[unsur_dipilih]:
        return (1,'!!!WOWOWW HEBAT KAMU BANG!!!')
    else:
        return (0,f'!!!WALAWE SINAU O MANEH!!!\nUnsur yang benar adalah {unsur_dipilih}')

def tebak_spu():
    tipe_soal = random.randint(1,2)
    match tipe_soal:
        case 1:
            return(gol_per())
        case 2:
            return(no_unsur())

def enter(x):
    p=input(f'------------------------\n(PAGE : {x}) [Ketik return untuk kembali]\nTekan enter untuk melanjutkan\n> ')
    return p.upper()


def cetak_spu():
    n=0
    for i,p in enumerate(tabel_periodik): 
        print(f"{i+1}: {p} \n|GOL   : {tabel_periodik[p][0]} \n|PER   : {tabel_periodik[p][1]} \n|SIMBOL: {tabel_periodik[p][2]}")
        if (i+1) % 10 == 0:
            n+=1
            l=enter(n)
            if l=='RETURN':
                break
            clear()
#def skor_akurasi():
