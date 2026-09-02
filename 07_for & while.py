liste = [1,2,3,4,5,6]
for rakam in liste:
    print(rakam) # for ile bu şekilde elemanları alt alta yazdırabiliriz.
print("----------------------------------------------------------")

isim = "Ahmet"
for harf in isim:
    print(harf) # Stringlerde de aynı şeyi yapabiliriz.
print("----------------------------------------------------------")

demet = ("çiçek","gül","papatya",4)
for a in demet:
    print(a) # demetlerde de aynı şeyi yapabiliriz.
print("----------------------------------------------------------")

for i in range(0,10):
    print(i) # range ile sayıları alt alta yazdırabiliriz. range(başlangıç, bitiş)
print("----------------------------------------------------------")

for i in range(0,10,2):
    print(i) # range(başlangıç, bitiş, artış miktarı)
print("----------------------------------------------------------")

for i in range(10):
    print(i) # range(başlangıç, bitiş) başlangıç default olarak 0'dır.
print("----------------------------------------------------------")

sonuc = 1
for i in range(0,10):
    sonuc *= 2
print(sonuc) # Bu örnekte 2'nin 10. kuvvetini hesapladık.
print("----------------------------------------------------------")

liste1 = ["a","b","c"]
liste2 = [1,2,3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam) # Matematikteki küme çarpımı işlemi yaptık.
print("----------------------------------------------------------")

list = [1,2,3,4,5,6]
for i in list:
    if i == 3:
        print("3'ü atladık.")
        continue # Bu şekilde 3'ü atladık.
    print(i)
print("----------------------------------------------------------")

for i in list:
    if i == 3:
        break # Bu şekilde 3'te durduk.
    print(i)
print("----------------------------------------------------------")

listem = range(100)

for i in listem:
    if i %3 != 0: # Eğer sayımızın 3 ile bölümündek kalan 0 değilse:
        continue  # O sayıyı atla.
    if i == 81: # Eğer sayımız 81'e geldiyse:
        break # Dur.
    print(i) # Bu şekilde 0'dan 81'e kadar 3'ün katı sayıları yazdırdık.
print("----------------------------------------------------------")

x = 1

while x < 20: # x 20'den küçük olduğu sürece:
    print("x =",x) # x'i yazdır.
    x += 1 # x'e bir ekle.

# Bu şekilde 1 den 20'ye kadar sayıları yazdırdık.
print("----------------------------------------------------------")

i = 1
while True:
    print(i)
    i += 1
    if i == 100:
        break
print("----------------------------------------------------------")

while True:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
    if i == 1000:
        break
