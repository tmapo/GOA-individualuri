###classwork 1
#მომხმარებელს შემოაატანინე რიცხვი და გაიგე 1 დან ამ რიცხვამდე რიცხვენის ნამრავლი 

# lmt = int(input("Enter a limit : "))
# i = 1
# jami = 1

# while i < lmt + 1:
#     jami *= i
#     i += 1

# print(jami)

###classwork 2
#მომხმარებელს შემოაატანინე რიცხვი და გაიგე 1 დან ამ რიცხვამდე ლუწი რიცხვენის ნამრავლი

# lmt = int(input("Enter a limit : "))
# i = 1
# jami = 1

# while i < lmt + 1:
#     if i % 2 == 0:
#        jami *= i
#     i += 1

# print(jami)

###classwork 3
#მომხმარებელს შემოაატანინე რიცხვი და გაიგე 1 დან ამ რიცხვამდე კენტი რიცხვენის ნამრავლი

# lmt = int(input("Enter a limit : "))
# i = 1
# jami = 1

# while i < lmt + 1:
#     if i % 2 != 0:
#        jami *= i
#     i += 1

# print(jami)

###classwork 4
#მომხმარებელს შეაყვანინე 5 რიცხვი და იპოვე მაქსიმუმი

# lst = []

# for i in range(5):
#     lst.append(int(input("Enter a number : ")))

# lst.sort()

# print("Highest number you've entered : " , lst[-1])

###classwork 5
# დაბეჭდე ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზეც და 5-ზეც

# num = 1

# while num <= 30 :
#     if num % 3 == 0 and num % 5 == 0 :
#         print(num)
#     num += 1

###classwork 6
#5 სიტყვიდან მოძებნე ყველაზე გრძელი

# lst = []

# for i in range(5):
#     lst.append(input("Enter a word : "))

# lst2 = []

# for i in lst :
#     lst2.append(int(len(i)))

# cvladi = lst2.index(max(lst2))

# print(lst[cvladi])

###classwork 7
#დაბეჭდე 1-დან 20-მდე რიცხვები და მიუწერე "ლუწია" ან "კენტია"

# num = 1
# while num <= 20:
#     if num % 2 == 0:
#         print(num , "ლუწია")
#     else:
#         print(num , "კენტია")
#     num += 1

###classwork 8
#დაბეჭდე მოცემული სიტყვის ყველა ასო ცალ-ცალკე

# word = input("Enter a word : ")
# i = 0
# while i < len(word):
#     print(word[i])
#     print("")
#     i += 1

###classwork 9
#მომხმარებლის შეყვანილი 5 რიცხვიდან დაბეჭდე მხოლოდ უარყოფითები

# lst = []

# for i in range(5):
#     lst.append(input("Enter a number : "))

# for i in lst:
#     if i[0] == "-":
#        print(i)

###classwork 10
#დაბეჭდე 5-ის ჯერადები 1-დან 50-მდე

# num = 1

# while num <= 50:
#     if num % 5 == 0:
#         print(num)
#     num += 1

###classwork 11
#დაბეჭდე სახელი იმდენჯერ, რამდენიც მის სიგრძეს შეესაბამება

# word = input("Enter a word : ")

# for i in range(len(word)):
#     print(word)

###classwork 12
#მომხმარებელს შეაყვანინე 5-ნიშნა რიცხვი და იპოვე მისი ციფრების ჯამი

# num = input("Enter a 5 letter long number : ")
# while len(num) != 5:
#     print("Length of the number you've entered isnt equal to 5!")
#     num = input("Try again : ")

# i = 0
# jami = 0

# for i in num : 
#     jami += int(i)

# print(jami)

###classwork 13
#შეიყვანე 5 სიტყვა და დაბეჭდე შებრუნებული ფორმით

# lst = []
# for i in range(5):
#     lst.append(input("Enter a word : "))

# for i in lst : 
   
#     print(i[::-1])
    
###classwork 14
# დაბეჭდე ასეთი პირამიდა:

# *
# **
# ***
# ****
# *****

# i = 1
# while i < 6:
#     print("*" * i)
#     i += 1

###classwork 15
# შეაყვანინე მომხმარებელს 5 სიტყვა და დაბეჭდე მხოლოდ ისინი, რომლებიც პალინდრომებია

# lst = []
# for i in range(5):
#     lst.append(input("Enter a word : "))

# for i in lst:
#     if i == i[::-1]:
#         print(i)

###classwork 16
#  დაბეჭდე პირამიდა უკუღმა

# *****
# ****
# ***
# **
# *

# i = 5
# while i > 0:
#     print("*" * i)
#     i -= 1
###classwork 17
#5 შეყვანილი რიცხვიდან ამოარჩიე მხოლოდ ისეთები, რომელთა ციფრების ჯამი ლუწია

# lst = []
# for i in range(5):
#     lst.append(input("Enter a number : "))

# for i in lst:
#     num = 0
#     jami = 0
#     while num < len(i):
#         jami += int(i[num])
#         num += 1
#     if jami % 2 == 0:
#         print(jami)