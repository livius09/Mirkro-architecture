iner="mov R1 R2 nop"
ops={
    "mov": 1,
    "math":2,
    "nop":0,
    "R1":1,
    "R2":2,
    "R3":3,   
}

iner=iner.split(" ")

for i in range(len(iner)):
    iner[i]=ops[iner[i]]

print(iner)

#mov 5 R1 
#thats the goal