ticket = int(input('Введите кол-во билетов: '))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Введите возраст посетителя № {i}: "))
    if age < 18:
        price.append(0)
    elif 18 <= age < 25:
        price.append(990)
    elif age >= 25:
        price.append(1390)
print(price)
if ticket > 3:
    a = int(sum(price) - sum(price)/10)
    print("Сумма покупки ,с учетом 10% скидки:" , a,"руб." )
else:
    a = sum(price)
    print ("Cумма покупки: ", a,"руб.")
if ticket > 3:
     discount = int(sum(price)/10)
else:
    discount = int(0)
print("Ваша скидка составила:", discount, "руб")

print("Спасибо за покупку!")
