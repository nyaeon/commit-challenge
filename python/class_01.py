class Calculator:
  def __init__(self):
    self.result = 0
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

  def sub(self, num):
    self.result -= num
    return self.result

cal1 = Calculator() # Ŭ������ ��ü�� ������ ������ �����Ѵ�. �ٸ� �ᱣ���� ������� �������� ���� ����
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4)) # ������ ����� �ᱣ���� ����
print(cal2.sub(5))
print(cal2.sub(7))