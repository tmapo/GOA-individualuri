#დავალება: მომხმარებელს შემოაყვანინე 30 სტრინგი და დაამატე ლისტში. ამ ლისტიდან დააბრუნე ოთხი ლისტი სადაც პირველში მარტო ისეთი სტრინგები წერია რომელიც ხმოვნით იწყება და თანხმოვნით მთავრდება, მეორეში მარტო ისეთი სტრინგები წერია რომელიც თანხმოვნით  იწყება და ხმოვნით მთავრდება მესამეში მარტო ისინი რომელიც თანხმოვნით იწყება და თანხმოვნით მთავრდება და მეოთხეში მარტო ისინი რომელიც ხმოვნით იწყება და ხმოვნით მთავრდება

lst = ["list-:-"]

#xmovani = a __ tanxmovani = b

list_ab = ["A_B -:-"]
list_ba = ["B_A -:-"]
list_bb = ["B_B -:-"]
list_aa = ["A_A -:-"]


for i in range(30):
    lst.append(input("enter anything : "))


for i in range(len(lst)):
    if lst[i][0] == "a"  or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
        if lst[i][-1] != "a" and lst[i][-1] != "e" and lst[i][-1] != "i" and lst[i][-1] != "o" and lst[i][-1] != "u" and lst[i][-1] != "A" and lst[i][-1] != "E" and lst[i][-1] != "I" and lst[i][-1] != "O" and lst[i][-1] != "U":
            list_ab.append(i)
    if lst[i][0] != "a" and lst[i][0] != "e" and lst[i][0] != "i" and lst[i][0] != "o" and lst[i][0] != "u" and lst[i][0] != "A" and lst[i][0] != "E" and lst[i][0] != "I" and lst[i][0] != "O" and lst[i][0] != "U":
        if lst[i][-1] == "a"  or lst[i][-1] == "e" or lst[i][-1] == "i" or lst[i][-1] == "o" or lst[i][-1] == "u" or lst[i][-1] == "A" or lst[i][-1] == "E" or lst[i][-1] == "I" or lst[i][-1] == "O" or lst[i][-1] == "U":
            list_ba.append(i)
    if lst[i][0] != "a" and lst[i][0] != "e" and lst[i][0] != "i" and lst[i][0] != "o" and lst[i][0] != "u" and lst[i][0] != "A" and lst[i][0] != "E" and lst[i][0] != "I" and lst[i][0] != "O" and lst[i][0] != "U":
        if lst[i][-1] == "a"  or lst[i][-1] == "e" or lst[i][-1] == "i" or lst[i][-1] == "o" or lst[i][-1] == "u" or lst[i][-1] == "A" or lst[i][-1] == "E" or lst[i][-1] == "I" or lst[i][-1] == "O" or lst[i][-1] == "U":
            list_bb.append(i)
    if lst[i][0] == "a"  or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
        if lst[i][-1] == "a"  or lst[i][-1] == "e" or lst[i][-1] == "i" or lst[i][-1] == "o" or lst[i][-1] == "u" or lst[i][-1] == "A" or lst[i][-1] == "E" or lst[i][-1] == "I" or lst[i][-1] == "O" or lst[i][-1] == "U":
            list_aa.append(i)

print(list_ab)
print(list_ba)
print(list_bb)
print(list_aa)