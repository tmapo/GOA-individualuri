###homework 1
#მომხმარებელს შეჰყავს რიცხვი n. დაწერე პროგრამა, რომელიც while ციკლით გამოთვლის რიცხვების ჯამს 1-იდან n-ის ჩათვლით.

###old

# n = int(input("enter a number : "))
# num = 1
# jami = 0

# while num < n:
#     jami += num
#     num += 1

# print(jami)


###new
# n = int(input("enter a number : "))
# num = 1
# jami = 0

# for i in range(n):
#     jami += i

# print(jami)

###homework 2
# რიცხვების უკუღმა დაბეჭდვა: 
# მომხმარებელი შევა რიცხვს n. დაბეჭდე რიცხვები n-იდან 1-მდე while ციკლით.

###old
# n = int(input("enter a number : "))
 

# while n > 0:
#     n -= 1
#     print(n)

###new
# n = int(input("enter a number : "))
# lst = []

# for i in range(n):
#     lst.append(i)

# lst.reverse()

# for i in lst:
#     print(i)

###homework 3
# პაროლი სწორად სანამ არ შეიყვანს:
# დაწერე პროგრამა, რომელიც მოთხოვს მომხმარებელს პაროლის შეყვანას მანამ, სანამ არ შეიყვანს სწორ პაროლს "python123".

###old
# password = "python123"
# user_pass = input("enter your password : ")

# while password != user_pass:
#     print("incorrect password! try again.")
#     user_pass = input("enter your password : ")

# print("corrcet password!")

###new
# password = "python123"
# user_pass = input("enter your password : ")

# #for i in
# if user_pass != password:
#     print("incorrect password!try again.")
#     user_pass = input("enter your password : ")
# if user_pass == password:
#     print("corrcet password!")

###classwork 4

# რიცხვების დათვლა მანამ, სანამ 0 არ შეიყვანება
# მომხმარებელს შეჰყავს რიცხვები მანამ, სანამ 0 არ შეიყვანს. დათვალე რამდენი რიცხვი შეიყვანა მანამ, სანამ 0-ს მიაღწია.
# მაგალითად: შეიყვანე რიცხვი: 5  
# შეიყვანე რიცხვი: 3  
# შეიყვანე რიცხვი: -2  
# შეიყვანე რიცხვი: 0  
# შეტანილი რიცხვების რაოდენობა: 3

###old
# user_pass = input(" Enter your number : ")
# pass_num = "0"
# attempt_counter = 0

# while pass_num != user_pass:
#     print("Incorrect number! Try again.")
#     user_pass = input(" Enter your number : ")
#     attempt_counter += 1

# print("Correct number! You've entered the wrong number " , attempt_counter , " times!")

###new
# user_pass = input(" Enter your number : ")
# pass_num = "0"
# attempt_counter = 0

# for i in 
#     if pass_num != user_pass:
#         print("Incorrect number! Try again.")
#         user_pass = input(" Enter your number : ")
#         attempt_counter += 1
#     if pass_num == user_pass:
#         print("Correct number! You've entered the wrong number " , attempt_counter , " times!")


###homework 5

# რიცხვების საშუალო
# შეიყვანე რიცხვები მანამ, სანამ -1 არ შეიყვანება. ბოლოს გამოიტანე ამ რიცხვების საშუალო.

###old
# user_pass = int(input("Enter your number : "))
# pass_num = -1
# avg_num1 = 0
# attempt_counter = 0

# while user_pass != pass_num:
#     print("Incorrect number! Try again.")
#     attempt_counter += 1
#     avg_num1 += user_pass
#     user_pass = int(input("Enter your number : "))

# avg_num = avg_num1 / attempt_counter 


# print("Correct number! Avg.number of incorrect numbers you've entered : " , avg_num )

###new


    




