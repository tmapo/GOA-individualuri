###classwork 1
#დაწერე ფუნქცია max_of_three(a, b, c), რომელიც დააბრუნებს სამ რიცხვს შორის უდიდესს.

# def stafilo(a , b , c):
#     max = a
#     if b > max :
#         max = b
#     if c > max :
#         max = c
#     print(max , "is the highest number.")

# stafilo(1 , 6 , 10)

###classwork 2
#აწერე ფუნქცია reverse_string(s), რომელიც მიიღებს სტრიქონს და დააბრუნებს მას შებრუნებულს.

# def stafilo(s):
#     num = len(s) - 1
#     str1 = ""
#     while num >= 0 :
#         str1 += s[num]
#         num -= 1
#     print(str1)

# stafilo("stafilo")

###classwork 3
#დაწერე ფუნქცია is_palindrome(word), რომელიც შეამოწმებს არის თუ არა გადაცემული სიტყვა პალინდრომი

# def stafilo(s):
#     num = len(s) - 1
#     str1 = ""
#     while num >= 0 :
#         str1 += s[num]
#         num -= 1
#     return str1

# def atami(s):
#     if stafilo(s) == s:
#         return "Aris palindromi"
#     else:
#         return "Ar aris palindromi"

# print(atami("ara"))
    
###classwork 4
#დაწერე ფუნქცია sum_even(numbers), რომელიც დააბრუნებს ლუწი რიცხვების ჯამს სიიდან.

# def vashli(num):
#     jami = 0
#     for i in num:
#         if i % 2 == 0:
#             jami += i
#     print(jami)

# lst1 = [10 , 9 , 17 , 20]
# vashli(lst1)
            
###classwork 5
#დაწერე ფუნქცია unique_elements(lst), რომელიც დააბრუნებს სიას უნიკალური ელემენტებით (დუბლიკატების გარეშე)

# def marwyvi(lst):
#     return list(set(lst))
# lst = [9 , 10 , 29 , 52 , 52 , 29]
# print(marwyvi(lst))

###classwork 6
#დაწერე ფუნქცია count_words(text), რომელიც დააბრუნებს სტრიქონში სიტყვების რაოდენობას.

# def mango(txt):
#     return len(txt.split())

# print(mango("gamarjoba chemi saxelia mrisxane mango"))

###classwork 7
#დაწერე ფუნქცია average(numbers), რომელიც მიიღებს რიცხვების სიას და დააბრუნებს მათ საშუალოს.

# def kombosto(num):
#     jami = 0
#     for i in num:
#         jami += i
#     print(num)
#     jami /= len(num)
#     print(jami)

# kombosto([5 , 5 , 5 , 5])

###classwork 8
#დაწერე ფუნქცია word_lengths(text), რომელიც დააბრუნებს სიას სიტყვების სიგრძეებით.
# მაგ.: "hello world" → [5, 5]

# def brokoli(txt):
#     lst1 = txt.split()
#     lst2 = []
#     for i in lst1:
#        lst2.append(len(i))
#     print(txt)
#     print(lst2)
    
        

# brokoli("gamarjoba chemi saxelia sevdiani brokoli")

###classwork 9
#დაწერე ფუნქცია longest_word(sentence), რომელიც დააბრუნებს სტრიქონში ყველაზე გრძელ სიტყვას.

def vashlatama(sentence):
    lst = sentence.split()
    word = ""
    for i in lst:
        if len(i) > len(word):
            word = i
    print(word)

vashlatama("me miyvars xeebi mtebi da futkris skebi")