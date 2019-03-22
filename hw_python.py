# # 연습문제 (리스트 내장함수)
list1 = ['Life', 'is', 'too', 'short']
print(" ".join(list1))

# # 연습문제 (if)

# 'shirt'

# # while 문 별찍기

num1 = 0
while num1 < 4:
    num1 += 1
    print(num1* '*')

# # 연습문제 (모음찾기)

word = 'mutzangesazachurum'
vowel = "aeiou"
count = 0

for a in word:
    if a in vowel:
        count += 1
print(count)

##############################################################

'''
과제 1
'''

# 1-1 while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요

sum3 = 0
num2 = 1

while num2 <= 1000:
    if num2 % 3 == 0:
        sum3 += num2
    num2 += 1
print(sum3)

# 1-2 while 문을 활용하여 아래같이 * 출력

num3 = 11

while num3 <= 11:
    num3 -= 1 
    print (num3 * '*')
    if num3 < 1:
        break

# 1-3 다음은 A학급 학생의  점수를 나타내는 리스트이다. 다음 리스트에서 50점이상의 점수들의 총 합을 구하시오

a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum_score = 0



while a:
    score = a.pop()
    if score > 50:
        sum_score += score
    else:
        pass
print(sum_score)

'''
과제 2 (for문)
'''

# 2-1 for 문을 활용해서 100까지 숫자 출력

a1 = 0

for a1 in range(100):
    print(a1 + 1)

# 2-2 for 문을 이용해 A학급의 평균 구하라

a2 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum_a = 0

for score in a2:
    sum_a += score 
print(sum_a / len(a2))

#2-3 리스트중에서 홀수에만 2를 곱하여 저장하는 코드가 있다. 다음 코드를 리스트 내포 (list comprehension) 을 이용해 표현하라

numbers = [1,2,3,4,5]

# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)



number_times_two = [n*2 for n in numbers if n % 2 == 1]

print(number_times_two)


