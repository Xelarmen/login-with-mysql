# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(host="185.210.95.31", user="abdulka2", passwd="A.kadir23",database="abdulka2_smssender", )
mycursor = mydb.cursor()

def register(kadi,sifre,sifre2):
    kullanicisql = "SELECT COUNT(kadi) FROM `user` WHERE `kadi`='" + kadi + "'"
    mycursor.execute(kullanicisql)
    kullanicisorgu = mycursor.fetchall()  # [(kayitsayisi,)] verikümesi

    if [(0,)] == kullanicisorgu:
        if sifre == sifre2:
            if len(sifre) >= 6 and len(kadi) >= 5:
                sql = "INSERT INTO `user`(`kadi`, `sifre`) VALUES ('" + kadi + "','" + sifre + "')"
                mycursor.execute(sql)
                print("Kayıt başarılı. Giriş Yapabilirsiniz!\n")
            elif len(sifre) <= 6 or len(kadi) <= 5:
                print("Kullanıcı Adınız veya Şifreniz için yetersiz karakter!\n")
        elif sifre != sifre2:
            print("Şifreler uyuşmuyor Tekrar deneyin!\n")
    if [(0,)] != kullanicisorgu:
        print("Kullanıcı Adınız Kullanılmaktadır!\n")
def login(kadi,sifre):
    sql = "SELECT `sifre` FROM `user` WHERE `kadi`= '" + kadi + "' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult[0] == (sifre,):  # veritabanı return olarak verikümesi döndürür gelen veri [('sifre',)] seklinde olur
        print("Sisteme Giriş Yapıldı")
    elif myresult[0] != (sifre,):
        print("Basarısız")


a = input("1) Kaydol\n2) Giriş Yap\n")

if a == str(1):
        kullanici = input("Kullanıcı Adınız (Min 5 Karakter Girin)\n")
        sifre = input("Sifreniz(Min 6 Karakter Girin) \n")
        sifre2 = input("Sifrenizi Tekrarlayın \n")
        register(kullanici,sifre,sifre2)

elif a == str(2):

        kullanici= input("Kullanıcı Adınız \n")
        sifre= input("Sifreniz \n")
        login(kullanici,sifre)

else :
    print("Yanlış Seçim!\n")

