import random
import string


def generate_password():
    password = ''
    for i in range(8):
        password += random.choice(string.ascii_letters + string.digits)
    return password
