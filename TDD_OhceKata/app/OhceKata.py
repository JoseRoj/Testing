import datetime
def saludar_noche(name,hora = datetime.datetime.now().hour):
    if hora == 20 or hora == 6:
        return "¡Buenas noches " + name + "!"

def saludar_tarde(name,hora = datetime.datetime.now().hour):
    if hora == 12 or hora == 18:
        return "¡Buenas tardes " + name + "!"

def saludar_dia(name,hora = datetime.datetime.now().hour):
    if hora == 10 or hora == 8:
        return "¡Buenos días " + name + "!"
