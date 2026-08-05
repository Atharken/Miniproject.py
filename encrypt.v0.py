import string
import random

text = str(input("enter your word\n:"))

alphabet = string.ascii_lowercase
r = random.sample(alphabet,3)

c = "".join(r)

alphabet2 = string.ascii_lowercase
r2 = random.sample(alphabet2,3)

d = "".join(r2)

def encry(text):
    return c + text[1:] + text[0] + d

x = encry(text)
print(x)
           
def decryt(x):
    return x[3:-3]
    
y = decryt(x)

def place(y):
    return y[-1] + y[0:-1]
    
z = place(y)
print(z)