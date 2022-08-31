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

cal1 = Calculator() # 클래스의 객체는 각각의 역할을 수행한다. 다른 결괏값과 상관없이 독립적인 값을 유지
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4)) # 이전에 계산한 결괏값을 유지
print(cal2.sub(5))
print(cal2.sub(7))