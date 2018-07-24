# Replace the placeholders with code and run the Python program

name = ["Stirling","Lana","Cyril","Pam","Ray","Cheryl"]
alias =["Duchess","Truckasaurus","Chet","Cookie Monster","Gilles de Rais","Cherlene"]

dict = {}

for i in range(0,len(name)):
    dict[name[i]]=alias[i]


for item in sorted(dict):
    print(item," : ",dict[item])

