import random
import string

def random_str_generator(size=5,chars= string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
