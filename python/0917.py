#1
x=int(input("���� ��: "))
y=int(input("������ ��: "))
z=int(input("���� ��: "))

tot = (x*2)+(y*4)+(z*4)

print("��ü �ٸ��� ��: %d"%(tot)

#2
price = int(input("��ǰ�� ������? "))
num = int(input("��ǰ�� ������? "))
tax = int(input("����(%)��? "))
delivery = int(input("��۷��? "))

total = (price*num)+(price*num*tax*0.01)+delivery

print("��ü ���� = %d"%(total)))

#3
tot= 52
unit = 3

a = tot//unit
b = tot%unit

print("������ ����: %d"%tot)
print("�� ����� ������ �ִ� ������ ����: %d"%unit)

print("\n�ִ� %d���� ������ �� �� �ְ� ���� ���ڴ� %d��"%(a,b))

#4
n=int(input("����="))
s= (n // 1000 + (n % 1000 - n % 100) // 100 + (n % 100 - n % 10) // 10 + n % 10)

print(s)
