import os

print(os.getcwd())

os.chdir(r"D:\clear the clutter")

print(os.getcwd())

x = os.listdir(r"D:\clear the clutter")


for i in x:
 print(i)
 x1, y = os.path.splitext(r"D:\clear the clutter")
 print(x1, y)
 f = os.path.splitext(i)
 print(f)