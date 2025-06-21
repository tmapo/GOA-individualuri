###classwork 1

# lst = []

# # xmovani = a __ tanxmovani = b

# list_ab = ["iwyeba xmovnit mtavrdeba tanxmovnit : "]
# list_ba = ["iwyeba tanxmovnit mtavrdeba xmovnit : "]
# list_bb = ["iwyeba tanxmovnit mtavrdeba tanxmovnit : "]
# list_aa = ["iwyeba xmovnit mtavrdeba xmovnit : "]



# for i in range(30):
#     lst.append(input("enter anything : "))

# for i in range(len(lst)):
#     if lst[i][0] == "a" or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
#         if lst[i][-1] != "a" and lst[i][-1] != "e" and lst[i][-1] != "i" and lst[i][-1] != "o" and lst[i][-1] != "u" and lst[i][-1] != "A" and lst[i][-1] != "E" and lst[i][-1] != "I" and lst[i][-1] != "O" and lst[i][-1] != "U":
#             list_ab.append(lst[i])
#     if lst[i][0] != "a" and lst[i][0] != "e" and lst[i][0] != "i" and lst[i][0] != "o" and lst[i][0] != "u" and lst[i][0] != "A" and lst[i][0] != "E" and lst[i][0] != "I" and lst[i][0] != "O" and lst[i][0] != "U":
#         if lst[i][-1] == "a" or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
#             list_ba.append(lst[i])
#     if lst[i][0] != "a" and lst[i][0] != "e" and lst[i][0] != "i" and lst[i][0] != "o" and lst[i][0] != "u" and lst[i][0] != "A" and lst[i][0] != "E" and lst[i][0] != "I" and lst[i][0] != "O" and lst[i][0] != "U":
#         if lst[i][-1] != "a" and lst[i][-1] != "e" and lst[i][-1] != "i" and lst[i][-1] != "o" and lst[i][-1] != "u" and lst[i][-1] != "A" and lst[i][-1] != "E" and lst[i][-1] != "I" and lst[i][-1] != "O" and lst[i][-1] != "U":
#             list_bb.append(lst[i])
#     if lst[i][0] == "a" or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
#         if lst[i][-1] == "a" or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
#             list_aa.append(lst[i])

# print(list_ab)
# print(list_ba)
# print(list_bb)
# print(list_aa)

###classwork 2

 # მომხმარებელს შემოაყვანინე 10 რიცხვი და გადაანაწილე 4 ლისტში 
 # თუ ეს რიცხვი იყოფა 5 ზე და არ იყოფა 7 ზე ჩაამატე პირველ ლისტში 
 # თუ ეს რიცხვი არ იყოფა 5 ზე და  იყოფა 7 ზე ჩაამატე მეორე ლისტში 
 # თუ ეს რიცხვი არ იყოფა 5 ზე და არ იყოფა 7 ზე ჩაამატე მესამე ლისტში 
 # თუ ეს რიცხვი იყოფა 5 ზე და  იყოფა 7 ზე ჩაამატე მეოთხე ლისტში 

# lst = []

# lst1 = ["iyofa 5-ze ar iyofa 7-ze : "]
# lst2 = ["ar iyofa 5-ze iyofa 7-ze : "]
# lst3 = ["ar iyofa 5-ze ar iyofa 7-ze : "]
# lst4 = ["iyofa 5-ze iyofa 7-ze : "]

# for i in range(5):
#     lst.append(int(input("enter a random number : ")))

# for i in range(len(lst)):
#     if lst[i] % 5 == 0 and lst[i] % 7 != 0:
#         lst1.append(lst[i])
#     if lst[i] % 5 != 0 and lst[i] % 7 == 0:
#         lst2.append(lst[i])
#     if lst[i] % 5 != 0 and lst[i] % 7 != 0:
#         lst3.append(lst[i])
#     if lst[i] % 5 == 0 and lst[i] % 7 == 0:
#         lst4.append(lst[i])

# print(lst1)
# print(lst2)
# print(lst3)
# print(lst4)
    

###classwork 3

#მომხმარებელს შემოაყვანინე 10 პაროლი შექმენი 2 ლისტი კარგი და ცუდი პაროლების კარგ პაროლებში ჩაამატე ის რომელიც 3 ზე მეტ ციფრს შეიცავს და დანარჩენები ცუდებში ჩაამატე

# lst = []
# lst_num = []

# lst_good = ["kargi parolebi : "]
# lst_bad = ["susti parolebi : "]
# num = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
# count = 0


# for i in range(10):
#     lst.append(input("enter your password : "))

# for i in lst:
#     for x in i:
#         for j in num:
#             if x == j:
#                 count += 1
#     if count <= 3:
#         lst_bad.append(i)
#         count = 0
#     else:
#         lst_good.append(i)
#         count = 0


     
# print(lst_good)
# print(lst_bad)

###classwork 4
 #მომხმარებელს შემოაყვანინე 10 პაროლი შექმენი 3 ლისტი კარგი,ცუდი და ძალიან კარგი.
 #ძალიან კარგ პაროლებში ჩაამატე ის რომელიც 3 ზე მეტ ციფრს შეიცავს და 3 ზე მეტ ხმოვანს
 #კარგ პაროლებში ჩაამატე ის რომელიც 3 ზე მეტ ციფრს შეიცავს ან 3 ზე მეტ ხმოვანს
 #ცუდ პაროლებში ჩაამატე ის რომელიც არც 3 ზე მეტ ციფრს შეიცავს და არც 3 ზე მეტ ხმოვანს


# lst = []

# lst_good = ["kargi parolebi : "]
# lst_bad = ["susti parolebi : "]
# lst__very_good = ["dzalian kargi parolebi : "]

# num = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
# xmovnebi = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U"]
# count = 0
# count1 = 0

# for i in range(5):
#     lst.append(input("enter your password : "))

# for i in lst:
#     for x in i:
#         for j in num:
#             if x == j:
#                 count += 1
#     if count > 3:
#         for k in xmovnebi:
#             if x == k:
#                 count1 += 1
#     if count1 > 3:
#         lst__very_good.append(i)
#         count1 = 0
#     if count1 < 3:
#         lst_good.append(i)
#         count = 0
#         count1 = 0 
#     if count < 3:
#         lst_bad.append(i)
    
# print(lst__very_good)
# print(lst_good)
# print(lst_bad)