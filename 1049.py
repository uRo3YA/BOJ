"""
    첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.
     둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
"""
n, m = map(int, input().split())

answer = 0
price_list = []

for _ in range(m):
    price = tuple(map(int, input().split()))
    price_list.append(price)

six_list = sorted(price_list, key=lambda x : x[0])
one_list = sorted(price_list, key=lambda x : x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    answer = six_list[0][0] * (n // 6) + one_list[0][1] * (n % 6)
    if six_list[0][0] < one_list[0][1] * (n % 6):
        answer = six_list[0][0] * (n//6 + 1)
else:
    answer = one_list[0][1] * n

print(answer)