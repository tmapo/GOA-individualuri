### classwork 1

# lst = ["vashli" , "Msxali" , "Sazamtro" , "atami" , "Marwyvi" , "vashlatama" , "alubali"] 
# xmovani = ["xmovani"]
# tanxmovani = ["tanxmovani"]

# for x in range(len(lst)):
#     if lst[x][0] == "a"  or lst[x][0] == "e" or lst[x][0] == "i" or lst[x][0] == "o" or lst[x][0] == "u" or lst[x][0] == "A" or lst[x][0] == "E" or lst[x][0] == "I" or lst[x][0] == "O" or lst[x][0] == "U":
#         xmovani.append(lst[x])
#     if lst[x][0] != "a" and lst[x][0] != "e" and lst[x][0] != "i" and lst[x][0] != "o" and lst[x][0] != "u" and lst[x][0] != "A" and lst[x][0] != "E" and lst[x][0] != "I" and lst[x][0] != "O" and lst[x][0] != "U":
#         tanxmovani.append(lst[x])

# print(xmovani)
# print(tanxmovani)

### classwork 2


# lst = []
# list_Aa = ["list_Aa"]
# list_Bb = ["list_Bb"]
# list_none = ["no A no B"]


# for i in range(10):
#     lst.append(input("enter anything:"))

# for x in range(len(lst)):
#     if lst[x][0] == "a" or lst[x][0] == "A":
#         if lst[x][-1] == "a" or lst[x][-1] == "A":
#             list_Aa.append(lst[x])
#     if lst[x][0] == "b" or lst[x][0] == "B": 
#         if lst[x][-1] == "b" or lst[x][-1] == "B":
#             list_Bb.append(lst[x])
#     if  lst[x][-1] != "a" and lst[x][-1] != "A" and lst[x][-1] != "b" and lst[x][-1] != "B":
#         list_none.append(lst[x])
#     if lst[x][0] != "a" and lst[x][0] != "A" and lst[x][0] != "b" and lst[x][0] != "B":
#         list_none.append(lst[x])

# print(list_Aa)
# print(list_Bb)
# print(list_none)

### classwork 3

# lst = []
# iyofa_7_11 = ["iyofa_7_11"]
# kentia_3 = ["kentia_3"]


# for i in range(10):
#     lst.append(int(input("enter a number: ")))

# for i in range(len(lst)):
#     if lst[i] % 7 == 0 and lst[i] % 11 == 0:
#         iyofa_7_11.append(lst[i])
#     if lst[i] % 2 != 0 and lst[i] % 3 == 0:
#         kentia_3.append(lst[i])


# print(iyofa_7_11)
# print(kentia_3)

### classwork 4

# lst = []
# xmvn_tnxmvn = ["iwyeba xmovnit da mtavrdeba tanxmovnit"]
# tnxmvn_xmvn = ["iwyeba tanxmovnit da mtavrdeba xmovnit"]

# for i in range(10):
#     lst.append(input("enter anything: "))

# for i in range(len(lst)):
#     if lst[i][0] == "a"  or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
#         if lst[i][-1] != "a" and lst[i][-1] != "e" and lst[i][-1] != "i" and lst[i][-1] != "o" and lst[i][-1] != "u" and lst[i][-1] != "A" and lst[i][-1] != "E" and lst[i][-1] != "I" and lst[i][-1] != "O" or lst[i][-1] != "U":
#             xmvn_tnxmvn.append(lst[i])
#     if lst[i][-1] == "a"  or lst[i][-1] == "e" or lst[i][-1] == "i" or lst[i][-1] == "o" or lst[i][-1] == "u" or lst[i][-1] == "A" or lst[i][-1] == "E" or lst[i][-1] == "I" or lst[i][-1] == "O" or lst[i][-1] == "U":
#         if lst[i][0] != "a" and lst[i][0] != "e" and lst[i][0] != "i" and lst[i][0] != "o" and lst[i][0] != "u" and lst[i][0] != "A" and lst[i][0] != "E" and lst[i][0] != "I" and lst[i][0] != "O" and lst[i][0] != "U":
#             tnxmvn_xmvn.append(lst[i])
    
    
# print(xmvn_tnxmvn)
# print(tnxmvn_xmvn)

### classwork 5

lst = []
xmvn_cifri = ["iwyeba xmovnit da mtavrdeba cifrit : "]
cifri_tnxmvn = ["iwyeba cifrit da mtavrdeba tanxmovnit : "]

for i in range(5):
    lst.append(input("enter anything: "))

for i in range(len(lst)):
    if lst[i][0] == "a"  or lst[i][0] == "e" or lst[i][0] == "i" or lst[i][0] == "o" or lst[i][0] == "u" or lst[i][0] == "A" or lst[i][0] == "E" or lst[i][0] == "I" or lst[i][0] == "O" or lst[i][0] == "U":
        if lst[i][-1] == "1" or lst[i][-1] == "2" or lst[i][-1] == "3" or lst[i][-1] == "4" or lst[i][-1] == "5" or lst[i][-1] == "6"  or lst[i][-1] == "7"  or lst[i][-1] == "8"  or lst[i][-1] == "9":
            xmvn_cifri.append(lst[i])
    if lst[i][0] == "1" or lst[i][0] == "2" or lst[i][0] == "3" or lst[i][0] == "4" or lst[i][0] == "5" or lst[i][0] == "6"  or lst[i][0] == "7"  or lst[i][0] == "8"  or lst[i][0] == "9":
        if lst[i][-1] != "a" and lst[i][-1] != "e" and lst[i][-1] != "i" and lst[i][-1] != "o" and lst[i][-1] != "u" and lst[i][-1] != "A" and lst[i][-1] != "E" and lst[i][-1] != "I" and lst[i][-1] != "O" and lst[i][-1] != "U":
            cifri_tnxmvn.append(lst[i])

print(xmvn_cifri)
print(cifri_tnxmvn)


        
    
