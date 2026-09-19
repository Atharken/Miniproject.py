import os

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

x = os.listdir(r"D:\clear the clutter")


for i in x:
 
 f = os.path.splitext(i)
 #print(f[1])

 for ii in l.items():
    for iii in ii[1]:
      if f[1] == iii:
        print("true")
      
      if f[1] == iii:
        print("true")