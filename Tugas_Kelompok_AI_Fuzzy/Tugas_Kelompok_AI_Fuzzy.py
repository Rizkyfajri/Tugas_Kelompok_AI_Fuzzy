from typing import Dict
from collections import defaultdict
import random 
import pandas as pd
import xlsxwriter as xw

#Buat table generator           || Sudah
#Isi table generator            || Sudah
#Buat random number generator   || Belum
#Buat Fuzzification             || Belum
#Buat Inference                 || Belum
#Buat Defuzzification           || Belum

workbook = xw.Workbook('masukan.xlsx')            #membuat file excel baru
worksheet = workbook.add_worksheet()            #menambahkan worksheet baru

tabel_NO = []
tabel_Nama = []
tabel_IPK = []
tabel_Gaji = []

masukan = int(input("masukan jumlah table       :")) #menerima input integer

for i in range(0,masukan):                      #memprosess hasil input untuk menambahkan tabel pada excel
    if(i<10):                                   #jika angka yang di input kurang dari 10 maka hasil output adalah tabel_0X
        tabel_NO.append("test")        #tabel_01 tabel_09
    else:                                       #jika tidak maka angka menjadi double digit setelah digit satu
        tabel_NO.append("Test")

for i in range(0,masukan):                      
    if(i<10):                                   
        tabel_Nama.append("test")        
    else:                                       
        tabel_Nama.append("Test")

for i in range(0,masukan):                      
    if(i<10):                                   
        tabel_IPK.append("test")        
    else:                                       
        tabel_IPK.append("Test")

for i in range(0,masukan):                      
    if(i<10):                                   
        tabel_Gaji.append("test")        
    else:                                       
        tabel_Gaji.append("Test")


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