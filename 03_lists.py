renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
print(type(renkler))
print(renkler[0]) # İlk elemanı yazdırır
print(renkler[-1]) # Son elemanı yazdırır
print(renkler[1:4]) # 1. indexten 4. indexe kadar olan elemanları yazdırır  
print(len(renkler)) # Listenin uzunluğunu yazdırır

#append metodu : Listenin sonuna yeni eleman ekler.
#insert metodu : Listenin herhangi indexine yenş eleman ekler.
#remove metodu : Listeden bir elemanı siler.
#extend metodu : Listeye birden fazla eleman ekler.
#pop metodu : Listenin son elemanını siler.


renkler.append("Gri",) # Listenin sonuna yeni bir eleman ekler
print(renkler)

renkler.insert(2, "Mor") # Listenin 2. indexine yeni bir eleman ekler
print(renkler)

renkler.remove("Sarı") # Listeden bir elemanı siler
print(renkler)

renkler.extend(["Turuncu", "Pembe"]) # Listeye birden fazla eleman ekler
print(renkler)

renkler2 = ["Turkuaz", "Fildişi"] # Yeni liste değişkeni yaptık.
renkler.extend(renkler2) # Listeye yeni list ekledik.
print(renkler)

renkler.pop() # Listenin son elemanını siler
print(renkler)

silinen = renkler.pop() # Silinen elemana değişken verdik
print(silinen) # Silineni gösterdik.

renkler.reverse() #Listeyi ters çevirdik ve kaydettik.
print(renkler)

renkler.sort() # Alfabetik Sıraladık ve kaydettik
print(renkler)

renkler.reverse() # Ters çevirdik ve kaydettik.
print(renkler)

print(renkler)
liste = sorted(renkler) #Tek seferlik Alfabetik Sıraladık.
print(liste)
print(renkler)

print("""-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------""")

renkler3 = ["Pembe", "Lacivert", "Bordo", "Lila"]
sayilar = [1,2,99,4,3,7,8]

print(min(renkler3))
print(min(sayilar))
print(max(renkler3))
print(max(sayilar))
print(sum(sayilar)) # Sayılar listesindeki elemanların toplamını verir. İnteger olmalı.

print("-------------------------------------------")
for a in renkler: # Listeyi satır satır yazdırır.
    print(a)
print("-------------------------------------------")

print(list(enumerate(renkler3,start=1))) # Listeyi numaralandırarak yazdırır.
print("-------------------------------------------")

print("Siyah" in renkler3) # Siyah renkler3 listesinde var mı diye sorar.
print("Lila" in renkler3) # Lila renkler3 listesinde var mı diye sorar.
print("-------------------------------------------")

stringrenkler3 = " :) ".join(renkler3) # Renkler3 listesini string haline getirir 
print(stringrenkler3 + " Selam")
print(type(stringrenkler3))
print("-------------------------------------------")

print(stringrenkler3)
renkler2 = stringrenkler3.split(" :) ") #stringi listeye çevirir
print(renkler2)
print(type(renkler2))