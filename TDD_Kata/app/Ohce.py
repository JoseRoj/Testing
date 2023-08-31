def saludar(name,hora):
    if hora >= 20 or hora < 6:
        return "¡Buenas noches " + name + "!"
    elif hora >= 6 and hora < 12:
        return "¡Buenos días " + name + "!"
    else: 
        return "¡Buenas tardes " + name + "!"

def reverse(word):
    return word[::-1]

def isPalindrome(word):
    if(word == word[::-1]):
        return "¡Bonita palabra!"
    else:
        return ""