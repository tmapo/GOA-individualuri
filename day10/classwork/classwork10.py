###classwork 1
#ამობეჭდე ციფრებით სამკუთხედი:

# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  

# for i in range(1, 5):
#     for k in range(1, i + 1):
#         print(k , end =  " ")
#     print()

###classwork 2
# შეამოწმე, არის თუ არა სია პალინდრომი ([1, 2, 3, 2, 1]) — ანუ წინიდან და უკუღმა ერთნაირი. გამოიყენე loop.

# lst = []
# num = int(input("Enter how many integers you want in the list : "))

# for i in range(num):
#     lst.append(int(input("Enter an integer : ")))

# lst2 = lst[::-1]

# if lst2 == lst:
#     print("This list is the same as it's reversed version. ")
# else:
#     print("This list isn't the same as it's reversed version. ")

###classwork 3
#მომხმარებელს შეჰყავს 10 რიცხვი — პროგრამამ უნდა დაბეჭდოს არითმეტიკულ საშუალოზე მაღალი რიცხვები

# lst = []

# for i in range(5):
#     lst.append(int(input("Enter an interger : ")))

# jami = 0

# for i in lst:
#     jami += i

# jami /= 5

# for i in lst:
#     if i > jami:
#         print(i)

###classwork 4
#სიის რიცხვებიდან შექმენი ახალი სია, რომელიც შეიცავს მხოლოდ უნიკალურ რიცხვებს

# lst1 = []

# for i in range(5):
#     lst1.append(int(input("Enter a number : ")))

# lst2 = set(lst1) 
# list(lst1)

# print(list(lst2))