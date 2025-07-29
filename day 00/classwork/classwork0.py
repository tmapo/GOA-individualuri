#classwork 1) გაქვს ლისტი სტრინგების, უნდა მიიღო 2 ლისტი ერთში უნდა ეწეროს სტრინგები რომლებიც თანხმონებით იწყება და მეორეში ისინი რომლებიც ხმოვნებით იწყება


# print(True or False) # true
# print(False or True) #true
# print(False and True) #false
# print(True and True) # true
# print(True or True) #true
# > metia
# <naklebia
# >= metia an tolia
# <= naklebia an tolia
# == shedareba(udris tu ara)
# != ar udris


# for i in range(1 , 101):
#     print(i)

# num = int(input("enter a number: "))

# if num % 2 == 1:
#     print("ეს რიცხვი კენტია")
# else :
#     print("ეს რიცხვი ლუწია")

# list = ["tevzi" , 34 , "arwivi" , "spilo" , 70]
# smth = input("enter something")

# print(5 > 2 or 3 < 2) # true
# print(3 == 2 or 3 != 2) #true


#              #true
# print( 17 == 19 or 5 + 6 == 11) 
# print( 15 != 8 or 89 == 8)
# print( 47 >= 7 or 6 >= 6)
# print( 67 > 7 and 46 == 46)
# print( 78 != 9 and 9 != 78)
# print( 40 > 6 and 17 + 9 == 26)

# print("///")

#             #false
# print( 90 < 0 or 78 < 1)
# print( 6 == 8 or 5 + 5 == 0)
# print( 19 != 19 or 69 < 9)
# print( 89 >= 89 and 7 == 9)
# print( 26 + 6 == 18 and 7 == 7)
# print( 56 > 56 and 56 == 56)


# classwork 2) მომხმარებელს შემოაყვანინე რიცხვი 

# თუ ეს რიცხვი ლუწია და იყოფა 3 ზე დაიპრინტოს "რიცხვი ლუწია და იყოფა 3 ზე 

# თუ ეს რიცხვი ლუწია და იყოფა 5 ზე დაიპრინტოს "ეს რიცხვი ლუწია და იყოფა 5 ზე 

# თუ ეს რიცხვი არ არის ლუწი და იყოფა სამზე დაიპრინტოს "ეს რიცხვი კენტია და იყოფა 3 ზე"

# თუ ეს რიცხვი ლუწია და არ იყოფა არც 5 ზე და არც 3 ზე დაიპრინტოს "ეს რიცხვი ლუწია და არ იყოფა არც 5 ზე და არც 3 ზე

# თუ ეს რიცხვი არ არის ლუწი და იყოფა 5 ზე დაიპრინტოს "ეს რიცხვი არ არის ლუწი და იყოფა 5 ზე"

# თუ ეს რიცხვი არ არის ლუწი და არ იყოფა არც 5 ზე და 3 ზე არც დაიპრინტოს "ეს რიცხვი არ არის ლუწი და არ იყოფა 5 ზე და 3 ზე"

# num = int(input("ჩაწერეთ რიცხვი: "))

# if num % 2 == 0 and num % 3 == 0:
#     print("რიცხვი ლუწია და იყოფა 3-ზე")
# if num % 2 == 0 and num % 5 == 0:
#     print("რიცხვი ლუწია და იყოფა 3-ზე")
# if num % 2 == 1 and num % 3 == 0:
#     print("რიცხვი კენტია და იყოფა 3-ზე")
# if num % 2 == 0 and num % 5 == 1 and num % 3 == 1:
#     print("რიცხვი ლუწია და არ იყოფა არც 5-ზე და არც 3-ზე")
# if num % 2 == 1 and num % 5 == 0:
#     print("რიცხვი კენტია და იყოფა 5-ზე")
# if num % 2 == 1 and num % 5 == 1 and num % 3 == 1:
#     print("რიცხვი კენტია და არ იყოფა არც 5-ზე და არც 3-ზე")

# list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])
# print(list[5])
# print(list[6])
# print(list[7])

# print(list[-1])
# print(list[-2])
# print(list[-3])
# print(list[-4])
# print(list[-5])
# print(list[-6])
# print(list[-7])
# print(list[-8])

# lst1 = [1 , 2 , 3 , 4 , 5 , 6 ] #6
# lst2 = [5 , 3 , 2 , 27 , 8] #5
# lst3 = [18 , "saas" , 18 , "mmm"] #4
# lst4 = ["aaa" , "bbb" , "ccc"] #3

# print(len(lst1) + len(lst2) + len(lst3) + len(lst4))

# lst = list(("vashli" , "banani" , "marwyvi"))
# lst1 = list(("atami" , "vashlatama"))
# lst2 = list(("sazamtro" , "kivi"))
# lst3 = list(("mandarini" , "fortoxali"))

# print(lst)
# print(lst1)
# print(lst2)
# print(lst3)

# print( len(lst) + len(lst1) + len(lst2) + len(lst3) ) #9

# fruit1 = input("enter a fruit: ")
# fruit2 = input("enter a second fruit: ")
# fruit3 = input("enter a third fruit: ")
# fruit4 = input("enter a fourth fruit: ")

# lst = list((fruit1 , fruit2 , fruit3 , fruit4))
# print(lst)

lst1 = ["banani" , "vashli" , "atami" , "fortoxali" , "sazamtro"]
lst2 = ["datvi" , "mgeli" , "niangi" , "lomi"]
lst3 = ["arwivi" , "flamingo" , "qori"]

print(lst1[1 : 3])
print(lst2[0 : 3]) 
print(lst3[-3 : -1]) 
