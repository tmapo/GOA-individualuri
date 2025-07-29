### classwork 1

# lst = ["16" , "87" , "aaagd" , "hsb" , 19 , 10 , 53]

# lst[0] = "17"
# lst[1] = "88"
# lst[2] = "aaagb"
# lst[3] = "hsd"
# lst[4] = 20
# lst[5] = 11
# lst[6] = 54

# print(lst)


# lst = ["16" , "87" , "aaagd" , "hsb" , 19 , 10 , 53]

# lst[-1] = 54
# lst[-2] = 11
# lst[-3] = 20
# lst[-4] = "hsa"
# lst[-5] = "aaagb"
# lst[-6] = "88"
# lst[-7] = "17"

# print(lst)



# lst = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 ]

# print(lst[2 : 5]) # 3 4 5 
# print(lst[1 : 6]) # 2 3 4 5 6
# print(lst[4 : 9]) # 5 6 7 8 9
# print(lst[0 : 10]) # 1 2 3 4 5 6 7 8 9 10
# print(lst[-8 : -2]) # 8 9 10 11 12 13
# print(lst[-13 : -10]) # 3 4 5 6
# print(lst[-15 : -9]) # 1 2 3 4 5 6
# print(lst[-3 : -1]) # 13 14



# lst = ["vashli" , "msxali" , "sazamtro" , "atami"]
# lst.insert(0 , "banani") # vashli -> banani
# lst.insert(1 , "fortoxali") # vashli -> fortoxali
# lst.insert(2 , "marwyvi") # vashli -> marwyvi
# lst.insert(3 , "kiwi") # vashli -> kiwi

# lst.append("avokado")
# lst.append("broweuli")
# lst.append("vashlatama")
# lst.append("qliavi")
# lst.append("mandarini")

# # lst = banani , fortoxali , marwyvi , kiwi , vashli , msxali , sazamtro , atami , avokado , broweuli , vashlatama , qliavi , mandarini

# lst1 = ["vashli gemrielia" , "msxali yvitelia" , "marwyvi lamazia"]
# lst3 = lst + lst1

# lst.extend(lst1)
# lst1.extend(lst)
# # lst = banani , fortoxali , marwyvi , kiwi , vashli , msxali , sazamtro , atami , avokado , broweuli , vashlatama , qliavi , mandarini , vashli gemrielia , msxali yvitelia , marwyvi lamazia

# lst.remove("banani")
# lst.remove("fortoxali")
# lst.remove("marwyvi")
# lst.remove("kiwi")
# lst.remove("vashli")

# lst.pop(0)
# lst.pop(1)
# lst.pop(2)
# lst.pop(3)
# lst.pop(4)




# print(lst3)
#print(lst)
# print(lst1)

# lst = ["vashli" , "msxali" , "sazamtro" , "atami"]

# for x in range(len(lst)):
#     print(lst[x])

# lst = [ 0 , 1 , 7 , 3 , 4 , 5 , 6 , 2]

# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i])
    
#output = 0 , 2 , 4 , 6

### classwork 2

# lst = [ 24 , 87 , 90 , 12 , 6 , 7]
# kenti = [ "kenti" ]
# luwi = [ "luwi" ]

# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         luwi.append(lst[i])
#     else:
#         kenti.append(lst[i])
# print(kenti)
# print(luwi)

### classwork3


lst = ["vashli" , "Msxali" , "Sazamtro" , "atami" , "Marwyvi" , "vashlatama" , "alubali"] 
xmovani = ["xmovani"]
tanxmovani = ["tanxmovani"]

for x in range(len(lst)):
    if lst[x][0] == "a":
        xmovani.append(lst[x])
    if lst[x][0] == "e":
        xmovani.append(lst[x])
    if lst[x][0] == "i":
        xmovani.append(lst[x])
    if lst[x][0] == "o":
        xmovani.append(lst[x])
    if lst[x][0] == "u":
        xmovani.append(lst[x])
    if lst[x][0] == "A":
        xmovani.append(lst[x])
    if lst[x][0] == "E":
        xmovani.append(lst[x])
    if lst[x][0] == "I":
        xmovani.append(lst[x])
    if lst[x][0] == "O":
        xmovani.append(lst[x])
    if lst[x][0] == "U":
        xmovani.append(lst[x])

    if lst[x][0] != "a":
        if lst[x][0] != "e":
            if lst[x][0] != "i":
                if lst[x][0] != "o":
                    if lst[x][0] != "u":
                        if lst[x][0] != "A":
                            if lst[x][0] != "E":
                                if lst[x][0] != "I":
                                    if lst[x][0] != "O":
                                        if lst[x][0] != "U":
                                            tanxmovani.append(lst[x])

print(xmovani)
print(tanxmovani)
    

    