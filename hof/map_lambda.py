n = map(lambda x: x + 1, (2, 3, 4))
print(list(n))




# def multiplication(a):
#     if a % 2 == 0:
#         return a
#     else:
#         return 'is not defined'
# n = map(multiplication, [1,3,4,5])
# print(list(n))



n = filter(lambda x: x % 2 == 0, [1, 2, 4, 5])
print(list(n))