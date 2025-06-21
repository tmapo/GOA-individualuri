#1)შექმენი ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
#  გადაუარე ამ სიას while ციკლით და ჩაამატე გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნე ეს სია.  
def vashli(numbers):
    num = 0
    result = []
    while num < len(numbers):
        double = numbers[num] * 2
        result.append(double)
        num += 1
    print(result)
        

numbers = [12 , 28 , 32 , 95 , 10]
vashli(numbers)