###classwork 2

 # მომხმარებელს შემოაყვანინე 10 რიცხვი და გადაანაწილე 4 ლისტში 
 # თუ ეს რიცხვი იყოფა 5 ზე და არ იყოფა 7 ზე ჩაამატე პირველ ლისტში 
 # თუ ეს რიცხვი არ იყოფა 5 ზე და  იყოფა 7 ზე ჩაამატე მეორე ლისტში 
 # თუ ეს რიცხვი არ იყოფა 5 ზე და არ იყოფა 7 ზე ჩაამატე მესამე ლისტში 
 # თუ ეს რიცხვი იყოფა 5 ზე და  იყოფა 7 ზე ჩაამატე მეოთხე ლისტში 

# def vashli(lst , lst1 , lst2 , lst3 , lst4):
#     for i in lst:
#         if i % 5 == 0 and i % 7 != 0:
#             lst1.append(i)
#         if i % 5 != 0 and i % 7 == 0:
#             lst2.append(i)
#         if i % 5 != 0 and i % 7 != 0:
#             lst3.append(i)
#         if i % 5 == 0 and i % 7 == 0:
#             lst4.append(i)
#     print(lst1)
#     print(lst2)
#     print(lst3)
#     print(lst4)

# lst = [5 , 10 , 70 , 68 , 7 , 49 , 42 , 20]
# lst1 = ["iyofa 5-ze, ar iyofa 7-ze"]
# lst2 = ["iyofa 7-ze, ar iyofa 5-ze"]
# lst3 = ["ar iyofa arc 5-ze da arc 7-ze"]
# lst4 = ["iyofa 5-zec da 7-zec"]

# vashli(lst , lst1 , lst2 , lst3 , lst4)

###classwork 3

# მომხმარებელს შემოაყვანინე 10 პაროლი შექმენი 2 ლისტი კარგი 
# და ცუდი პაროლების კარგ პაროლებში ჩაამატე ის რომელიც 3 ზე მეტ ციფრს შეიცავს და დანარჩენები ცუდებში ჩაამატე

# def vashli(lst , lst_bad , lst_good): 
#     num = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
#     count = 0
#     for i in range(10):
#         lst.append(input("enter your password : "))
#     for i in lst:
#         for x in i:
#             for j in num:
#                 if x == j:
#                     count += 1
#         if count <= 3:
#             lst_bad.append(i)
#             count = 0
#         else:
#             lst_good.append(i)
#             count = 0
#     print(lst_good)
#     print(lst_bad)
# lst = []
# lst_bad = ["cudi parolebis listi : "]
# lst_good = ["kargi parolebis listi : "]
# vashli(lst , lst_bad , lst_good)

###classwork 4
 #მომხმარებელს შემოაყვანინე 10 პაროლი შექმენი 3 ლისტი კარგი,ცუდი და ძალიან კარგი.
 #ძალიან კარგ პაროლებში ჩაამატე ის რომელიც 3 ზე მეტ ციფრს შეიცავს და 3 ზე მეტ ხმოვანს
 #კარგ პაროლებში ჩაამატე ის რომელიც 3 ზე მეტ ციფრს შეიცავს ან 3 ზე მეტ ხმოვანს
 #ცუდ პაროლებში ჩაამატე ის რომელიც არც 3 ზე მეტ ციფრს შეიცავს და არც 3 ზე მეტ ხმოვანს

def vashli(lst , lst_bad , lst_good , lst_very_good): 
    num = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
    xmovnebi = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" ,"U"]
    count = 0
    count1 = 0
    for i in range(5):
        lst.append(input("enter your password : "))
    for i in lst:
        for x in i:
            for j in num:
                if x == j:
                    count += 1
            for k in xmovnebi:
                if x == k:
                    count1 += 1
        if count < 3 and count1 >= 3:
            lst_good.append(i)
            count = 0
            count1 = 0
        if count >= 3 and count1 < 3:
            lst_good.append(i)
            count = 0
            count1 = 0
        if count >= 3 and count1 >= 3:
            lst_very_good.append(i) 
            count = 0
            count1 = 0
        if count < 3 and count1 < 3:
            lst_bad.append(i)
            count = 0
            count1 = 0

    
    print(lst_good)
    print(lst_bad)
    print(lst_very_good)
lst = []
lst_bad = ["cudi parolebis listi : "]
lst_good = ["kargi parolebis listi : "]
lst_very_good = ["dzalian parolebis kargi listi : "]
vashli(lst , lst_bad , lst_good , lst_very_good)

#classwork 1) მომხმარებელს შემოაყვანინე 10 სტრინგი, და დააბრუნე 3 ლისტი თუ ამ სტრინგში ხმოვანი უფრო მეტია ვიდრე თანხმოვანი ჩაემატოს პირველ ლისტში, თუ თანხმოვანი მეტია, მეორეში და თუ ტოლია მესამეში 

# def vashli(lst , A_metia_B , B_metia_A , A_tolia_B):
#     xmovnebi = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" ,"U"]
#     count = 0
#     count1 = 0
#     for i in range(6):
#         lst.append(input("Enter anything : "))
#     for i in lst:
#         for k in i:
#             for x in xmovnebi:
#                 if x == k:
#                     count += 1
#                 if x != k:
#                     count1 += 1
#         if count > count1:
#             A_metia_B.append(i)
#             count = 0
#             count1 = 0
#         if count < count1:
#             B_metia_A.append(i)
#             count = 0
#             count1 = 0
#         if count == count1:
#             A_tolia_B.append(i)
#             count = 0
#             count1 = 0
#     print(A_metia_B)
#     print(A_tolia_B)
#     print(B_metia_A)

# lst = []
# A_metia_B = ["xmovnebi tanxmovnebze metia : "]
# A_tolia_B = ["xmovnebi da tanxmovnebi tolia : "]
# B_metia_A = ["tanxmovnebi xmovnebze metia : "]
# vashli(lst , A_metia_B , B_metia_A , A_tolia_B)
        
        
def count_digits(password):
    return sum(c.isdigit() for c in password)

def count_vowels(password):
    vowels = "aeiouAEIOUაეიოუ"
    return sum(c in vowels for c in password)


very_good = []
good = []
bad = []


for i in range(10):
    pw = input(f"{i+1}-ე პაროლი: ")
    digits = count_digits(pw)
    vowels = count_vowels(pw)

    if digits > 3 and vowels > 3:
        very_good.append(pw)
    elif digits > 3 or vowels > 3:
        good.append(pw)
    else:
        bad.append(pw)


print("\nძალიან კარგი პაროლები:", very_good)
print("კარგი პაროლები:", good)
print("ცუდი პაროლები:", bad)