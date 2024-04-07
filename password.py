# Empiezo
from random import sample
def password_generator(longitud):
    abc = "abcdefghijklmnopqrstwyz"
    abc_upper = abc.upper()
    num = "0123456789"
    simbols = "!@$%^&*()_+"
    secuencia = abc + abc_upper + num + simbols
    secuencia_sample = sample(secuencia,longitud)
    password_g = "".join(secuencia_sample)
    return password_g
password = password_generator(15)
print(password)