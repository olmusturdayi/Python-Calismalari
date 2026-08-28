# Sözlük
kisi = {"isim" : "ali" , "yas" : "20" , "cinsiyet" : "erkek" , "hobiler" : ["Satranç" , "Sinema"]}
# {x : y} şeklinde sözlük oluştururuz. ilk değer(x)(key) string veya integer olmalı.
# Ancak ikinci değer(y)(value) her şey olabilir. 

print(kisi["isim"])
print(kisi["yas"])
print(kisi["cinsiyet"])
print(kisi["hobiler"])

kisi["isim"] = "Ahmet" # Sözlükteki elemanı değiştirebiliriz.
print(kisi["isim"])

kisi.update({"isim":"Murat","yas":"40"}) # .update ile sözlükte birden çok elemanı değiştirebiliriz.
print(kisi)

kisi["id"] = 123456 #Sözlüğe yeni bir eleman ekleyebiliriz.
print(kisi)

kisi.update({"meslek":"mühendis"}) # .update ile de yeni bir eleman ekleyebiliriz.
print(kisi)

del kisi["meslek"] # del ile eleman silebiliriz.
print(kisi)

for a in kisi: # alt alta keyleri yazdı ama value'leri yazmadı.
    print(a)

for a in kisi: # Bu şekilde alt alta valueleri yazdırır.
    print(kisi[a])

print(kisi.keys()) # Bu şekilde key'leri yazdırır.
print(kisi.values()) # Bu şekilde value'leri yazdırır.
print(kisi.items()) # Bu şekilde hem key'leri hem de value'leri yazdırır.

for x in kisi.items(): # Bu şekilde alt alta hem keyleri hem valueleri yazdırır.
    print(x)

for x,y in kisi.items(): # Bu şekilde tırnak,parantez kullanmadan keyleri ve valueleri alt alta yazdırır.
    print(x,y)

# print(kisi["dogumtarihi"]) # sözlükte böyle key olmadığı için hata verir.
print(kisi.get("dogumtarihi")) # Hata vermemesi için .get kullanırız. Yoksa "none" çıktısını verir.
print(kisi.get("isim","bulunamadı"))
print(kisi.get("dogumtarihi","bulunamadı"))