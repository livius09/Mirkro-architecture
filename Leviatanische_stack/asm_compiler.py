
ops={
    "nop":0,
    "mov": 1,
    "math":2,
    "jmp":3,
    "jif1":4,
    "jif2":5,
    "ret":6,
    

    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "ji": 9, 
    "Mi1":10,
    "Mi2":11,
    "Mo1":12,
    "Mi3":13,
    "Mi4":14,
    "Mo2":15,
    "pc":16,
    "bus":31,
    
    "add":0,
    "sub":1,
    "mul":2,
    "div":3,
    "rem":4,
       
}
with open("Leviatanische_stack/input.txt","r") as file:
    dat=file.readlines()

#remove coments
for i in range(len(dat)):
    dat[i]=dat[i].split("#")[0].strip()


zeil=[]
for i in range(len(dat)):

    dat[i]=dat[i].strip()
    if len(dat[i])!=0:
        zeil.append(dat[i].split(" ")) #split the lines into the ops

print("dat:")
print(dat)

labels={}
labeln=0

for k in range(len(zeil)):
    if len(zeil[k])==1 and zeil[k][0][-1]==':':
        labels[str(zeil[k][0])] = (k*4-labeln*4)
        labeln+=1



for el in labels.values():
    zeil.pop(int(el/4))

labels["li"]=7
print(labels)


#fill comands up with nop so you dont have to write it manualy # mov R2 R3 to mov R2 R3 nop
for k in range(len(zeil)):
    for i in range(4-len(zeil[k])):
        zeil[k].append("nop")

for k in range(len(zeil)):
    for i in range(len(zeil[k])):
        if len(zeil[k])==4 and zeil[k][i][-1]==':':
            zeil[k][i]=labels[str(zeil[k][i])]
        


#to give better read abylti # mov 5 R2   to mov bus R2 5 
for k in range(len(zeil)):
    if zeil[k][0]=="mov":
        try:
            nu=int(zeil[k][1])
        except:
            continue #if a exetion acours go to the next line

        zeil[k][1]="bus"
        zeil[k][3]=nu

print("used for replacing:")
print(zeil)

out="eror"
for k in range(len(zeil)):
    for i in range(len(zeil[k])):
        try:
            out=hex(ops[zeil[k][i]]) #try to get the op code from the dict
        except KeyError as ke:
            try:
                n=int(zeil[k][i]) #if its no opcode try casting it to a number
                out=hex(n)
            except:
                print("could not compile key not found")
                print(f"on line {k+1},{i+1}")
                #exit()

        print(out,end=" ")
    print()
