from random import sample
def password_generator(long):
    abc = "abcdefghijklmnopqrstuvwxz"
    abc_upper = abc.upper()
    num = "0123456789"
    simbols = "!@#$%^&*()"
    character = abc + abc_upper + num + simbols
    password_long = sample(character, long)
    new_pass = "".join(password_long)
    return new_pass
password = password_generator(12)
print(password)
