import os
import shutil
import time

path=input("Enter path of the folder .")
days=30
time = time.time()-(days*24*60*60)

if os.path.exists(path):
    for root,files,folders in os.walk(path,topdown=True):
        for name in files :
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime
        
            if time >= ctime:
                os.remove(path)
                print("Deleted file from"+path+"successfully.")
        
        for name in folders :
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime

            if time >= ctime :
                shutil.rmtree(path)
                print("Deleted file from"+path+"successfully.")

else:
    print("Path not found")
    path = input("Re-enter the path of the folder")
    