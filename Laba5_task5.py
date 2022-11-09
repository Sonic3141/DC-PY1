def get_random_password() -> str:
    import random
    import string
    n = 8 #пароль длины n (по умолчанию 8 символов)
    alphabet = string.ascii_letters + string.digits #алфавит из  A - Z, a - z и 0 - 9
    stri= ''.join(random.sample(alphabet, n)) #  по условию следует использовать функцию sample из модуля random.
    return stri

print(get_random_password()) #вывод пароля
