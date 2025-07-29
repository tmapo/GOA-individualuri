###classwork 1

# num = input("enter a number : ")
# jami = 0

# for i in num:
#     jami += int(i)


# print(jami)

###classwork2


# num1 = 1
# num2 = 1

# while num1 <= 5:
#     num2 *= num1
#     num1 += 1
    

# print(num2)

###classwork 3

# password = "stop"
# user_pass = input("enter your password : ")

# while password != user_pass:
#     print("Incorrect password! Try again.")
#     user_pass = input("enter your password : ")

# print("correct password!")

###classwork 4 

#classwork 5) მომხმარებელს უნდა გამოიცნოს რიცხვი, რომელიც დაფარულია whyle loop ით

# mstry_num = 7
# user_num = int(input("Guess the mistery num : "))

# while mstry_num != user_num:
#     user_num = int(input("Unlucky guess! try again : "))

# print("You guessed the mistery number!")

###classwork 5

# classwork 6) დაიბეჭდოს თითოეული ასო ცალკე ხაზზე (მხოლოდ while-ით)

# word = input("enter anything : ")
# i = 0

# while i < len(word):
#     print(word[i])
#     i += 1    

###classwork 6 

#classwork 7) დაიბეჭდოს 1-დან 50-მდე ყველა რიცხვი, რომელიც ერთდროულად იყოფა 5-ზეც და 2-ზეც whyle loop ის გამოყენებით

# num = 1

# while num <= 50:
#     if num % 5 == 0 and num % 2 == 0:
#         print(num)
#     num += 1 

###classwork 7

#classwork 😎 იპოვოს მინიმალური რიცხვი მომხმარებლის შეყვანილ რიცხვებს შორის (0 წყვეტს)

# user_num = int(input("enter a number : "))
# num = 0
# lst = []
# while user_num != 0:
#     lst.append(user_num)
#     user_num = int(input("enter a lower number : "))

# print("lowest number : 0")

# lst.sort()

# print("the lowest number you've entered before 0 : " , lst[0])

### classwork 8

#classwork 9)  დაითვალოს რამდენი სიტყვა შეიყვანა მომხმარებელმა სანამ დაწერს "exit"-ს

# user_word = input("enter anything : ")
# word = "exit"
# attempt_counter = 0


# while word != user_word:
#     attempt_counter += 1
#     user_word = input("enter anything : ")

# if attempt_counter == 1 :
#     time = "time"
# else:
#     time = "times"

# print("You've entered the wrong word" , attempt_counter , time)


