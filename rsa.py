print("RSA encoder/decoder by Rew.\n")
print("Menu. \n1) Encode number, use random RSA. 2) Encode number, use my RSA, which i input. 3) Decode my RSA")

menu = None
while (menu != 1) and (menu != 2) and (menu != 3):
    try: 
        menu = int(input("Enter 1 or 2 or 3: "))
    except:
        print("'1' or '2' or '3', blyat! Bye")
        exit()
print("\nOkay, nice, move on! \n")

if(menu == 1):
    print("Enter to integer number, which you want encode.")
    #num = None
    #while type(num) != int:
    #    try:
    #        num = int(input("Enter: "))
    #    except KeyboardInterrupt:
    #        exit()
    #    except:
    #        print("Что ты там ввёл нахрен, дебил?")
elif(menu == 2):
    n = int(input("Enter to n (p*q): "))
    # n - один из открытых ключей, представляет собой произведение двух случайных, целых,
    # (приблизительно одинаковых по размеру простых чисел p и q (например 29 и 31) Алисы).

    e = int(input("Enter to exponent 'e' (1<e<ф(n)): "))
    # e - экспонента, второй открытый ключ, подбирается так, чтобы он был
    # нечетным и не имел общих делителей с Ф(n), т.е. с  числом (p-1)*(q-1) не имел общих делителей.
    # Обычно просто берут любое простое число. Слишком малую экспоненту брать не рекомендуется, ослабит безопасность.

    try:
        num = int(input("Enter integer number, which you want to encode, 0-"+str(n-1)+": "))
        # Открытый текст, который мы будем шифровать. Представляет собой число в интервале от 0 до (n-1).
    except:
        print("Что ты там ввёл нахрен, дебил?")
        exit()

    cipher = (num**e)%n
    print("CipherText:\n", cipher)
else:
    print("Дописать потом")

# Дописать:
# декодер (3 пункт, находится в else)
# Рандомный генератор RSA (криптостойкий)

# По желанию:
# увеличить скорость новыми алгоритмами
# сделать ко всему проверки (снизит читаемость и вроде ненужно)
