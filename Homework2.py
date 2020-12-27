ad = input("Adınız nedir?")
soyad = input("Soyadınız nedir?")
yas = int(input("Yaşınız kaç?"))
dogumyili = int(input("Doğum yılınız nedir?"))

infos = [ad, soyad, yas, dogumyili]
print(infos)

for yas in infos :
    if infos[2] < 18:
        print("You can't go out because it's too dangerous") 
        break
else:
        print("You can go out the street")