# დაწერე პროგრამა, რომელიც:
# სთხოვს მომხმარებელს შეიყვანოს წინადადება.
# ციკლის გამოყენებით დათვლის, რამდენი სიტყვაა ტექსტში.
# სიტყვებს შორის დაშორებად ჩაითვალოს მხოლოდ გამოტოვება (space).
# შედეგი დაბეჭდოს.

text = input(" Enter a random text : ")
word_count = 0
inWord = False
for i in text :
    if i != " " and not inWord : 
        word_count += 1
        inWord = True
    elif i == " " :
        inWord = False

print(word_count)