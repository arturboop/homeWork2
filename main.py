# a = int(input("  введите число:"))
# b = int(input("  введите какую степинь хотите ввести:"))
#
# v = (a**b)
#
# print(v)





# a = int(input("введите число:"))
# b = int(input("введите второе число"))
# c = int(input("введите третье число:"))
# d = int(input("введите четвертое число:"))
#
#
#
# s= int(input("\n\n\nвведите какую степинь хотите ввести:"))
# v = (a**s)
# r = (b**s)
# e = (c**s)
# g = (d**s)
# print(v,r,e,g)


# def digit_count_and_sum(word):
#     digits = [int(char) for char in word if char.isdigit()]
#     count = len(digits)
#     total_sum = sum(digits)
#
#     print(f"Количество цифр: {count}")
#     print(f"Сумма цифр: {total_sum}")
#
#
# digit_count_and_sum(input("напишите предложение:"))





#
# def add_right(a, b):
#     e = str(a) + str(b)
#     print(e)
#
#
# add_right(1213, 412)
#



#
# def a_left(a,b):
#     e = str(b) + str(a)
#     print(e)
# a_left(123232,324)






# def work_with_list(a, b):
#     e = [x * b for x in a]
#     print(e)
#
#
# work_with_list([4, 3, 5, 7, 5, 45, 34, 3], 22)






# def big_sales(sales):
#     max_month = max(sales, key=sales.get)
#     return max_month
#
#
# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
#
# print(big_sales(sales))
#



# 12. min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang,
# min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang

# def min_max(numbers,max_num,min_num):
#     maximum=max(numbers)
#     minimum=min(numbers)
#
#     if maximum==max_num:
#         print(f"{max_num} son ro'yxatdagi eng katta son")
#     else:
#         print(f"{max_num} son ro'yxatdagi eng katta son emas")
#
#     if minimum==min_num:
#         print(f"{min_num} son ro'yxatdagi eng kichik son")
#     else:
#         print(f"{min_num} son ro'yxatdagi eng kichik son emas")
# numbers=[1,-9,41,36,0,9,0,13]
# katta=41
# kichik=0
# min_max(numbers,katta,kichik)


# 13. expensiveProduct(products) - funksiyadagi products - list.
# Unga products sifatida [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ] shunaqa qiymat beriladi.
# Eng qimmat telefon nomini print qilib bersin bu funksiya.
#
# def expensiveProduct(products):
#     max_price = max(product["price"] for product in products)
#     return max(product["name"] for product in products if product["price"] == max_price)
#
# products = [
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1100
#     },
# ]
#
# print(expensiveProduct(products))
#
#






