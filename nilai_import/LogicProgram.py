from models import *
import math
import csv

class Regresi :
    pass

    def __init__(self, nil, nil2, ber, ber2, nilber, n):
        self.nil = nil
        self.nil2 = nil2
        self.ber = ber
        self.ber2 = ber2
        self.nilber = nilber
        self.n = n


    def a(self):
        return ((self.nil * self.nil2) - (self.ber * self.nilber))/((self.n * self.ber2) - (self.ber**2))
    def b(self):
        return ((self.n * self.nilber) - (self.ber * self.nil))/((self.n * self.nil2) - (self.nil**2))
    def regresi(self, x):
        a = self.a()
        b = self.b()
        reg = a + (b * x)
        return reg

class Korelasi :

    def korelasi(self, nil, nil2, ber, ber2, nilber, n ) :
       return  ((n * nilber) - (nil * ber)) / (math.sqrt(((n * ber2) - ber ** 2) * ((n * nil2) - nil ** 2)))


class Hitung_Regresi_korelasi:

    def __init__(self, id):
        self.n = 0
        self.nil2 = 0
        self.nil = 0
        self.ber = 0
        self.ber2 = 0
        self.nilber = 0
        self.id = id
        #self.x = x

    def ambil_data(self):

        data = Import_Nilai.objects.filter(post_id = self.id)
        n = data.count()
        self.n = n

        for i in data :
            nil2p = i.nilai ** 2
            self.nil2 += nil2p  # y2
            self.nil += i.nilai  # y
            ber2p = i.berat ** 2
            self.ber2 += ber2p  # x2
            self.ber += i.berat  # x
            nilberp = i.berat * i.nilai
            self.nilber += nilberp  # xy

    def hitung(self):
        ObjRegresi = Regresi(self.nil, self.nil2, self.ber, self.ber2, self.nilber, self.n)
        ObjKorelasi = Korelasi()
        #Reg = ObjRegresi.regresi(self.x)
        Reg_a = ObjRegresi.a()
        Reg_b = ObjRegresi.b()
        Kor = ObjKorelasi.korelasi(self.nil, self.nil2, self.ber, self.ber2, self.nilber, self.n)
        return Reg_a, Reg_b, Kor


            


