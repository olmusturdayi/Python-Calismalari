mesaj = "Hello" #Değişken Eklendi. #ÖNEMLİ: 0. harf:B / 1. Harf O / 2. HARF V / ...
mesaj2 = "World" #Değişken2 Eklendi.
mesaj3 = "123456789"
mesaj4= "Merhaba"

mesaj = mesaj.upper() #mesaj değişkeninin harflerinin büyük olduğunu akılda tutturduk.

print("Merhaba Dünya")

print("""Merhaba

Dünya""") #3 Çift Tırnak Açıp Alt Satırlara Çıktı Çıkarma.

print("Merhaba\nDünya") # \n ile alt satıra geçme.

print("Merhaba\t\t\tDünya") # \t ile taba basıp boşluk yapma.

print(mesaj + " " + mesaj2) # değişkenlerin arasına kendimizce boşluk ekleme.

print(mesaj[0])  #Pythonda sayılar 0'dan başlar. Değişkenin kaçıncı harfini yazdırmak
                 #istiyorsak 0 dan başlamalıyız.

print(mesaj[-1]) #-1 Sonuncu harf oluyor.

print(mesaj[0:4:1]) #0. karakterle(dahil) 4. karakter(hariç) arasını yazdırır. 
                    #Son sayı varsayılan sayı olan zaten 1. 2 yaparsak 
                    #atlayarak yazar. 2 yazarsak 2 atlayarak yazar.

print(mesaj[1:4]) #1. karakterle(dahil) 4. karakter(hariç) arasını yazdırır.

print(mesaj3)
print(mesaj3[::2])
print(mesaj3[::3])
print(mesaj3[::-1]) #-1 tersten yazdırır. 
print(mesaj3[::-2])

print(mesaj.lower()) # Harfleri küçük yazdırdık.
print(mesaj.upper()) # Harfleri büyük yazdırdık.
print(mesaj.capitalize()) # İlk harfi büyük yazdırdık.

print(mesaj2.startswith("Wo")) #Soruyorum, mesaj2 de Wo ile başlıyor mu? Terminal de true diyor.
print(mesaj2.endswith("ld")) #Soruyorum, mesaj2 de ld ile bitiyor mu? Terminal de true diyor.
print(mesaj2.count("a")) # Soruyorum, mesaj2 de kaç tane a harfi var?
print(mesaj2.count("o")) # Soruyorum, mesaj2 de kaç tane o harfi var?
print(mesaj3.isdigit()) # isdigit: sadece rakam mı olduğunu sorar.
print(mesaj.isalpha()) # isalpha: sadece harf mi olduğunu sorar.
print(mesaj.isalnum()) # isalnum: harf veya rakam mı var onu sorar. Noktalama işareti gibi şeylerin 
                       # olmadığını teyit etmek için kullanılır.

print("Bu kelime " + str(len(mesaj)) + " harflidir.") #Kelimenin kaç harfli olduğunu söyler.
print("Bu iki kelime " + str(len(mesaj + mesaj2)) + " harflidir.") #İki kelimenin kaç harfli olduğunu söyler.

cümle = "Bu hayat çok güzel"

print(cümle.replace("güzel","berbat")) #replace: cümledeki kelimeleri değiştirmeye yarar.
print("Selam " * 10) # Selam yazısını 10'la çarpar ve yazar.

isim = "Eko"
yas = "20"

print("{} , {} yasindadir".format(isim,yas))

print(f"{isim} {yas} yasindadir.")