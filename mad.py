from random import randint
import datetime
import getpass
import sys

users = {"admin" : "123", "AC2311" : "Camels"}

date_now = datetime.date.today()

p4 = 0
p5 = 22
p6 = 47
p7 = 88
p8 = 90
p9 = 120
p10 = 144
p11 = 320
p12 = 648
p13 = 890
p14 = 360
p15 = 265
p16 = 102
p17 = 308
p18 = 357
p19 = 298
p20 = 100
p21 = 89
p22 = 77
p23 = 67

a4 = 0
a5 = 14
a6 = 34
a7 = 77
a8 = 80
a9 = 90
a10 = 140
a11 = 230
a12 = 700
a13 = 1030
a14 = 400
a15 = 320
a16 = 100
a17 = 450
a18 = 403
a19 = 303
a20 = 103
a21 = 103
a22 = 90
a23 = 44


def percent(a, b) : 
  
    result = int(((b - a) * 100) / a) 
  
    return result 

def login():
	user = input("Username: ")
	passw = getpass.getpass()

	if user in users:
		if passw == users[user]:
			return 1
		else:
			return "incorrect password"
	else:
		return "user not found"


def main():
	res = login()
	if res == 1:
		print("Sales Record")
		print("\nWeek {} \n{}".format(date_now.strftime("%V"), date_now.strftime("%d-%B-%Y")))
		sales()

	elif res != 1:
		print(res)

def sales():
	print("\nSales  \t\t Predic   Actual  Vari")
	print("04:00 - 05:00 \t {} \t {} \t {}%".format(p4, a4, 0))
	print("05:00 - 06:00 \t {} \t {} \t {}%".format(p5, a5, percent(p5, a5)))
	print("06:00 - 07:00 \t {} \t {} \t {}%".format(p6, a6, percent(p6, a6)))
	print("07:00 - 08:00 \t {} \t {} \t {}%".format(p7, a7, percent(p7, a7)))
	print("08:00 - 09:00 \t {} \t {} \t {}%".format(p8, a8, percent(p8, a8)))
	print("09:00 - 10:00 \t {} \t {} \t {}%".format(p9, a9, percent(p9, a9)))
	print("10:00 - 11:00 \t {} \t {} \t {}%".format(p10, a10, percent(p10, a10)))
	print("11:00 - 12:00 \t {} \t {} \t {}%".format(p11, a11, percent(p11, a11)))
	print("12:00 - 13:00 \t {} \t {} \t {}%".format(p12, a12, percent(p12, a12)))
	print("13:00 - 14:00 \t {} \t {} \t {}%".format(p13, a13, percent(p13, a13)))
	print("14:00 - 15:00 \t {} \t {} \t {}%".format(p14, a14, percent(p14, a14)))
	print("15:00 - 16:00 \t {} \t {} \t {}%".format(p15, a15, percent(p15, a15)))
	print("16:00 - 17:00 \t {} \t {} \t {}%".format(p16, a16, percent(p16, a16)))
	print("17:00 - 18:00 \t {} \t {} \t {}%".format(p17, a17, percent(p17, a17)))
	print("18:00 - 19:00 \t {} \t {} \t {}%".format(p18, a18, percent(p18, a18)))
	print("19:00 - 20:00 \t {} \t {} \t {}%".format(p19, a19, percent(p19, a19)))
	print("20:00 - 21:00 \t {} \t {} \t {}%".format(p20, a20, percent(p20, a20)))
	print("21:00 - 22:00 \t {} \t {} \t {}%".format(p21, a21, percent(p21, a21)))
	print("22:00 - 23:00 \t {} \t {} \t {}%".format(p22, a22, percent(p22, a22)))
	print("23:00 - 00:00 \t {} \t {} \t {}%".format(p23, a23, percent(p23, a23)))




main()