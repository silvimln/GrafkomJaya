from tkinter import *
import math as mt
lvl_segitiga = int(input("masukkan level segitiga :"))

lebar = 500
tinggi = 500
window = Tk()
canvas = Canvas(window,width=lebar,height=tinggi)

#titik A = awal
x_center=lebar/2
y_center=lebar/2 -150
panjang_sisi_awal = 300

def cari_titik (x,y,panjang,sudut):
    x = panjang * mt.cos(mt.radians(sudut)) + x
    y = panjang * mt.sin(mt.radians(sudut)) + y
    return [x,y]

def gambar_rekursif(lvl_segitiga, titik, panjang_sisi, cnv, sudut=60, curlvl=1):
    x = 0
    y = 1
    
    temp_ttk = [titik]
    B = cari_titik(titik[x],titik[y],panjang_sisi,sudut)
    sudut += 120
    C = cari_titik(B[x],B[y],panjang_sisi,sudut)
    
    temp_ttk.append(B)
    temp_ttk.append(C)
    
    if lvl_segitiga == 1:
        canvas.create_line(temp_ttk[0][x],temp_ttk[0][y], temp_ttk[2][x],temp_ttk[2][y])
        canvas.create_line(temp_ttk[1][x],temp_ttk[1][y],temp_ttk[2][x],temp_ttk[2][y])
        canvas.create_line(temp_ttk[0][x],temp_ttk[0][y],temp_ttk[1][x],temp_ttk[1][y])
        return
    
    canvas.create_line(temp_ttk[0][x],temp_ttk[0][y], temp_ttk[2][x],temp_ttk[2][y])
    canvas.create_line(temp_ttk[1][x],temp_ttk[1][y],temp_ttk[2][x],temp_ttk[2][y])
    canvas.create_line(temp_ttk[0][x],temp_ttk[0][y],temp_ttk[1][x],temp_ttk[1][y])
    
    if curlvl < 2:
        A2 = cari_titik(temp_ttk[0][x],temp_ttk[0][y],panjang_sisi/3, sudut-120)
        cnv.create_text(A2[x],A2[y],text="A2")
        gambar_rekursif(lvl_segitiga,A2,panjang_sisi/3,cnv,sudut+180,curlvl+1)
        
        B2 = cari_titik(temp_ttk[1][x],temp_ttk[1][y],panjang_sisi/3, sudut)
        cnv.create_text(B2[x],B2[y],text="B2")
        gambar_rekursif(lvl_segitiga,B2,panjang_sisi/3,cnv,sudut-60,curlvl+1)
        
        C2 = cari_titik(temp_ttk[2][x],temp_ttk[2][y],panjang_sisi/3, sudut+120)
        cnv.create_text(C2[x],C2[y],text="C2")
        gambar_rekursif(lvl_segitiga,C2,panjang_sisi/3,cnv,sudut+60,curlvl+1)
        
    if 2<= curlvl <lvl_segitiga:
        A2 = cari_titik(temp_ttk[0][x],temp_ttk[0][y],panjang_sisi/3, sudut-120)
        gambar_rekursif(lvl_segitiga, A2, panjang_sisi/3,cnv,sudut+180,curlvl+1)
        
        B2 = cari_titik(temp_ttk[1][x],temp_ttk[1][y],panjang_sisi/3, sudut)
        gambar_rekursif(lvl_segitiga,B2,panjang_sisi/3,cnv,sudut-60,curlvl+1)

gambar_rekursif(lvl_segitiga, [x_center,y_center], panjang_sisi_awal, canvas)

canvas.pack()
canvas.mainloop()