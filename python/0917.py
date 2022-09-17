#1
x=int(input("닭의 수: "))
y=int(input("돼지의 수: "))
z=int(input("소의 수: "))

tot = (x*2)+(y*4)+(z*4)

print("전체 다리의 수: %d"%(tot)

#2
price = int(input("상품의 가격은? "))
num = int(input("상품의 개수는? "))
tax = int(input("세금(%)은? "))
delivery = int(input("배송료는? "))

total = (price*num)+(price*num*tax*0.01)+delivery

print("전체 가격 = %d"%(total)))

#3
tot= 52
unit = 3

a = tot//unit
b = tot%unit

print("과자의 개수: %d"%tot)
print("한 사람당 나누어 주는 과자의 개수: %d"%unit)

print("\n최대 %d명에게 나누어 줄 수 있고 남는 과자는 %d개"%(a,b))

#4
n=int(input("정수="))
s= (n // 1000 + (n % 1000 - n % 100) // 100 + (n % 100 - n % 10) // 10 + n % 10)

print(s)
