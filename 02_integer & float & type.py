sayi1 = 5
isim = "Eko"
sayi2 = 2.5
sayi3 = 3

print(type(sayi1)) # Bu bir değişkenin tipini yazdırır. int: integer yani tam sayı demektir.
print(type(sayi2)) # Bu bir değişkenin tipini yazdırır. float: ondalıklı sayı demektir.
print(type(isim)) # Bu bir değişkenin tipini yazdırır. str: string yani metin demektir.

print(sayi1)
print(sayi2)

# Matematiksel İşlemler
# Toplama +
# Çıkarma -
# Çarpma *
# Bölme /
# Tam Bölme //
# Üs Alma **
# Mutlak Değer abs()
# Mod Alma %
# Yuvarlama round() 

print(16//5) # Tam bölme işlemi yapar. 16'yı 5'e böler ve sonucu tam sayı olarak verir.
print(16/5) # Bölme işlemi yapar. 16'yı 5'e böler ve sonucu float olarak verir.
print(sayi1 ** sayi3) # ** ile üs alma işlemi yaparız. 5 üzeri 3
print(sayi1 * sayi3) # * ile çarpma işlemi yaparız. 5 çarpı 3
print(abs(-2)) # abs() ile mutlak değerini alırız. -2'nin mutlak değeri 2'dir.
print(abs(-2.16)) # abs() ile mutlak değerini alırız. -2.16'nın mutlak değeri 2.16'dır.
print(22/7) # 22'yi 7'ye böler ve sonucu float olarak verir.
pi = 22/7
print(round(pi)) # round() ile sayıyı yuvarlarız.
print(round(pi,2)) # round() ile sayıyı yuvarlarız. 2 ile virgülden sonra kaç basamak olacağını belirleriz.
print(3 * 5 + 6) # Matematikte işlem önceliği vardır. Önce çarpma ve bölme işlemleri yapılır, sonra toplama ve çıkarma işlemleri yapılır.
print(3 * (5 + 6)) # Parantez içindeki işlemler önce yapılır.
print(30 % 4) # % ile mod alma işlemi yaparız. 
              #30'u 4'e böler ve kalanı verir.

# Karşılaştırma Operatörleri
#Eşittir "=="
#Eşit Değildir "!="
#Büyüktür ">"
#Küçüktür "<"
#Büyük Eşittir ">="
#Küçük Eşittir "<="

print(3==3) # 3 eşit 3 mü? T/F
print(3==5) # 3 eşit 5 mi? T/F
print(3<6) # 3 6'dan küçük mü? T/F
print(3!=6) # 3 6'ya eşit değil mi? T/F

rakam1 = "100"
rakam2 = 100
rakam3 = int(rakam1)
print(rakam2==rakam3)

i=1
i -= 2 
print(i) 
