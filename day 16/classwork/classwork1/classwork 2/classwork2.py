# შექმენი საკუთარი ფუნქცია, რომელსაც გადაეცემა სიტყვა და დაბრუნებს მას "capitalize" მსაგავსაად.
# def manual_capitalize(text):
#     result = text[0].upper() + text[1:].lower()
#     return result

# print(manual_capitalize("ME Dzalian MIYvaRs KaRaLiOkI"))

#წარმოიდგინე რომ შენი ხარ წიგნის ყდის დიზაინერი შენ უნდა დაწერო წინადადება ისე, როგორც წიგნის სათაურები. მაგრამ არის რაღაც სიტყვები რომლებიც არ უნდა დაერო დიდად თუ ისინი არ არიან დასაწყისში ეს სიტყვები :  and, the , of ,in on ,at, with, a, an.

# def custom_title_function(text):
#     if not text : 
#        return text
#     result = ""
#     nono_words = ["and" , "the" , "of" , "in" , "on" , "at" , "with" , "a" , "an"]
#     text1 = text.split()
#     for word in text1:
#         for nono in nono_words:
#             if word != nono:
#                 if len(word) > 0 :
#                     result += word[0].upper() + word[1:].lower() + " "
#     return result
# print(custom_title_function("harry potter and the chamber of secrets"))

def myTitle(text):
    nono_words = ["and" , "the" , "of" , "in" , "on" , "at" , "with" , "a" , "an"]
    words = text.lower().split()
    result = []
    for i in range(len(words)) :
        word = words[i]
        if i == 0 or word not in nono_words:
            word = word[0].upper() + word[1:].lower()
        result.append(word)
    return " ".join(result)

print(myTitle("harry potter and the chamber of secrets"))