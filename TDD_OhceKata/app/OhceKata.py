import datetime

def saludar(name,hora = datetime.datetime.now().hour):
    if hora >= 20 or hora < 6:
        return "¡Buenas noches " + name + "!"
    if hora >= 6 and hora < 12:
        return "¡Buenos días " + name + "!"
    if hora >= 12 and hora < 20:
        return "¡Buenas tardes " + name + "!"

def isPalindrome(word):
    if(word == word[::-1]):
        cad = "¡Bonita palabra!"
    else:
        cad = ""
    return [word[::-1], cad]
