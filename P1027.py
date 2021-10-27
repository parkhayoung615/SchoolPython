# 안뇽하세여 

x = 17
y = 20
t = x
x = y
y = t

print(x, y, t)

a = 7
b = 6
c = a * b
b = c - a
a = (c % b) + (c - b)
print (a)
print (b)
print (c)



height = input("키(cm)를 입력하세요")
weight = input("몸무게(kg)을 입력하세요")
height = int(height)
weight = int(weight)
bmi = (weight/(height*height)) * 10000

print ("체질량 지수 : ", bmi)




sum = 0
f = open("input.txt", "r")
lines = f.readlines()
for i in range(0, len(lines)):
    num = int(lines[i])
    print(num)
    sum = sum + num
print("합계", sum)
f.close()

f = open("output.txt", "a")
f.write("합계 : " + str(sum))
f.close()


pay = 14000
age = int(input("나이를 입력해주세요"))
if(age >= 60):
    print ("30% 할인 대상입니다.\n찜질방 이용 요금:{}원 ", format(pay*0.7))
elif (age <= 10):
    print("20% 할인 대상입니다.\n찜질방 이용 요금:{}", format(pay*0.8))
else:
    print("할인 대상이 아니다.\n찜질방 기본 이용 요금:14000")