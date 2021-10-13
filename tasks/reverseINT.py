# print(input('enter num : ')[::-1])

num = 12345
rev = 0

# while num != 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(rev)

for i in range(1,6):
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)

for i in range(0,9999999999):
    print('nc')
