from typing import Dict, Match
from collections import defaultdict
import random 
import pandas as pd
import xlsxwriter as xw
import itertools as itl
import string

#Buat table generator           || Sudah
#Isi table generator            || Sudah
#Buat random number generator   || Belum
#Buat Fuzzification             || Belum
#Buat Inference                 || Belum
#Buat Defuzzification           || Belum

workbook = xw.Workbook('masukan.xlsx')            #membuat file excel baru
worksheet = workbook.add_worksheet()            #menambahkan worksheet baru

#==================== list

random.seed(12345)
tabel_NO = []
tabel_Nama = []
tabel_IPK = []
tabel_Gaji = []

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
    n = random.randint(1,20)
    tabel_Gaji.append(n)


worksheet.write(0,0,"No")
worksheet.write(0,1,"Nama")
worksheet.write(0,2,"IPK")
worksheet.write(0,3,"Gaji")

for i in range(0,masukan):                  #berhasil membuat table n*n berisi
    worksheet.write(i+1, 0,tabel_NO[i])
    worksheet.write(i+1, 1,tabel_Nama[i])
    worksheet.write(i+1, 2,tabel_IPK[i])
    worksheet.write(i+1, 3,tabel_Gaji[i])

workbook.close()                                #menutup file yang sudah terisis