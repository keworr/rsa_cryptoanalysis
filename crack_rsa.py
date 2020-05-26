import requests
import time
from math import ceil

def fermat(n,m):
	# Факторизация Ферма для чисел N < 10**307, т.к. выше проблематично взятие корня и лучше isqrt()
	start_time = time.time()
	t0=ceil(n**0.5)
	counter=0
	t=t0+counter
	temp=ceil(((t*t)-n)**0.5)
	while((temp*temp)!=((t*t)-n)) and ((time.time()-start_time)<m):
		counter+=1
		t=t0+counter
		temp=ceil(((t*t)-n)**0.5)
	s=temp
	p=t+s
	q=t-s
	if(p*q!=n):
		return 0,0
	return p,q #,time.time()-start_time (время для дебага)

def isqrt(n):
	x=n
	y=(x+n//x)//2
	while(y<x):
		x=y
		y=(x+n//x)//2
	return x

def fermat_big(n,m):
	# Факторизация Ферма для чисел N > 10**306
	start_time = time.time()
	t0=isqrt(n)+1
	counter=0
	t=t0+counter
	temp=isqrt((t*t)-n)
	while((temp*temp)!=((t*t)-n)) and ((time.time()-start_time)<m):
		counter+=1
		t=t0+counter
		temp=isqrt((t*t)-n)
	s=temp
	p=t+s
	q=t-s
	if(p*q!=n):
		return 0,0
	return p,q #,time.time()-start_time (время для дебага)

print("RSA cracker by Rew.\n")
print("""Выберите атаку на RSA.

1 - Факторизация модуля 'n'
2 - Факторизация Ферма, если 'p' и 'q' близкие числа
3 - Поиск разложения 'n' на factordb
4 - Атака Хастада, если имеется 3 и более экземпляров
5 - yaprof (свойство гомоформизма, 2 и более экземлпяров)
""")

menu = int(input("\nEnter: "))
if(menu == 1):
	print("\nФакторизация модуля 'n'\n")
	print("Пока не сделано, т.к. мне лень. Лучше поищи на factordb, это даже лучше")
#	n = int(input("Введите n (p*q): "))
#	m = int(input("Сколько минут будем факторизовывать?\n"))
#	if():
#	...
#	elif():
#	...
#	...

elif(menu == 2):
	print("\nФакторизация Ферма.\n")
	n = int(input("Введите n (p*q): "))
	m = int(input("Сколько минут будем факторизовывать?\n"))

	if(n<10*307):
		p,q=fermat(n,m*60)
	else:
		p,q=fermat_big(n,m*60)

	if(p!=0):
		print("p="+str(p)+"; q="+str(q))
	else:
		print("Не удалось факторизовать",n,"за",m,"минут")

elif(menu == 3):
	print("\nПоищем на factordb. Введите n: \n")

elif(menu == 4):
	print("\nАтака Хастада.\n")

elif(menu == 5):
	print("\nСвойство гомоморфизма\n")
# ...
else:
	print("...")


# Что надо дописать 
# 1) Парсер factordb
# Другие атаки
# Все алгоритмы факторизации для п. 1
