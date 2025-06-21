#  2)შექმენი ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
#  გადაუარეთ ამ სიას for ციკლი და ჩაამატე მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნე ეს სია. 

def luwi(numbers):
    numbers1 = []
    for i in numbers:
        if i % 2 == 0:
            numbers1.append(i)
    print(numbers1)

numbers = [10 , 92 , 74 , 2 , 9 , 3 , 5]
luwi(numbers)