

sugar = int(input())
bag5 = sugar//5

if sugar % 5 == 0:
    print(bag5)
else:
    for i in range(bag5,-1,-1):
        global bag3
        if (sugar - 5*i)%3 == 0:
            bag3 = (sugar - 5*i)//3
            print(i+bag3)
            break
        else:
            bag3 = 0
if bag3 == 0:
    print("-1")     # 구현이 어려웠던 부분



################1차시도################
# n = int(input())
#
# if n >= 5 and n%5%3 == 0:
#     k = n//5
#     a = n%5
#     b = a//3
# elif n >= 5 and n%5%3 != 0 and n%3 ==0:
#     k = n//3
#     b = 0
# #elif
# else:
#     k = -1
#     b = 0
#
# print(k+b)