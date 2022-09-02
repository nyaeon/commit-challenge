pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
  print("택시를 타고 간다.") # 주머니에 돈이 있으면
elif card: # 주머니에 돈이 없고 카도가 있으면
  print("택시를 타고 간다.") 
else: # 주머니에 돈도 없고 카드가 없으면
  print("걸어 간다.")