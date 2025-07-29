#1) დაწერე Python პროგრამა, რომელიც:
#სთხოვს მომხმარებელს (user-ს) შეიყვანოს რაიმე ტექსტი.
#დაითვლის, რამდენი დიდი ასო (Uppercase) და პატარა ასო (Lowercase) არის ამ ტექსტში.

text = input("Enter a random text : ")
lowcs = text.lower()
hghcs = text.upper()
num = 0
hghNum = 0
lowNum = 0
while num < len(text):
    if text[num] != " ":
        if text[num] == hghcs[num]:
            hghNum += 1
    if text[num] != " ":
        if text[num] == lowcs[num]:
            lowNum += 1
    num += 1
print(" In the text -" , text , "- There is " , hghNum , " Highcase letters and " , lowNum ," Lowcase letters." )