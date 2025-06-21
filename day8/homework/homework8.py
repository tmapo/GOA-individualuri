num = 1

ind = 0
jami = 0
lst1 = []
lst_jami = []

while num < 200:
    lst1.append(str(num))
    num += 1

for i in lst1 :
    j = 0 
    for k in i:
        j += int(k)
    lst_jami.append(j)
    j = 0

lst2 = []
for i in lst_jami:
    if i > 15:
        lst2.append(lst_jami.index(i))


lst3 = []
for i in lst2 :
   lst3.append(lst1[i])

cvladi1 = set(lst3)
cvladi2 = list(cvladi1)

print(cvladi2)