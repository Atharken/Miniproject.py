import os
import shutil


l = {
 "audio" : [".mp3", ".wav", ".m4a"],
 "images" : [".png", ".jpg", ".jpeg", ".gif", ".webp"],
 "videos" : [".mp4", ".mkv", ".avi", ".mov"],
 "documents" : [".pdf", ".docx", ".doc", ".txt"],
 "archives" : [".zip", ".rar", ".7z"],
 "code" : [".py", ".js", ".html", ".css"]
}
print(os.getcwd())

os.chdir(r"D:\clear the clutter")

print(os.getcwd())

x = os.listdir(r"D:\clear the clutter") # list of files in clutter dir 


for i in x:  
 
 f = os.path.splitext(i) # split music.mp3 to ("music",".mp3")
 

 for ii in l.items(): # key[0] and values[1] 
     
    for iii in ii[1]: # in value list
      if f[1] == iii:

        os.makedirs(ii[0], exist_ok = True) # exist_ok = True is for if file already existed dont throw error 
        print("true")

        shutil.move(i,os.path.join(ii[0],i) )

      
# everything is new in this project i'll rate this medium to hard difficulty