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

folder_path = input("enter your folder path\n:")  # inputing file path does'nt need to add r at the start of the path

os.chdir(folder_path[1:-1])

print(os.getcwd())

x = os.listdir(folder_path[1:-1]) # list of files in clutter dir 



for i in x:  # list[song.mp3,main.py]
 condition = False 
 f = os.path.splitext(i) # split music.mp3 to ("music",".mp3")
 

 for ii in l.items(): # key[0] and values[1] 
     
    for iii in ii[1]: # in value list  iii = .mp3,main.py  etc
      if f[1] == iii and os.path.isfile(i):

        os.makedirs(ii[0], exist_ok = True) # exist_ok = True is for if file already existed dont throw error 
        print("true")

        shutil.move(i,os.path.join(ii[0],i))
        condition = True
        break
    if condition == True:
      break    
 if condition == False and os.path.isfile(i):
  os.makedirs("mislenious", exist_ok=True)
  shutil.move(i,os.path.join("mislenious",i))


      
# everything is new in this project i'll rate this hard difficulty for 
