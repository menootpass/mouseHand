import os
import pyautogui as pt
import json

vidCap = 0

os.system("clear")
con = int(input("==========WELCOME===========\nPilih Os Yang Anda Gunakan:\n1. Windows\n2. Linux\n3. Mac\n>>"))


if con == 1:
	vidCap = 1
elif con == 3:
	vidCap = 0
elif con == 2:
	vidCap = -1
else:
	print("Error")


informasi ={ 
    "os" : con,
    "vidcap" : vidCap
    
} 
    
# the json file where the output must be stored 
out_file = open("data.json", "r+") 
    
json.dump(informasi, out_file, indent = 6) 
    
out_file.close() 


import index