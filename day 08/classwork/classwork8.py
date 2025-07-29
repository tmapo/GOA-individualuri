###classwork 1
# დაიბეჭდოს რიცხვები 1-დან 100-მდე, რომლებიც არის 7-ის ჯერადები while loop ით

# num = 0
# while num < 100:
#     if num % 7 == 0:
#         print(num)
#     num += 1

###classwork 2
# დაიბეჭდოს რიცხვებს 10–დან 1-მდე დაყოლება უკუსვლით while loop ით

# num = 10 

# while num > 0:
#     print(num)
#     num -= 1

###classwork 3
# დაითვალე 1-დან 100-მდე რიცხვების ჯამი, რომლებიც 3-ის ჯერადია და ლუწია while loop ით

# num = 0
# jami = 0

# while num < 100:
#     if num % 3 == 0:
#         jami += num
#     num += 1

# print(jami)

###classwork 4
# შეიყვანე ორი რიცხვი და დაბეჭდე მათი შორის ყველა რიცხვი, რომლებიც კენტია while loop ით

# min = int(input("enter min : "))
# max = int(input("enter max : "))

# while min < max :
#     if min % 2 != 0:
#         print(min)
#     min += 1

###classwork 5
# N-მდე დაბეჭდე ყოველი მესამე რიცხვი

# n = int(input("Enter the limit : "))
# num = 0
# while num < n :
#     print(num)
#     num += 3
    
###classwork 6
# შეიყვანე რიცხვი და დაბეჭდე მისი ციფრები ცალ-ცალკე while loop ით

# num = input("Enter a number : ")
# lenght = len(num)
# ind = 0

# while ind < lenght:
#     print(num[lenght - 1])
#     lenght -= 1

###classwork 7
# იპოვე ციფრების საშუალო არითმეტიკული (მაგ: 534 → (5+3+4)/3) while loop ით 

# num = input("Enter a number : ")
# lenght = len(num)
# ind = 0
# jami = 0

# while ind < lenght:
#     jami += int(num[ind])
#     ind += 1

# jami /= lenght
# print(jami)

###classwork 8
# დაიბეჭდოს ყველა რიცხვი 1-დან 100-მდე, რომლის ციფრების ჯამი მეტია 10-ზე   

num = 1

ind = 0
jami = 0
lst1 = []
lst_jami = []

#lst1-shi movaqciet yvela ricxvi 1-dan 100-mde
while num < 100:
    lst1.append(str(num))
    num += 1

#gamovitvalet lst1-shi myofi titoeuli elementis cifrta jami da chavamatet isini cal-calke lst_jami-shi
for i in lst1 :
    j = 0 
    for k in i:
        j += int(k)
    lst_jami.append(j)
    j = 0

#lst2-shi chavamatet yvela lst_jami-shi myofi is elementi romelic 10-ze metia
lst2 = []
for i in lst_jami:
    if i > 10:
        lst2.append(lst_jami.index(i))


#lst3-shi chavamatet yvela elementi lst1-dan romlis index-i lst2-shi myofi elementebis tolia
lst3 = []
for i in lst2 :
   lst3.append(lst1[i])

#lst3-shi avkrdzalet ganmeorebuli ricxvebi
cvladi1 = set(lst3)
cvladi2 = list(cvladi1)

print(cvladi2)