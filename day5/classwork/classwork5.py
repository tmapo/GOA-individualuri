###classwork 1

# მომხმარებელს შემოატანინე 10 სტრინგი და გადაანაწილე 3 ლისტში მკაცრში, ჩვეულებრივში და კითხვითში. მკაცრ ლისტში დაამატე ისინი, რომელიც "!" მთავრდება, კითხვითში, რომელიც "?" მთავრდება და ყველა დანარჩენი ჩვეულებრივში ჩაამატე.

# lst = []
# lst_mkacri = ["mtavrdeba !-t"]
# lst_chveulebrivi  = ["mtavrdeba .-t an sxva..."]
# lst_kitxviti = ["mtavrdeba ?-t"]

# for i in range(10):
#     lst.append(input("enter anything : "))

# for i in lst:
#     if i[-1] == "!":
#         lst_mkacri.append(i)
#     if i[-1] == "?":
#         lst_kitxviti.append(i)
#     if i[-1] != "!" and i[-1] != "?":
#         lst_chveulebrivi.append(i)

# print(lst_mkacri)
# print(lst_kitxviti)
# print(lst_chveulebrivi)


###classwork 2

#classwork 2) მომხმარებელს შემოატანინე 10 სტრინგი და გადაანაწილე 6 ლისტში მკაცრში ხმოვნით, მკაცრში თანხმოვნით, ჩვეულებრივში ხმოვნით, ჩვეულებრივში თანხმოვნით, კითხვითში ხმოვნით და კითხვითში თანხმოვნით

# lst = []

# # A = xmovani B = tanxmovani
# lst_mkacri_a = ["iwyeba xmovnit mtavrdeba !-t"]
# lst_mkacri_b = ["iwyeba tanxmovnit mtavrdeba !-t"]

# lst_chveulebrivi_a = ["iwyeba xmovnit mtavrdeba .-t an sxva..."]
# lst_chveulebrivi_b  = ["iwyeba tanxmovnit mtavrdeba .-t an sxva..."]

# lst_kitxviti_a = ["iwyeba xmovnit mtavrdeba ?-t"]
# lst_kitxviti_b = ["iwyeba tanxmovnit mtavrdeba ?-t"]


# for i in range(6):
#     lst.append(input("enter anything : "))

# for i in lst:
#     if i[-1] == "!":
#         if i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u" or i[0] == "A" or i[0] == "E" or i[0] == "I" or i[0] == "O" or i[0] == "U":
#             lst_mkacri_a.append(i)
#     if i[-1] == "!":
#         if i[0] != "a" and i[0] != "e" and i[0] != "i" and i[0] != "o" and i[0] != "u" and i[0] != "A" and i[0] != "E" and i[0] != "I" and i[0] != "O" and i[0] != "U":
#             lst_mkacri_b.append(i)
#     if i[-1] == "?":
#         if i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u" or i[0] == "A" or i[0] == "E" or i[0] == "I" or i[0] == "O" or i[0] == "U":
#             lst_kitxviti_a.append(i)
#     if i[-1] == "?":
#         if i[0] != "a" and i[0] != "e" and i[0] != "i" and i[0] != "o" and i[0] != "u" and i[0] != "A" and i[0] != "E" and i[0] != "I" and i[0] != "O" and i[0] != "U":
#             lst_kitxviti_b.append(i)
#     if i[-1] != "?" and i[-1] != "!":
#         if i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u" or i[0] == "A" or i[0] == "E" or i[0] == "I" or i[0] == "O" or i[0] == "U":
#             lst_chveulebrivi_a.append(i)
#     if i[-1] != "?" and i[-1] != "!":
#         if i[0] != "a" and i[0] != "e" and i[0] != "i" and i[0] != "o" and i[0] != "u" and i[0] != "A" and i[0] != "E" and i[0] != "I" and i[0] != "O" and i[0] != "U":
#             lst_chveulebrivi_b.append(i)

          

# print(lst_mkacri_a)
# print(lst_mkacri_b)
# print(lst_kitxviti_a)
# print(lst_kitxviti_b)
# print(lst_chveulebrivi_a)
# print(lst_chveulebrivi_b)

### classwork 3 

# num = 0
# while  num < 6:
#     print(num)
#     num += 1

# ricxvi = 10
# while ricxvi >= 0:
#     ricxvi -= 1
#     print(ricxvi)

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 1

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 2

# num = -28
# while num + 28 <= 0:
#     print(num)
#     num -= 1

###classwork 4

# num = 0
# while  num < 6:
#     print(num)
#     num += 1
#     if num == 3:
#         break

# ricxvi = 10
# while ricxvi >= 0:
#     ricxvi -= 1
#     print(ricxvi)
#     if ricxvi <= 5:
#         break

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 1
#     if ricxvi >= 50:
#         break

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 2
#     if ricxvi == 80:
#         break

# num = -28
# while num + 28 <= 0:
#     print(num)
#     num -= 1
#     if num < 10:
#         break

###classwork 5

# num = 0
# while  num < 6:
#     print(num)
#     num += 1
#     if num == 4:
#         continue

# ricxvi = 10
# while ricxvi >= 0:
#     ricxvi -= 1
#     print(ricxvi)
#     if ricxvi== 5:
#         continue

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 1
#     if ricxvi == 99 or ricxvi == 2:
#         continue

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 2
#     if ricxvi == 72 or ricxvi == 45 or ricxvi == 13:
#         continue

# num = -28
# while num + 28 >= 0:
#     print(num)
#     num -= 1
#     if num == -28:
#         continue

### classwork 6

# num = 0
# while  num < 6:
#     print(num)
#     num += 1
# else:
#     print("num > 6")

# ricxvi = 10
# while ricxvi >= 0:
#     ricxvi -= 1
#     print(ricxvi)
# else:
#     print(" atami miyvars ")

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 1
# else:
#     print("ricxvi agar aris 0-ze meti")

# ricxvi = 100
# while ricxvi +1 > 0:
#     print(ricxvi)
#     ricxvi -= 2
# else:
#     print("!!!")

# num = -28
# while num + 28 >= 0:
#     print(num)
#     num -= 1
# else:
#     print("marto -28")

###classwork 7

#დაითვალე 1-იდან 10-ის ჩათვლით რიცხვების ჯამი while loop ის გამოყენებით

# num = 0
# num1 = 0

# while num < 11:
#     num += 1
#     num1 += num

# print(num1)

###classwork 8

#classwork 4) მომხმარებელს შემოიყვანე რიცხვები, სანამ მომხმარებელი არ შეიყვანს 0-ს

# num = int(input("enter a number : "))   

# while num != 0:
#     num = int(input("enter a number : "))   
# print("dasrulda")
        



    
