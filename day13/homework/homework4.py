#   4) შექმენი ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია,
#   გადაურე ორივეს for ციკლით და გაიგე თითოეულ სიაში რიცხვების ჯამი(შეინახე ცალკე ცვლადებში),
#  გაამრავლე ორივე ერთმანეთზე და დააბრუნე.
def total(numbers , numbers1):
    total1 = 0
    total2 = 0
    for i in numbers:
        total1 += i
    for i in numbers1:
        total2 += i
    total = total1 * total2
    return total

numbers = [ 1 , 2 , 3]
numbers1 = [ 2 , 2 , 1]
print(total(numbers , numbers1))