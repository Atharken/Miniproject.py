import datetime
import time
n1 = datetime.datetime.now() 
print(n1.strftime("%y-%m-%d "))

while True:
   n = datetime.datetime.now() #from import datetime get datetime now() means current.
   
   print(n.strftime("%H:%M:%S"))
   
   time.sleep(1)