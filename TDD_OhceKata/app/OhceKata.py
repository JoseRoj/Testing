import datetime

def saludar(name,hora = datetime.datetime.now().hour):
    if hora >= 20 or hora < 6:
        return "¡Buenas noches " + name + "!"
    if hora >= 6 and hora < 12:
        return "¡Buenos días " + name + "!"
    if hora >= 12 and hora < 20:
        return "¡Buenas tardes " + name + "!"

def isPalindrome(word):
    cadena = word.lower().replace(" ","")
    if(cadena == cadena[::-1]):
        return [word[::-1], "¡Bonita palabra!"]
    else:
        return word[::-1]
