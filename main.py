china = 350_000
dubai = 150_000
bali = 400_000

dist = input("Введите пунк поездки (china, dubai, bali): ")
count = int(input("Введите количество людей:  "))

if dist == "china":
    price = china * count
elif dist == "dubai":
    price = dubai * count
else:
    price = bali * count

print("Цена поездки: ", price)
