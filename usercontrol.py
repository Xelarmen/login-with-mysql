# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(host="$$$",user="$$$",passwd="$$$",database="$$$",)
mycursor = mydb.cursor()

a = input("1) Kaydol\n2) Giriş Yap\n")

if a == str(1):
    while 1:
        kullanici = input("Kullanıcı Adınız (Min 5 Karakter Girin)\n")
        sifre = input("Sifreniz(Min 6 Karakter Girin) \n")
        sifre2 = input("Sifrenizi Tekrarlayın \n")
        kullanicisql= "SELECT COUNT(firstcolumnname) FROM `secondcolumnname` WHERE `firstcolumnname`='"+kullanici+"'"
        mycursor.execute(kullanicisql)
        kullanicisorgu = mycursor.fetchall() #[(kayitsayisi,)] verikümesi
        if [(0,)]== kullanicisorgu:
            if sifre==sifre2:
                if len(sifre)>= 6 and len(kullanici)>=5:
                    sql = "INSERT INTO `tablename`(`firstcolumnname`, `sifre`) VALUES ('"+kullanici +"','"+sifre+"')"
                    mycursor.execute(sql)
                    print("Kayıt başarılı. Giriş Yapabilirsiniz!\n")
                    break
                elif len(sifre)<=6 or len(kullanici)<=5:
                    print("Kullanıcı Adınız veya Şifreniz için yetersiz karakter!\n")
            elif sifre!=sifre2:
                print("Şifreler uyuşmuyor Tekrar deneyin!")
        if [(0,)] != kullanicisorgu:
            print("Kullanıcı Adınız Kullanılmaktadır!")

elif a == str(2):
    while 1:
        kullanici= input("Kullanıcı Adınız \n")
        sifre= input("Sifreniz \n")
        sql ="SELECT `secondcolumnname` FROM `tablename` WHERE `firstcolumnname`= '"+kullanici+"' "
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult[0]==(sifre,):#veritabanı return olarak verikümesi döndürür gelen veri [('sifre',)] seklinde olur
            print("Sisteme Giriş Yapıldı")
            break
        elif myresult[0]!=(sifre,):
            print("Basarısız")

else :
    print("Yanlış Seçim!\n")
