def fizz_buzz(number):
    if number%5 == 0:
        if number%3 == 0:
            return "fizzbuzz"
        return "buzz"
    elif number%3 == 0:
        return "fizz"
    return number
