def saludar(name,hora):
    if hora >= 20 or hora < 6:
        return "¡Buenas noches " + name + "!"
    elif hora >= 6 and hora < 12:
        return "¡Buenos días " + name + "!"
    else: 
        return "¡Buenas tardes " + name + "!"

def reverse(word):
    cadena = word[::-1]
    return cadena