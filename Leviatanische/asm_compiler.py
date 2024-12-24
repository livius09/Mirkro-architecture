iner="mov R1 R2 nop"
ops={
    "nop":0,
    "mov": 1,
    "math":2,
    "jmp":3,
    "jif1":4,
    "jif2":5,
    "jb":6,

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
    "bus":31,
    
    "add":0,
    "sub":1,
    "mul":2,
    "div":3,
    "rem":4,
       
}

iner=iner.split(" ")

for i in range(len(iner)):
    iner[i]=hex(ops[iner[i]])

print(iner)


#mov 5 R1 
#thats the goal
