def saludar(name,hora):
    if hora >= 20 or hora < 6:
        return "¡Buenas noches " + name + "!"
    if hora >= 6 and hora < 12:
        return "¡Buenos días " + name + "!"
    if hora >= 12 and hora < 20:
        return "¡Buenas tardes " + name + "!"
