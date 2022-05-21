from typing import Dict, Match
from collections import defaultdict
import random 
import pandas as pd
from pandas.core.frame import DataFrame
import xlsxwriter as xw
import itertools as itl
import string

#Buat table generator           || Sudah
#Isi table generator            || Sudah
#Buat random number generator   || Sudah
#Buat Fuzzification             || Sudah
#Buat Inference                 || Sudah
#Buat Defuzzification           || Belum

workbook = xw.Workbook('masukan.xlsx')            #membuat file excel baru
worksheet = workbook.add_worksheet()            #menambahkan worksheet baru
#data_set = pd.read_excel('E:/Universitas/semester_4/Kecerdasan Buatan/Tugas/FuzzyLogic/Tugas_Kelompok_AI_Fuzzy/Tugas_Kelompok_AI_Fuzzy/masukan.xlsx')

#==================== list

random.seed(12345)
tabel_NO = []
tabel_Nama = []
tabel_IPK = []
tabel_Umur = []

masukan = int(input("masukan jumlah table       :")) #menerima input integer
#Mengenerate nilai untuk table excel
#To do
#generate nomor || sudah
#Random Nama    || Sudah
#Random IPK     || Sudah
#Random Gaji    || Sudah

for i in range(0,masukan):
    i = i +1
    tabel_NO.append(i)

#    if(i<10):                                   #Test
#        tabel_NO.append("test")                 #
#    else:                                       #
#        tabel_NO.append("Test")


for i in range(0,masukan):                      
    n = string.ascii_uppercase
    char = ''.join(random.choice(n) for i in range(5))
    tabel_Nama.append(char)

for i in range(0,masukan):                      
    n = format(random.uniform(0,4),".2f")
    tabel_IPK.append(n)

for i in range(0,masukan):                      
    n = random.randint(18,30)
    tabel_Umur.append(n)


worksheet.write(0,0,"No")
worksheet.write(0,1,"Nama")
worksheet.write(0,2,"IPK")
worksheet.write(0,3,"Umur")

for i in range(0,masukan):                  #berhasil membuat table n*n berisi
    worksheet.write(i+1, 0,tabel_NO[i])
    worksheet.write(i+1, 1,tabel_Nama[i])
    worksheet.write(i+1, 2,tabel_IPK[i])
    worksheet.write(i+1, 3,tabel_Umur[i])

workbook.close()                                #menutup file yang sudah terisis


#===============================================================================
#=======================Fuzzification

#IPK Rules
# tinggi 3 < n <= 4
# sedang 2 <= n <= 3
# rendah n < 2
numIPK = []
numUMR = []

for i in range(0, len(tabel_IPK)):
    temp = float(tabel_IPK[i])
    numIPK.append(temp)

for i in range(0, len(tabel_Umur)):
    temp = float(tabel_Umur[i])
    numUMR.append(temp)

#print(tabel_IPK)
#print(numIPK)
#print(tabel_Umur)
#print(numUMR)


def IPKtinggi(numIPK):
    I_Tinggi = float

    if(float(numIPK[i]) > 3):
        I_Tinggi = 1
    elif(float(numIPK[i]) >= 2 and float(numIPK[i]) <= 3):
        I_Tinggi = (3 - float(numIPK[i]))/2
    elif(float(numIPK[i]) <2):
        I_Tinggi = 0
    return I_Tinggi

def IPKsedang(numIPK):
    I_Sedang = float
    if(float(numIPK[i]) > 3):
        I_Sedang = 0
    elif(float(numIPK[i]) >= 2 and float(numIPK[i]) <= 3):
        I_Sedang = (3 - float(numIPK[i]))/2
    elif(float(numIPK[i]) <2):
        I_Sedang = 0
    return I_Sedang

def IPKrendah(numIPK):
    I_Rendah = float
    if(float(numIPK[i]) > 3):
        I_Rendah = 0
    elif(float(numIPK[i]) >= 2 and float(numIPK[i]) <= 3):
        I_Rendah = (3 - float(numIPK[i]))/2
    elif(float(numIPK[i]) <2):
        I_Rendah = 1
    return I_Rendah

tinggi  =[]
sedang  =[]
rendah  =[]
for i in range(len(tabel_IPK)):
    tinggi.append(IPKtinggi(tabel_IPK))
    sedang.append(IPKsedang(tabel_IPK))
    rendah.append(IPKrendah(tabel_IPK))


#print(tinggi)
#print(sedang)
#print(rendah)

#usia
# muda      18 <= n < 21
# menengah  21 <= n <= 25
# tua       25 < n <= 30


def usiaMuda(tabel_Umur):
    Muda = float
    if(18 <=  float(tabel_Umur[i]) and float(tabel_Umur[i]) < 21):
        Muda = 1
    elif(21 <= float(tabel_Umur[i]) and float(tabel_Umur[i]) <= 25):
        Muda = (25 -float(tabel_Umur[i]))/21
    elif(25 < float(tabel_Umur[i])):
        Muda = 0
    return Muda

def usiaMenengah(tabel_Umur):
    Menengah = float
    if(18 <=  float(tabel_Umur[i]) and float(tabel_Umur[i]) < 21):
        Menengah = 0
    elif(21 <= float(tabel_Umur[i]) and float(tabel_Umur[i]) <= 25):
        Menengah = (25 -float(tabel_Umur[i]))/21
    elif(25 < float(tabel_Umur[i]) and float(tabel_Umur[i]) <= 30):
        Menengah = (30 -float(tabel_Umur[i]))/25
    else:
        Menengah = 0
    return Menengah

def usiaTua(tabel_Umur):
    Tua = float
    if(18 <=  float(tabel_Umur[i]) and float(tabel_Umur[i]) < 21):
        Tua = 0
    elif(21 <= float(tabel_Umur[i]) and float(tabel_Umur[i]) <= 25):
        Tua = (25 -float(tabel_Umur[i]))/21
    elif(25 < float(tabel_Umur[i])):
        Tua = 1
    return Tua

Muda = []
Menengah = []
Tua = []

for i in range(len(tabel_Umur)):
    Muda.append(usiaMuda(tabel_Umur))
    Menengah.append(usiaMenengah(tabel_Umur))
    Tua.append(usiaTua(tabel_Umur))


#print(Muda)
#print(Menengah)
#print(Tua)

NK1 = pd.DataFrame(list(zip(tabel_NO,tabel_Nama,tinggi,sedang,rendah)), columns= ['No','Nama','Tinggi','Sedang','Rendah'])
NK2 = pd.DataFrame(list(zip(tabel_NO,tabel_Nama,Muda,Menengah,Tua)), columns= ['No','Nama','Muda','Menengah','Tua'])
#inferensi

Tinggi_Tinggi_Muda = list(zip(tinggi,Muda))
Tinggi_Sedang_Muda = list(zip(sedang,Muda))
Rendah_Rendah_Muda = list(zip(rendah,Muda))

Tinggi_Tinggi_Menengah = list(zip(tinggi,Menengah))
Rendah_Sedang_Menengah = list(zip(sedang,Menengah))
Rendah_Rendah_Menengah = list(zip(rendah,Menengah))

Tinggi_Tinggi_Tua = list(zip(tinggi,Tua))
Rendah_Sedang_Tua = list(zip(sedang,Tua))
Rendah_Rendah_Tua = list(zip(rendah,Tua))


#defuzzification 
Perkalian_New = 0
Pembagian_New = 0

for i in range(0,len(Tinggi_Tinggi_Muda)):
    perkalian = Tinggi_Tinggi_Muda[i][0] * Tinggi_Tinggi_Muda[i][1]
    pembagian = Tinggi_Tinggi_Muda[i][0]
    Perkalian_New = Perkalian_New + perkalian
    Pembagian_New = Pembagian_New + pembagian
z = Perkalian_New / Pembagian_New

print(z)
"""
for(a,b) in Hasil_dict:
    if key in Hasil_dict:
        Hasil_dict
"""
#Sort_NK1 = DataFrame.sort_values(NK1, ascending=['0'])

#print(NK1.head(10))
#print(NK2.head(10))
#NK2 = pd.DataFrame(list(zip(tabel_NO,tabel_Nama,Muda,Menengah,Tua)))
