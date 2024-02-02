import random

def generate_random_code(string):
    code = ''.join(random.choices(string, k=10))
    return code


