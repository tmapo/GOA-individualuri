###classwork 1
# შექმენით სია, რომელსაც შეინახავთ ცვლადში სახელად friends. მაგ სიაში უნდა შეინახოთ მინიმუმ 5 მეგობრის სახელი. პირველ რიგში გამოიტანეთ თქვენი საუკეთესო მეგობრის სახელი ინდექსების დახმარებით. დაბეჭდეთ სია. შეცვლაეთ მე-3 ინდექსზე მყოფი სახელი ახალით და დაბეჭდეთ სია. საბოლოოდ დაბეჭდეთ მთლიანი სიის სიგრძე

# friends = ["giorgi" , "vaso" , "ioane" , "sandro" , "qima"]
# print(friends[3])

# print(len(friends))
#შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. გადაუარეთ ამ საის while loop-ის გამოყენებით. 
#გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი,
#საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი.

# numbers = [39 , 10 , 76 , 5 , 1 , 25 , 81 , 45 , 9 , 192]
# num = 0
# kenti = 0
# luwi = 0
# while num < len(numbers):
#     if numbers[num] % 2 == 0:
#         luwi += numbers[num]
#     else:
#         kenti += numbers[num]
#     num += 1

# if kenti > luwi:
#     print("kenti ricxvebis jami luwi ricxvebis jamze metia")
# else:
#     print("luwi ricxvebis jami kenti ricxvebis jamze metia")

###classwork 2
#შექმენით სია შემდგარი 5 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტებიშექმენით სია შემდგარი 5 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტები

lst = ["vashli" , "msxali" , "atami" , "marwyvi" , "kenkra"]
print(lst[2:4])