import os

print(os.getcwd())

os.chdir(r"D:\clear the clutter")

print(os.getcwd())

x = os.listdir(r"D:\clear the clutter")

for i in x:
 print(i)


