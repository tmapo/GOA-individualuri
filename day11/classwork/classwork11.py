
###classwork 1
# #მომხმარებელს შემოაყვანინე საწყისი და საბოლოო რიცხვები და გაიგე საწყისიდან საბოლოომდე რიცხვების ჯამი ფუმქციით

# def vashli(min, max):
#     jami = 0
#     while min < max:
#         jami += min
#         min += 1
#     print(jami)

# min = int(input("Enter MIN number : "))
# max = int(input("Enter MAX number : "))

# vashli(min , max)

###classwork 2 
#მომხმარებელს შემოაყვანინე საწყისი და საბოლოო რიცხვები და გაიგე საწყისიდან საბოლოომდე რიცხვების ნამრავლი ფუნქციით

# def msxali(min , max):
#     namravli = 1
#     for i in range(min , max):
#         namravli *= i
#     print(namravli)
# min = int(input("Enter MIN number : "))
# max = int(input("Enter MAX number : "))

# msxali(min , max)

###classwork 3
#მომხმარებელს შემოაყვანინე საწყისი და საბოლოო რიცხვები და გაიგე საწყისიდან საბოლოომდე ლუწი რიცხვების ჯამი ფუნქციით

# def atami(min , max):
#     jami = 0
#     for i in range(min , max):
#         if i % 2 == 0:
#             jami += i
#     print(jami)

# min = int(input("Enter MIN number : "))
# max = int(input("Enter MAX number : "))

# atami(min , max)

###classwork 4
#მომხმარებელს შემოაყვანინე საწყისი და საბოლოო რიცხვები და გაიგე საწყისიდან საბოლოომდე კენტი რიცხვების ჯამი ფუნქციით

# def yurdzeni(min , max):
#     jami = 0
#     for i in range(min , max):
#         if i % 2 == 1:
#             jami += i
#     print(jami)

# min = int(input("Enter MIN number : "))
# max = int(input("Enter MAX number : "))

# yurdzeni(min , max)

###classwork 5
#მომხმარებელს შემოაყვანინე საწყისი და საბოლოო რიცხვები და გაიგე საწყისიდან საბოლოომდე ლუწი რიცხვების ნამრავლი ფუნქციით

# def kiwi(min , max):
#     namravli = 1
#     for i in range(min , max):
#         if i % 2 == 0:
#             namravli *= i
#     print(namravli)

# min = int(input("Enter MIN number : "))
# max = int(input("Enter MAX number : "))

# kiwi(min , max)

###classwork 6
#მომხმარებელს შემოაყვანინე საწყისი და საბოლოო რიცხვები და გაიგე საწყისიდან საბოლოომდე კენტი რიცხვების ნამრავლი ფუნქციით

# def marwyvi(min , max):
#     namravli = 1
#     for i in range(min , max):
#         if i % 2 == 1:
#             namravli *= i
#     print(namravli)

# min = int(input("Enter MIN number : "))
# max = int(input("Enter MAX number : "))

# marwyvi(min , max)

###classwork 7
# მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე რიცხვების ჯამი ფუნქციით

# def banani(num1 , num2):
#     jami = 0
#     if num1 < num2:
#         for i in range(num1 , num2):
#             jami += i
#     if num2 < num1:
#         for i in range(num2 , num1):
#             jami += i
#     print(jami)
            
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# banani(num1 , num2)

###classwork 8
#მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე რიცხვების ნამრავლი ფუნქციით

# def vashlatama(num1 , num2):
#     jami = 1
#     if num1 < num2:
#         for i in range(num1 , num2):
#             jami *= i
#     if num2 < num1:
#         for i in range(num2 , num1):
#             jami *= i
#     print(jami)
            
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# vashlatama(num1 , num2)

###classwork 9
#მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე ლუწი რიცხვების ნამრავლი ფუნქციით

# def qliavi(num1 , num2):
#     jami = 1
#     if num1 < num2:
#         for i in range(num1 , num2):
#             if i % 2 == 0:
#                 jami *= i
#     if num2 < num1:
#         for i in range(num2 , num1):
#             if i % 2 == 0:
#                 jami *= i
#     print(jami)
            
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# qliavi(num1 , num2)

###classwork 10
#მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე კენტი რიცხვების ჯამი ფუნქციით

# def gargari(num1 , num2):
#     jami = 1
#     if num1 < num2:
#         for i in range(num1 , num2):
#             if i % 2 == 1:
#                 jami += i
#     if num2 < num1:
#         for i in range(num2 , num1):
#             if i % 2 == 1:
#                 jami += i
#     print(jami)
            
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# gargari(num1 , num2)

###classwork 11
# მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე ლუწი რიცხვების ჯამი ფუნქციით

# def karalioki(num1 , num2):
#     jami = 0
#     if num1 > num2:
#         for i in range(num2 , num1):
#             if i % 2 == 0:
#                 jami += i
#     if num2 > num1:
#         for i in range(num1 , num2):
#             if i % 2 == 0:
#                 jami += i
#     print(jami)

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# karalioki(num1 , num2)

###classwork 12
#მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე კენტი რიცხვების ნამრავლი ფუნქციით

# def gargari(num1 , num2):
#     jami = 1
#     if num1 < num2:
#         for i in range(num1 , num2):
#             if i % 2 == 1:
#                 jami *= i
#     if num2 < num1:
#         for i in range(num2 , num1):
#             if i % 2 == 1:
#                 jami *= i
#     print(jami)
            
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# gargari(num1 , num2)
###classwork 13
# მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე ისეთი რიცხვების ჯამი, რომელიც იყოფა 5 ზე ფუნქციით

# def karalioki(num1 , num2):
#     jami = 0
#     if num1 > num2:
#         for i in range(num2 , num1):
#             if i % 5 == 0:
#                 jami += i
#     if num2 > num1:
#         for i in range(num1 , num2):
#             if i % 5 == 0:
#                 jami += i
#     print(jami)

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# karalioki(num1 , num2)

###classwork 14
# მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე ისეთი ლუწი რიცხვების ჯამი, რომელიც იყოფა 5 ზე ფუნქციით

# def karalioki(num1 , num2):
#     jami = 0
#     if num1 > num2:
#         for i in range(num2 , num1):
#             if i % 5 == 0 and i % 2 == 0:
#                 jami += i
#     if num2 > num1:
#         for i in range(num1 , num2):
#             if i % 5 == 0 and i % 2 == 0:
#                 jami += i
#     print(jami)

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# karalioki(num1 , num2)

###classwork 15
# მომხმარებელს შემოაყვანინე ორი რიცხვი, გაიგე რომელია უდიდესი და რომელი უმცირესი ამ ორი რიცხვიდან, შემდეგ კი გაიგე უმცირესიდან უდიდესამდე ისეთი ლუწი რიცხვების ჯამი, რომელიც იყოფა 3ზე და არის ლუწი ფუნქციით

def karalioki(num1 , num2):
    jami = 0
    if num1 > num2:
        for i in range(num2 , num1):
            if i % 3 == 0 and i % 2 == 0:
                jami += i
    if num2 > num1:
        for i in range(num1 , num2):
            if i % 3 == 0 and i % 2 == 0:
                jami += i
    print(jami)

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

karalioki(num1 , num2)
