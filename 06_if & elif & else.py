if True:
    print("Koşul doğru.")
    print("Halen if bloğunun içindeyiz.")

if False:
    print("Bu mesajı atlayacaktır.") # Yanlış olduğu için bu koşulu atlar.
else:
    print("Bu mesajı yazacaktır.") # Ve bu çıktıyı verir.

print("""
---------------------------------------------------------------
---------------------------------------------------------------""")

a = 5
b = 7
if a != b:
    print("a b'ye eşit değildir.")
print("--------------------------------------------------")

c = 6
d = 8
if c == d:
    print("c d'ye eşittir.")
else:
    print("c d'ye eşit değildir.")
print("--------------------------------------------------")

renk = "Siyah"
if renk == "Beyaz": # Eğer renk beyazsa:
    print("Beyaz")  # Beyaz çıktısını ver.
elif renk == "Sarı":# Beyaz değilse ve renk sarıysa:
    print("Sarı")   # Sarı çıktısını ver.
elif renk == "Mavi":# Beyaz ve sarı değilse ve renk maviyse:
    print("Mavi")   # Mavi çıktısını ver.
else:               # O bile değilse:
    print("Hiçbiri")# Hiçbiri çıktısını ver.
print("--------------------------------------------------")

e = 5
f = 8
g = 10
if e == f or g > e: # or bağlacında birinin doğru olması koşulu doğru yapar.
    print("Koşul doğru")
else:
    print("Koşul yanlış")
print("--------------------------------------------------")

if e < f and g > f: #and bağlacında koşulun doğru olması için her koşulun doğru olması şart.
    print("Koşul doğru")
else:
    print("Koşul yanlış")
print("--------------------------------------------------")

liste = [1,2,3,4,5,6,7,8,9]
s = 4
g = 0
isim = "Python"
deger = "o"
if s or g in liste:
    print("Listede var.")
else:
    print("Listede yok.")
print("--------------------------------------------------")

if deger in isim: # in bağlacıyla değerin var mı olduğunu sorgularız.
    print("Listede var.")
print("--------------------------------------------------")

if not deger in isim: # not ekleyerek yok mu olduğunu sorgularız.
    print("Listede yok")
else:
    print("Listede var.")
print("--------------------------------------------------")

# is anahtar kelimesi (Hafızada aynı nesne olmalı.)
h = "python"
k = "pytho"
k += "n"

print(h)
print(k)

if h == k:
    print("h = k")
else:
    print("h != k")

if h is k: # is bağlacı == aksine, "hafızada" değerlerin eşit mi olduklarını sorgular.
    print("h = k")
else:
    print("h != k")
