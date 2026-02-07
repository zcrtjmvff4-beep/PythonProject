china = 350_000
dubai = 150_000
bali = 400_000

dist = input("Введите пунк поездки (china, dubai, bali): ")
adults = int(input("Введите количество взрослых:  "))
kids = int(input("Введите количество детей:  "))

if dist == "china":
    dist_price = china
elif dist == "dubai":
    dist_price = dubai
else:
    dist_price = bali


total =  dist_price * (2 * adults + kids) // 2
print("Цена поездки: ", total)
