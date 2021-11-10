'''
point = 0;
sum = 0
while (sum < 20):
    point = int(input("다트점수를입력하세염"))
    print("점수는", point)
    sum += point
    
print("합계 점수는 ", sum)

=======================================
# 1부터 16까지 출력

for i in range(1, 16):
    print("i = ", i)
    
=======================================
# 홀수의 합

sum = 0
for i in range(1, 16):
    if (i % 2 != 0):
        sum += i
print ("합 = ", sum)

=======================================
# 짝수의 합

sum = 0
for i in range(1, 16):
    if (i % 2 != 1):
        sum += i
print ("합 = ", sum)

=======================================
# 이중 for문

for i in range(1, 6):
    for j in range(1, i+1):
        print("*" , end =" ")
    print()

========================================
# 배열
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    print("%d번 : %d" %(i+1, a[i]))
    print("%i%s : %i" %(i+1, "번", a[i]))
    print("{}번 : {}" .format(i+1, a[i]))