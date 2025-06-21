#    3)შექმენი რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან.
#   გაიგე ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი.                        


numbers = [1 , 23 , 2 , 75 , 3 , 263 , 4 , 74 , 5 , 90]
min = numbers[0]
max = numbers[0]
for i in range(1 , len(numbers)):
    current = numbers[i]
    if current < min:
        min = current
    if current > max:
        max = current

total = max + min
print(min)
print(max)
print(total)