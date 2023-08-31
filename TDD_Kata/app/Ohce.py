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
    cadena = word.lower().replace(" ","") 
    if( cadena == cadena[::-1]):
        return "¡Bonita palabra!"
    else:
        return ""
    
def saludo_adios(name,hora):
    return saludar(name,hora) + "\n¡Adios " + name + "!"

def all(name,hora,lista):
    cadena = saludar(name,hora)
    i = 0
    while lista[i] != "Stop!":
        cadena += "\n" + reverse(lista[i])
        if(isPalindrome(lista[i]) != ""):
            cadena += "\n" + isPalindrome(lista[i])
        i = i + 1
    cadena += "\nAdios " + name
    return cadena