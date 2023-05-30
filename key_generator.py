import random
import string

def get_random_derived_key(n=43):
    posible_characters = string.ascii_letters + string.digits + "/"

    derived_key = ''.join(random.choice(posible_characters) for char in range(n))

    return derived_key + '='

def get_random_iv(n=16):
    return int(''.join(random.choice(string.digits) for digit in range(n)))
