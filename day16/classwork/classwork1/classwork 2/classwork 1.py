def manual_capitalize(text):
    if not text :
        return text
    letter1 = text[0].upper()
    rest = text[1:].lower()
    return letter1 + rest

print(manual_capitalize("ME MiyvARS mANGoebi"))

def manual_title(text):
    result = ""
    text1 = text.split()
    for word in text1:
        if len(word) > 0:
            result += word[0].upper() + word[1:].lower() + " "
    return result.strip()

print(manual_title("ME miYVArS MaNgOEBI"))



    