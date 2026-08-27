demet = ("Sarı", "Lacivert", "Kırmızı", "Siyah")
print(type(demet)) # Normal parantez ile bir tuple(demet) oluşturduk.
print(len(demet)) # 4 elemanlı bir tuple.

print("""-------------------------------------------------""")

for a in demet:
    print(a)

print("""-------------------------------------------------""")

# Listeden farklı olarak tuplea (demete) bir eleman ekleyemeyiz, çıkaramayız veya değiştiremeyiz.

# Set (küme) nedir ve nasıl tanımlanır
# Setleri yazdırma
# Setlere eleman ekleme - silme
# remove - discard metotları

kume = {"Sarı", "Lacivert", "Kırmızı", "Yeşil"}
print(type(kume)) # Küme parantezleri ile bir set(küme) oluşturduk.
print(len(kume)) # 4 elemanlı bir set.

for a in kume:
    print(a) # Gariptir ki sırası sürekli random değişiyor. Kümenin olayı budur.
print("""-------------------------------------------------""")

print(kume)
kume.add("Lila") # .add kümeye eleman ekler.
print(kume)
kume.remove("Sarı")
print(kume) # .remove kümeden eleman siler.
kume.discard("Gri") # Olmayan bir elemanı .remove ile silmeye çalışırsak hata alırız.
                    # Hata almamak için .discard komutunu kullanırız.
print("""-------------------------------------------------""")

# Kümelerde kesişim & birleşim işlemi
# Kümelerde fark işlemi
# in anahtar kelimesi

kume1 = {"Sarı", "Mavi", "Yeşil", "Kırmızı", "Siyah"}
kume2 = {"Sarı", "Mavi", "Yeşil", "Lila", "Lacivert"}

print(kume1.intersection(kume2)) # .intersection ile kesişim işlemi uygularız.
print(kume1.union(kume2)) # .union ile birleşim işlemi uygularız.
print(kume1.difference(kume2)) # .difference ile fark işlemi uygularız. (kume1'de olup kume2'de olmayanlar.)
print(kume2.difference(kume1)) # .difference ile fark işlemi uygularız. (kume2'de olup kume1'de olmayanlar.)
print("Sarı" in kume1) # Sarı elemanı kume1'de var mı? diye sorarız.
print("Lila" in kume1) # Lila elemanı kume1'de var mı? diye sorarız.
print("Beyaz" in kume1.union(kume2)) # Beyaz elemanı kume1 ile kume2'nin birleşiminde var mı? diye sorarız.
print("""-------------------------------------------------""")

bosliste1 = [] # Boş bir liste yaparız. 
bosliste2 = list() # Boş bir liste yaparız.

bosdemet1 = () # Boş bir tupple(demet) yaparız.
bosdemet2 = tuple() # Boş bir tupple(demet) yaparız.

boskume1 = {} # Maalesef ki boş bir küme oluşturmaz. 'dict' oluşturur. (dict = sözlük)
boskume2 = set() # Boş bir set(küme) oluşturur.

print(type(boskume1))
print("""-------------------------------------------------""")

python = set("PYTHON") # set içine girdiğimiz elemanları kümeye çevirir.
print(python)








