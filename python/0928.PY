#1

a = int(input("정수를 입력하세요 : "))
if a<0 :
    b=a*-1
else :
    b=a

print("%d 의 절대값은 %d" %(a,b))


#2

a = int(input("정수 1 : "))
b = int(input("정수 2 : "))
if a<b :
    max= b
else :
    max = a
    
print("\n\n정수 1 : %d과 정수 2 : %d 중에서 큰 값은 %d " %(a,b, max))    

#4

a = int(input("정수 : "))
if a > 0 :
    print("정수 %d는 양수이다"%a)
if a <= -1:
    print("정수 %d는 음수이다"%a)
else :
    print("정수 %d는 0이다"%a)

#5

a = int(input("정수 : "))
b = int(input("정수 : "))
c = int(input("정수 : "))
m=0

if a<b :
    if a< c :
        m=a
    elif c<b:
        m= c
elif b < c :
    m = b
else : m =c

print("%d,%d,%d 중에서 가장 작은 값은 %d"%(a,b,c,m))


#6
x = int(input("x값 : "))
y = int(input("y값 : "))

if x > 0 :
    if y > 0 :
        print("x값 :%d, y값:%d -> 1사분면"%(x,y))
    elif y < 0 :
        print("x값 :%d, y값:%d -> 4사분면"%(x,y))
elif x < 0 :
    if y > 0 :
        print("x값 :%d, y값:%d -> 2사분면"%(x,y))
    elif y < 0 :
        print("x값 : %d, y값:%d -> 3사분면"%(x,y))
else : print("사분면의 중심")



#7

humidity = int(input("습도(%) : "))
day = int(input("지속일수 : "))

if humidity <= 35 :
    if day >= 2 :
        print("습도 %d이하가 %d일 이상 -> 건조주의보 알림"%(humidity,day))
else : print("건조주의보 알림 없음")




#8

wind_speed1 = int(input("육상 풍속(m/h) : "))
wind_speed2 = int(input("순간풍속(m/s) : "))

if (wind_speed1 >= 14) or (wind_speed2 >= 20) :
    print("육상 풍속(m/h)이 %d이상 또는 순간풍속(m/s)%d이상 -> 강풍주의보 알림 %d"%(wind_speed1,wind_speed2))
else :
    print("강풍주의보 알림 없음")





#9

price = int(input("감자칩 가격 : "))
cnt = int(input("구입 갯수 : "))

money = price * cnt
if cnt >= 10 :
    money = money * 0.9
print("%d원짜리 감자칩 %d개 구입 -> 총 금액은 %d원"%(price,cnt,money))






#10

price = int(input("감자칩 가격 : "))
cnt = int(input("구입 갯수 : "))

money = price * cnt

if cnt >= 10 or cnt <= 19 :
    money = money * 0.9
elif cnt >= 20:
    money = money * 0.8
print("%d원짜리 감자칩 %d개 구입 -> 총 금액은 %d원"%(price,cnt,money))




#11

excel = int(input("엑셀 점수 : "))
access = int(input("엑세스 점수 : "))
s_um = excel * access
avg = s_um / 2

print("엑셀점수:%d점 엑세스점수:%d"%(excel,access))
print("총점%d 평균%0.2f점"%(s_um,avg))

if excel >= 50 and access >= 50 :
    if avg > 60 :
        print("합격")
    else :
        print("불합격")
else :
    print("결과 : 과락으로 불합격")
